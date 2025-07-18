"""Analyzer for processing trending repositories and organizing them by language."""

import json
import base64
from typing import Any
from pathlib import Path
import datetime
from collections import defaultdict

from pydantic import Field, model_validator

from src.trending_ai.models import ReadmeData, TrendingData, LanguageStats, GitHubRepository
from src.trending_ai.github_client import GitHubAPIClient


class TrendingAI(GitHubAPIClient):
    output_dir: Path = Field(default=Path("./data"))

    @model_validator(mode="after")
    def _setup(self) -> "TrendingAI":
        self.output_dir.mkdir(exist_ok=True, parents=True)
        return self

    def analyze_trending_repositories(self, since: str = "daily") -> TrendingData:
        """Analyze trending repositories and organize them by programming language.

        Args:
            since (str): Time period ('daily', 'weekly', 'monthly')

        Returns:
            TrendingData: Complete analysis results
        """
        # Fetch trending repositories
        repositories = self.get_trending_repositories(language=None, since=since)

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

    def _get_repository_readme(self, full_name: str) -> ReadmeData | None:
        """Get the README file for a repository.

        Args:
            full_name (str): The full name of the repository (owner/repo)

        Returns:
            Optional[ReadmeData]: The README data if found, None otherwise
        """
        url = f"{self.base_url}/repos/{full_name}/readme"

        data = self._make_request(url=url)

        # Decode content if it's base64 encoded
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

    def download_readmes(self, repositories: list[GitHubRepository]) -> dict[str, ReadmeData]:
        """Download README files for a list of repositories.

        Args:
            repositories (List[GitHubRepository]): List of repositories

        Returns:
            Dict[str, ReadmeData]: Dictionary mapping repository full name to README data
        """
        readmes = {}
        for repo in repositories:
            readme = self._get_repository_readme(repo.full_name)
            if readme:
                readmes[repo.full_name] = readme
        return readmes

    def save_analysis_results(
        self, trending_data: TrendingData, readmes: dict[str, ReadmeData]
    ) -> None:
        """Save analysis results to files.

        Args:
            trending_data (TrendingData): The trending data analysis
            readmes (Dict[str, ReadmeData]): README files data
        """
        timestamp = trending_data.fetched_at.strftime("%Y%m%d_%H%M%S")

        # Save trending data summary
        summary_file = self.output_dir / f"trending_summary_{timestamp}.json"
        with open(summary_file, "w", encoding="utf-8") as f:
            # Create a serializable version of the data
            summary_data: dict[str, Any] = {
                "fetched_at": trending_data.fetched_at.isoformat(),
                "total_repositories": trending_data.total_repositories,
                "languages_count": len(trending_data.languages),
                "languages": {},
            }

            for lang, stats in trending_data.languages.items():
                summary_data["languages"][lang] = {
                    "count": stats.count,
                    "total_stars": stats.total_stars,
                    "average_stars": round(stats.average_stars, 2),
                }

            json.dump(summary_data, f, indent=2, ensure_ascii=False)

        # Save repositories by language
        for language, repos in trending_data.repositories_by_language.items():
            # Clean language name for filename
            safe_language = "".join(
                c for c in language if c.isalnum() or c in (" ", "-", "_")
            ).rstrip()
            lang_file = self.output_dir / f"repositories_{safe_language}_{timestamp}.json"

            repos_data = []
            for repo in repos:
                repo_data = {
                    "name": repo.name,
                    "full_name": repo.full_name,
                    "description": repo.description,
                    "html_url": repo.html_url,
                    "language": repo.language,
                    "stargazers_count": repo.stargazers_count,
                    "forks_count": repo.forks_count,
                    "created_at": repo.created_at,
                    "updated_at": repo.updated_at,
                    "owner": {
                        "login": repo.owner.login,
                        "html_url": repo.owner.html_url,
                        "type": repo.owner.type,
                    },
                    "topics": repo.topics,
                }
                repos_data.append(repo_data)

            with open(lang_file, "w", encoding="utf-8") as f:
                json.dump(repos_data, f, indent=2, ensure_ascii=False)

        # Save README files
        if readmes:
            readme_dir = self.output_dir / f"readmes_{timestamp}"
            readme_dir.mkdir(exist_ok=True)

            for full_name, readme in readmes.items():
                # Create safe filename
                safe_name = full_name.replace("/", "_").replace("\\", "_")
                readme_file = readme_dir / f"{safe_name}_README.md"

                with open(readme_file, "w", encoding="utf-8") as f:
                    f.write(f"# {full_name}\n\n")
                    f.write(f"Repository: https://github.com/{full_name}\n")
                    f.write(f"Fetched at: {readme.fetched_at.isoformat()}\n")
                    f.write(f"Size: {readme.size} bytes\n\n")
                    f.write("---\n\n")
                    f.write(readme.content)
