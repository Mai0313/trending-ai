"""GitHub API client for fetching trending repositories and README files."""

import time
import base64
from datetime import datetime

from pydantic import Field
import requests
from pydantic_settings import BaseSettings

from src.trending_ai.models import GitHubUser, ReadmeData, GitHubRepository


class GitHubAPIConfig(BaseSettings):
    """Configuration for GitHub API client.

    Attributes:
        base_url (str): The base URL for GitHub API
        api_key (Optional[str]): GitHub personal access token for authentication
        per_page (int): Number of items per page for pagination
        max_pages (int): Maximum pages to fetch
        rate_limit_delay (float): Delay between requests to avoid rate limiting
    """

    base_url: str = Field(
        default="https://api.github.com",
        description="The base URL for GitHub API",
        frozen=False,
        deprecated=False,
    )
    api_key: str = Field(
        description="GitHub personal access token for authentication",
        validation_alias="GITHUB_TOKEN",
        frozen=False,
        deprecated=False,
    )
    per_page: int = Field(
        default=100,
        description="Number of items per page for pagination",
        frozen=False,
        deprecated=False,
    )
    max_pages: int = Field(
        default=10, description="Maximum pages to fetch", frozen=False, deprecated=False
    )
    rate_limit_delay: float = Field(
        default=1.0,
        description="Delay between requests to avoid rate limiting",
        frozen=False,
        deprecated=False,
    )


class GitHubAPIClient:
    """Client for interacting with GitHub API."""

    def __init__(self, config: GitHubAPIConfig):
        """Initialize the GitHub API client.

        Args:
            config (GitHubAPIConfig): Configuration for the API client
        """
        self.config = config
        self.session = requests.Session()

        # Set up headers
        self.session.headers.update({
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "TrendingAI/1.0",
        })

        if self.config.api_key:
            self.session.headers.update({"Authorization": f"token {self.config.api_key}"})

    def _make_request(self, url: str, params: dict | None = None) -> dict:
        """Make a request to the GitHub API with rate limiting.

        Args:
            url (str): The API endpoint URL
            params (Optional[Dict]): Query parameters

        Returns:
            Dict: The JSON response from the API

        Raises:
            requests.RequestException: If the request fails
        """
        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()

            # Check rate limit
            remaining = int(response.headers.get("X-RateLimit-Remaining", 0))
            if remaining < 10:
                reset_time = int(response.headers.get("X-RateLimit-Reset", 0))
                sleep_time = max(reset_time - int(time.time()), 0) + 1
                print(f"Rate limit low ({remaining}), sleeping for {sleep_time} seconds...")
                time.sleep(sleep_time)

            # Add delay between requests
            time.sleep(self.config.rate_limit_delay)

            return response.json()

        except requests.RequestException as e:
            print(f"Error making request to {url}: {e}")
            raise

    def get_trending_repositories(
        self, language: str | None = None, since: str = "daily"
    ) -> list[GitHubRepository]:
        """Get trending repositories from GitHub.

        Since GitHub doesn't have an official trending API, we'll use the search API
        with specific parameters to get recently popular repositories.

        Args:
            language (Optional[str]): Filter by programming language
            since (str): Time period ('daily', 'weekly', 'monthly')

        Returns:
            List[GitHubRepository]: List of trending repositories
        """
        # Calculate date for "since" parameter
        days_map = {"daily": 1, "weekly": 7, "monthly": 30}
        days = days_map.get(since, 1)

        # Create search query for recently created/updated popular repositories
        from datetime import datetime, timedelta

        date_threshold = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")

        query_parts = [
            f"created:>{date_threshold}",
            "stars:>1",  # Only repositories with at least 1 star
        ]

        if language:
            query_parts.append(f"language:{language}")

        query = " ".join(query_parts)

        params = {"q": query, "sort": "stars", "order": "desc", "per_page": self.config.per_page}

        repositories = []

        for page in range(1, self.config.max_pages + 1):
            params["page"] = page
            url = f"{self.config.base_url}/search/repositories"

            try:
                data = self._make_request(url, params)
                items = data.get("items", [])

                if not items:
                    break

                for item in items:
                    try:
                        # Create user object
                        owner_data = item["owner"]
                        owner = GitHubUser(
                            login=owner_data["login"],
                            id=owner_data["id"],
                            avatar_url=owner_data["avatar_url"],
                            html_url=owner_data["html_url"],
                            type=owner_data["type"],
                        )

                        # Create repository object
                        repo = GitHubRepository(
                            id=item["id"],
                            name=item["name"],
                            full_name=item["full_name"],
                            description=item.get("description"),
                            html_url=item["html_url"],
                            language=item.get("language"),
                            stargazers_count=item["stargazers_count"],
                            forks_count=item["forks_count"],
                            open_issues_count=item["open_issues_count"],
                            created_at=item["created_at"],
                            updated_at=item["updated_at"],
                            pushed_at=item["pushed_at"],
                            owner=owner,
                            default_branch=item["default_branch"],
                            size=item["size"],
                            archived=item["archived"],
                            disabled=item["disabled"],
                            private=item["private"],
                            fork=item["fork"],
                            topics=item.get("topics", []),
                        )

                        repositories.append(repo)

                    except Exception as e:
                        print(f"Error parsing repository {item.get('full_name', 'unknown')}: {e}")
                        continue

                print(f"Fetched page {page}, got {len(items)} repositories")

            except Exception as e:
                print(f"Error fetching page {page}: {e}")
                break

        print(f"Total repositories fetched: {len(repositories)}")
        return repositories

    def get_repository_readme(self, full_name: str) -> ReadmeData | None:
        """Get the README file for a repository.

        Args:
            full_name (str): The full name of the repository (owner/repo)

        Returns:
            Optional[ReadmeData]: The README data if found, None otherwise
        """
        url = f"{self.config.base_url}/repos/{full_name}/readme"

        data = self._make_request(url)

        # Decode content if it's base64 encoded
        content = data.get("content", "")
        encoding = data.get("encoding", "utf-8")

        if encoding == "base64":
            try:
                content = base64.b64decode(content).decode("utf-8")
            except Exception as e:
                print(f"Error decoding README for {full_name}: {e}")
                content = content  # Keep original if decode fails

        readme = ReadmeData(
            repository_full_name=full_name,
            content=content,
            encoding=encoding,
            size=data.get("size", 0),
            download_url=data.get("download_url"),
            fetched_at=datetime.now(),
        )

        return readme

    def get_trending_repositories_all_languages(
        self, since: str = "daily"
    ) -> list[GitHubRepository]:
        """Get trending repositories for all languages.

        Args:
            since (str): Time period ('daily', 'weekly', 'monthly')

        Returns:
            List[GitHubRepository]: List of all trending repositories
        """
        print("Fetching trending repositories for all languages...")
        return self.get_trending_repositories(language=None, since=since)
