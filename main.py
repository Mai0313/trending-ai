"""Main entry point for TrendingAI - GitHub trending repositories analyzer.

This script fetches trending repositories from GitHub, organizes them by programming language,
and downloads their README files for analysis.
"""

import sys

from src.trending_ai.analyzer import TrendingAnalyzer
from src.trending_ai.github_client import GitHubAPIClient


def main() -> None:
    """Main function to run the trending repositories analysis."""
    github_client = GitHubAPIClient()
    analyzer = TrendingAnalyzer(github_client, output_dir="output")

    try:
        trending_data = analyzer.analyze_trending_repositories(since="daily")
        analyzer.print_language_summary(trending_data)
        all_repositories = []
        for repos in trending_data.repositories_by_language.values():
            all_repositories.extend(repos)
        readmes = analyzer.download_readmes(all_repositories)
        analyzer.save_analysis_results(trending_data, readmes)
        sorted_languages = sorted(
            trending_data.languages.items(), key=lambda x: x[1].count, reverse=True
        )[:10]

        for i, (language, stats) in enumerate(sorted_languages, 1):
            print(
                f"   {i:2d}. {language}: {stats.count} repositories ({stats.total_stars} total stars)"
            )

    except KeyboardInterrupt:
        print("\n\n⏹️  Analysis interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error during analysis: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
