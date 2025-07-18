from src.trending_ai.github_client import GitHubAPIClient


def main() -> None:
    """Main function to run the trending repositories analysis."""
    github_client = GitHubAPIClient()
    all_repos = github_client.get_trending_repositories()


if __name__ == "__main__":
    main()
