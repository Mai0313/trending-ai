"""GitHub API client for fetching trending repositories and README files."""

import re
import time
import base64
from typing import Any, Literal
import datetime
from collections import defaultdict

from bs4 import BeautifulSoup
import httpx
import logfire
from pydantic import Field, ConfigDict, computed_field
from pydantic_settings import BaseSettings

from src.trending_ai.models import ReadmeData, TrendingData, LanguageStats, GitHubRepository


class GitHubAPIConfig(BaseSettings):
    """Configuration for GitHub API client.

    Attributes:
        base_url (str): The base URL for GitHub API
        token (Optional[str]): GitHub personal access token for authentication
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
    token: str | None = Field(
        default=None,
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
    def headers(self) -> dict[str, str]:
        headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        }
        if self.token:
            headers.update({"Authorization": f"token {self.token}"})
        return headers

    def _parse_full_names(self, response: httpx.Response) -> list[str]:
        soup = BeautifulSoup(response.content, "html.parser")
        full_names = []
        repo_links = soup.select('h2.h3.lh-condensed a[href^="/"]')
        if not repo_links:
            repo_links = soup.select('article h2 a[href^="/"]')
        if not repo_links:
            repo_links = soup.select('h1.h3 a[href^="/"]')
        for link in repo_links:
            href = link.get("href", "")
            # Extract owner/repo from href like "/owner/repo"
            match: re.Match[str] | None = re.match(r"^/([^/]+/[^/]+)", href)
            if match:
                full_name = match.group(1)
                full_names.append(full_name)
                logfire.info("Found trending repository", full_name=full_name)
        return full_names

    def _make_request(self, url: str, params: dict[str, Any] | None = None) -> httpx.Response:
        with httpx.Client(params=params, headers=self.headers) as client:
            response = client.get(url)
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
            return response

    def get_trendings(
        self,
        language: Literal["python", "go", "rust", None],
        since: Literal["daily", "weekly", "monthly"],
    ) -> list[GitHubRepository]:
        # Build trending page URL
        trending_url = "https://github.com/trending"
        if language:
            trending_url += f"/{language}"

        response = self._make_request(url=trending_url, params={"since": since})
        full_names = self._parse_full_names(response=response)

        repositories: list[GitHubRepository] = []
        for full_name in full_names:
            logfire.info("Fetching repository details from GitHub API", full_name=full_name)
            repo = self.get_info(full_name=full_name)
            repositories.append(repo)
        return repositories

    def get_info(self, full_name: str) -> GitHubRepository:
        url = f"{self.base_url}/repos/{full_name}"
        response = self._make_request(url=url)
        repo_dict: dict[str, Any] = response.json()
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
                fetched_at=datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"),
            )
        return repo

    def get_readme(self, full_name: str) -> ReadmeData:
        url = f"{self.base_url}/repos/{full_name}/readme"

        response = self._make_request(url=url)
        data: dict[str, Any] = response.json()

        content = data.get("content", "")
        encoding = data.get("encoding", "utf-8")

        if encoding == "base64":
            data.update({"content": base64.b64decode(content).decode("utf-8")})

        readme = ReadmeData(
            repository_full_name=full_name,
            content=data.get("content", ""),
            encoding=data.get("encoding", "utf-8"),
            size=data.get("size", 0),
            download_url=data.get("download_url"),
            fetched_at=datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"),
        )
        return readme

    def get_summary(self, repositories: list[GitHubRepository]) -> TrendingData:
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
            fetched_at=datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"),
            total_repositories=len(repositories),
            languages=languages,
            repositories_by_language=dict(repositories_by_language),
        )

        return trending_data
