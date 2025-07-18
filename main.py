from src.trending_ai.github_client import GitHubAPIClient
from src.trending_ai.trending import TrendingAI


def main() -> None:
    """Main function to run the trending repositories analysis."""
    trending = TrendingAI()
    repos = trending.analyze_trending_repositories()
    print(repos[0])


if __name__ == "__main__":
    main()
