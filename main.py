from pathlib import Path

import logfire

from src.trending_ai.analyzer import TrendingAnalyzer
from src.trending_ai.github_client import GitHubAPIClient


def main() -> None:
    """Main function to run the trending repositories analysis."""
    github_client = GitHubAPIClient()
    analyzer = TrendingAnalyzer(github_client, output_dir=Path("output"))

    trending_data = analyzer.analyze_trending_repositories(since="daily")
    all_repositories = []
    for repos in trending_data.repositories_by_language.values():
        all_repositories.extend(repos)
    readmes = analyzer.download_readmes(all_repositories)
    analyzer.save_analysis_results(trending_data, readmes)
    sorted_languages = sorted(
        trending_data.languages.items(), key=lambda x: x[1].count, reverse=True
    )[:10]

    for i, (language, stats) in enumerate(sorted_languages, 1):
        logfire.info(
            f"{i:2d}. {language}: {stats.count} repositories ({stats.total_stars} total stars)"
        )


if __name__ == "__main__":
    main()
