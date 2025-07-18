from openai import OpenAI, AzureOpenAI
from pydantic import Field, AliasChoices, computed_field
from pydantic_settings import BaseSettings
from openai.types.shared import ChatModel

from src.trending_ai.models import GitHubRepository


class OpenAIConfig(BaseSettings):
    api_type: str = Field(
        default="openai",
        description="The api type from openai for calling models.",
        examples=["openai", "azure"],
        validation_alias=AliasChoices("OPENAI_API_TYPE"),
        frozen=False,
        deprecated=False,
    )
    base_url: str = Field(
        ...,
        description="The base url from openai for calling models.",
        examples=["https://api.openai.com/v1", "https://xxxx.openai.azure.com"],
        validation_alias=AliasChoices("OPENAI_BASE_URL", "AZURE_OPENAI_ENDPOINT"),
        frozen=False,
        deprecated=False,
    )
    api_key: str = Field(
        ...,
        description="The api key from openai for calling models.",
        examples=["sk-proj-...", "141698ac..."],
        validation_alias=AliasChoices("OPENAI_API_KEY", "AZURE_OPENAI_API_KEY"),
        frozen=False,
        deprecated=False,
    )
    api_version: str = Field(
        default="2025-04-01-preview",
        description="The api version from openai for calling models.",
        examples=["2025-04-01-preview"],
        validation_alias=AliasChoices("OPENAI_API_VERSION"),
        frozen=False,
        deprecated=False,
    )


class TrendingAnalysis(OpenAIConfig):
    model: ChatModel | str = Field(
        ...,
        title="LLM Model Selection",
        description="This model should be OpenAI Model.",
        frozen=False,
        deprecated=False,
    )

    @computed_field
    @property
    def client(self) -> OpenAI | AzureOpenAI:
        if self.api_type == "azure":
            client = AzureOpenAI(
                api_key=self.api_key,
                azure_endpoint=self.base_url,
                api_version=self.api_version,
                azure_deployment=self.model,
            )
        else:
            client = OpenAI(api_key=self.api_key)
        return client

    def get_analysis(self, repo: GitHubRepository) -> str:
        prompt = f"""
        You are an expert in analyzing GitHub repositories.
        This repository is from Github trending, please notice some highlight points and summary what this repo is doing.

        {repo.model_dump_json()}
        You must reply it as a technical report in markdown format.
        """

        response = self.client.chat.completions.create(
            model=self.model, messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
