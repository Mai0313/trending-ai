"""Analyzer for processing trending repositories and organizing them by language."""

import json
from typing import Any
from pathlib import Path
from datetime import datetime
from collections import defaultdict

from src.trending_ai.models import ReadmeData, TrendingData, LanguageStats, GitHubRepository
from src.trending_ai.github_client import GitHubAPIClient


class TrendingAnalyzer:
    """Analyzer for processing and organizing trending GitHub repositories."""

    def __init__(self, github_client: GitHubAPIClient, output_dir: str = "output"):
        """Initialize the trending analyzer.

        Args:
            github_client (GitHubAPIClient): GitHub API client instance
            output_dir (str): Directory to save output files
        """
        self.github_client = github_client
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

    def analyze_trending_repositories(self, since: str = "daily") -> TrendingData:
        """Analyze trending repositories and organize them by programming language.

        Args:
            since (str): Time period ('daily', 'weekly', 'monthly')

        Returns:
            TrendingData: Complete analysis results
        """
        print(f"Starting analysis of {since} trending repositories...")

        # Fetch trending repositories
        repositories = self.github_client.get_trending_repositories_all_languages(since)

        # Group repositories by language
        repositories_by_language = defaultdict(list)

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
            fetched_at=datetime.now(),
            total_repositories=len(repositories),
            languages=languages,
            repositories_by_language=dict(repositories_by_language),
        )

        print(
            f"Analysis complete! Found {len(repositories)} repositories across {len(languages)} languages."
        )

        return trending_data

    def download_readmes(self, repositories: list[GitHubRepository]) -> dict[str, ReadmeData]:
        """Download README files for a list of repositories.

        Args:
            repositories (List[GitHubRepository]): List of repositories

        Returns:
            Dict[str, ReadmeData]: Dictionary mapping repository full name to README data
        """
        print(f"Downloading README files for {len(repositories)} repositories...")

        readmes = {}

        for i, repo in enumerate(repositories, 1):
            print(f"Downloading README {i}/{len(repositories)}: {repo.full_name}")

            readme = self.github_client.get_repository_readme(repo.full_name)
            if readme:
                readmes[repo.full_name] = readme

        print(f"Successfully downloaded {len(readmes)} README files.")
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

        print(f"Saved trending summary to: {summary_file}")

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

            print(f"Saved {len(repos)} {language} repositories to: {lang_file}")

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

            print(f"Saved {len(readmes)} README files to: {readme_dir}")

    def print_language_summary(self, trending_data: TrendingData) -> None:
        """Print a summary of languages and their repository counts.

        Args:
            trending_data (TrendingData): The trending data to summarize
        """
        print("\n" + "=" * 60)
        print("TRENDING REPOSITORIES SUMMARY")
        print("=" * 60)
        print(f"Fetched at: {trending_data.fetched_at}")
        print(f"Total repositories: {trending_data.total_repositories}")
        print(f"Programming languages: {len(trending_data.languages)}")
        print()

        # Sort languages by repository count
        sorted_languages = sorted(
            trending_data.languages.items(), key=lambda x: x[1].count, reverse=True
        )

        print(f"{'Language':<20} {'Count':<10} {'Total Stars':<15} {'Avg Stars':<12}")
        print("-" * 60)

        for language, stats in sorted_languages:
            print(
                f"{language:<20} {stats.count:<10} {stats.total_stars:<15} {stats.average_stars:<12.1f}"
            )

        print("\n" + "=" * 60)
