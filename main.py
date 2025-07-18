import json
import asyncio
from pathlib import Path
import datetime
from functools import cached_property

from pydantic import Field, computed_field, model_validator

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

    @computed_field
    @cached_property
    def repos(self) -> list[GitHubRepository]:
        """Get the trending repositories for the specified language and time period.
        Defaults to Python language and daily trending.
        """
        return self.get_trendings(language="python", since="daily")

    def analysis(self) -> None:
        for repo in self.repos:
            report = self.get_analysis(repo=repo, language="zh-TW")
            report_file = self.output_folder / f"{repo.name}.md"
            report_file.write_text(report, encoding="utf-8")

    async def a_analysis(self, limit: int = 10) -> None:
        """This version is faster, but you need to take care of the rate limit."""
        semaphore = asyncio.Semaphore(limit)

        async def _process_repo(repo: GitHubRepository) -> tuple[GitHubRepository, str]:
            async with semaphore:
                report = await self.a_get_analysis(repo=repo, language="zh-TW")
                return repo, report

        tasks = [_process_repo(repo) for repo in self.repos]
        results = await asyncio.gather(*tasks)
        for repo, report in results:
            report_file = self.output_folder / f"{repo.name}.md"
            report_file.write_text(report, encoding="utf-8")

    def trending(self) -> None:
        repo_list = [repo.model_dump() for repo in self.repos]
        output_path = self.output_folder / "github_trending.json"
        with output_path.open("w", encoding="utf-8") as f:
            json.dump(repo_list, f, indent=4, ensure_ascii=False)

    async def a_trending(self) -> None:
        self.trending()

    async def __call__(self) -> None:
        await self.a_trending()
        await self.a_analysis()


if __name__ == "__main__":
    import fire

    trending_ai = TrendingAI(model="gpt-4o")

    fire.Fire(trending_ai)
