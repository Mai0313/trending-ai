import json
from pathlib import Path
import datetime

from src.trending_ai.client import GitHubAPIClient


def main() -> None:
    """Main function to run the trending repositories analysis."""
    client = GitHubAPIClient()
    repos = client.get_trendings(language="python", since="daily")
    repo_list = [repo.model_dump() for repo in repos]
    today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    output_path = Path(f"./data/trending_repos_{today}.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(repo_list, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()
