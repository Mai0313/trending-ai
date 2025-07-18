"""Main entry point for TrendingAI - GitHub trending repositories analyzer.

This script fetches trending repositories from GitHub, organizes them by programming language,
and downloads their README files for analysis.
"""

import sys

from src.trending_ai.analyzer import TrendingAnalyzer
from src.trending_ai.github_client import GitHubAPIClient, GitHubAPIConfig


def main() -> None:
    """Main function to run the trending repositories analysis."""
    # Create GitHub API client configuration
    config = GitHubAPIConfig(
        per_page=100,
        max_pages=3,  # Limit to avoid excessive API calls
        rate_limit_delay=1.0,
    )

    # Initialize clients
    github_client = GitHubAPIClient(config)
    analyzer = TrendingAnalyzer(github_client, output_dir="output")

    try:
        # Analyze trending repositories
        print("📊 Analyzing trending repositories...")
        trending_data = analyzer.analyze_trending_repositories(since="daily")

        # Print summary
        analyzer.print_language_summary(trending_data)

        # Download README files for all repositories
        all_repositories = []
        for repos in trending_data.repositories_by_language.values():
            all_repositories.extend(repos)

        print(f"\n📚 Downloading README files for {len(all_repositories)} repositories...")
        readmes = analyzer.download_readmes(all_repositories)

        # Save results
        print("\n💾 Saving analysis results...")
        analyzer.save_analysis_results(trending_data, readmes)

        print("\n✅ Analysis complete!")
        print("📁 Results saved in the 'output' directory")
        print(f"📊 Total repositories analyzed: {len(all_repositories)}")
        print(f"📚 README files downloaded: {len(readmes)}")
        print(f"🌐 Programming languages found: {len(trending_data.languages)}")

        # Show top languages
        print("\n🏆 Top programming languages:")
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
