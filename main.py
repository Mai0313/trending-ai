import json
from pathlib import Path
import datetime

from pydantic import Field, model_validator

from src.trending_ai.client import GitHubAPIClient
from src.trending_ai.models import GitHubRepository
from src.trending_ai.analysis import TrendingAnalysis


class TrendingAI(GitHubAPIClient, TrendingAnalysis):
    output_folder: Path = Field(
        default=Path("./docs/report"),
        description="The folder you wanna save the reports and details.",
        frozen=False,
        deprecated=False,
    )

    @model_validator(mode="after")
    def _setup(self) -> "TrendingAI":
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        self.output_folder = self.output_folder / today
        self.output_folder.mkdir(parents=True, exist_ok=True)
        return self

    def analysis(self, repos: list[GitHubRepository] | None = None) -> list[GitHubRepository]:
        if not repos:
            repos = self.get_trendings(language="python", since="daily")
        for repo in repos:
            report = self.get_analysis(repo=repo, language="zh-TW")
            report_file = self.output_folder / f"{repo.name}.md"
            report_file.write_text(report, encoding="utf-8")
        return repos

    def trending(self, repos: list[GitHubRepository] | None = None) -> list[GitHubRepository]:
        if not repos:
            repos = self.get_trendings(language="python", since="daily")
        repo_list = [repo.model_dump() for repo in repos]
        output_path = self.output_folder / "github_trending.json"
        with output_path.open("w", encoding="utf-8") as f:
            json.dump(repo_list, f, indent=4, ensure_ascii=False)
        return repos

    def __call__(self) -> list[GitHubRepository]:
        repos = self.get_trendings(language="python", since="daily")
        self.trending(repos=repos)
        self.analysis(repos=repos)
        return repos


if __name__ == "__main__":
    trending_ai = TrendingAI(model="gpt-4.1")
    trending_ai()
