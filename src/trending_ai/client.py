"""GitHub API client for fetching trending repositories and README files."""

import re
import time
import base64
from typing import Any, Literal
import datetime
from collections import defaultdict

from bs4 import BeautifulSoup
import logfire
from pydantic import Field, ConfigDict, computed_field
import requests
from pydantic_settings import BaseSettings

from src.trending_ai.models import ReadmeData, TrendingData, LanguageStats, GitHubRepository


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


class GitHubAPIClient(GitHubAPIConfig):
    """Client for interacting with GitHub API."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    @computed_field
    @property
    def session(self) -> requests.Session:
        session = requests.Session()
        session.headers.update({
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Authorization": f"token {self.api_key}",
        })
        return session

    def _make_request(self, url: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        """Make a request to the GitHub API with rate limiting.

        Args:
            url (str): The API endpoint URL
            params (Optional[Dict]): Query parameters

        Returns:
            Dict: The JSON response from the API

        Raises:
            requests.RequestException: If the request fails
        """
        response = self.session.get(url, params=params)
        response.raise_for_status()

        # Check rate limit
        remaining = int(response.headers.get("X-RateLimit-Remaining", 0))
        if remaining < 10:
            reset_time = int(response.headers.get("X-RateLimit-Reset", 0))
            sleep_time = max(reset_time - int(time.time()), 0) + 1
            logfire.warning(
                "Rate Limit is Low",
                remaining=remaining,
                reset_time=reset_time,
                sleep_time=sleep_time,
            )
            time.sleep(sleep_time)

        # Add delay between requests
        time.sleep(self.rate_limit_delay)
        return response.json()

    def get_trendings(
        self,
        language: Literal["python", "go", "rust", None],
        since: Literal["daily", "weekly", "monthly"],
    ) -> list[GitHubRepository]:
        """Get trending repositories from GitHub trending page.

        Scrapes the GitHub trending page to get repository names,
        then fetches detailed information using GitHub API.

        Args:
            language (Literal["python", "go", "rust", None]): Filter by programming language
            since (Literal["daily", "weekly", "monthly"]): Time period

        Returns:
            List[GitHubRepository]: List of trending repositories
        """
        # Build trending page URL
        trending_url = "https://github.com/trending"
        params: dict[str, str] = {"since": since}
        if language:
            trending_url += f"/{language}"

        # Fetch trending page
        logfire.info(
            "Fetching trending repositories from GitHub trending page",
            url=trending_url,
            params=params,
        )

        response = self.session.get(trending_url, params=params)
        response.raise_for_status()

        # Parse HTML
        soup = BeautifulSoup(response.content, "html.parser")

        # Find repository links - they are typically in h2 tags with class "h3 lh-condensed"
        # or in article tags containing repository information
        repo_names = []

        # Look for repository links in the trending page
        # The structure is usually: <h2 class="h3 lh-condensed"><a href="/owner/repo">
        repo_links = soup.select('h2.h3.lh-condensed a[href^="/"]')

        if not repo_links:
            # Try alternative selectors if the main one doesn't work
            repo_links = soup.select('article h2 a[href^="/"]')

        if not repo_links:
            # Try another alternative
            repo_links = soup.select('h1.h3 a[href^="/"]')

        for link in repo_links:
            href = link.get("href", "")
            # Extract owner/repo from href like "/owner/repo"
            match: re.Match[str] | None = re.match(r"^/([^/]+/[^/]+)", href)
            if match:
                full_name = match.group(1)
                repo_names.append(full_name)
                logfire.info("Found trending repository", repo_name=full_name)

        # Fetch detailed information for each repository using GitHub API
        repositories: list[GitHubRepository] = []
        for repo_name in repo_names:
            logfire.info("Fetching repository details from GitHub API", repo_name=repo_name)
            url = f"{self.base_url}/repos/{repo_name}"
            repo_dict = self._make_request(url=url)
            repo = GitHubRepository(**repo_dict)
            try:
                repo.readme = self.get_readme(full_name=repo.full_name)
            except Exception:
                repo.readme = ReadmeData(
                    repository_full_name=repo.full_name,
                    content=f"No readme available, please check {repo.html_url}",
                    encoding="utf-8",
                    size=0,
                    download_url=None,
                    fetched_at=datetime.datetime.now(),
                )
            repositories.append(repo)
        return repositories

    def get_readme(self, full_name: str) -> ReadmeData:
        url = f"{self.base_url}/repos/{full_name}/readme"

        data = self._make_request(url=url)

        content = data.get("content", "")
        encoding = data.get("encoding", "utf-8")

        if encoding == "base64":
            content = base64.b64decode(content).decode("utf-8")

        readme = ReadmeData(
            repository_full_name=full_name,
            content=content,
            encoding=encoding,
            size=data.get("size", 0),
            download_url=data.get("download_url"),
            fetched_at=datetime.datetime.now(),
        )

        return readme

    def get_detail(self, repositories: list[GitHubRepository]) -> TrendingData:
        # Group repositories by language
        repositories_by_language: dict[str, list[GitHubRepository]] = defaultdict(list)
        for repo in repositories:
            language = repo.language or "Unknown"
            repositories_by_language[language].append(repo)

        # Calculate language statistics
        languages = {}
        for language, repos in repositories_by_language.items():
            total_stars = sum(repo.stargazers_count for repo in repos)
            average_stars = total_stars / len(repos) if repos else 0

            languages[language] = LanguageStats(
                language=language,
                count=len(repos),
                repositories=repos,
                total_stars=total_stars,
                average_stars=average_stars,
            )

        # Create trending data object
        trending_data = TrendingData(
            fetched_at=datetime.datetime.now(),
            total_repositories=len(repositories),
            languages=languages,
            repositories_by_language=dict(repositories_by_language),
        )

        return trending_data
