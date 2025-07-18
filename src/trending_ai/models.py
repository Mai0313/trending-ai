"""Models for GitHub API responses and application data structures."""

import datetime

from pydantic import Field, BaseModel


class GitHubUser(BaseModel):
    """GitHub user model.

    Attributes:
        login (str): The username of the user
        id (int): The unique user ID
        avatar_url (str): URL to the user's avatar image
        html_url (str): URL to the user's GitHub profile
        type (str): Type of account (User or Organization)
    """

    login: str = Field(..., description="The username of the user")
    id: int = Field(..., description="The unique user ID")
    avatar_url: str = Field(..., description="URL to the user's avatar image")
    html_url: str = Field(..., description="URL to the user's GitHub profile")
    type: str = Field(..., description="Type of account (User or Organization)")


class GitHubRepository(BaseModel):
    """GitHub repository model.

    Attributes:
        id (int): The unique repository ID
        name (str): The name of the repository
        full_name (str): The full name of the repository (owner/repo)
        description (Optional[str]): The description of the repository
        html_url (str): URL to the repository on GitHub
        language (Optional[str]): The primary programming language
        stargazers_count (int): Number of stars
        forks_count (int): Number of forks
        open_issues_count (int): Number of open issues
        created_at (str): Creation timestamp
        updated_at (str): Last update timestamp
        pushed_at (str): Last push timestamp
        owner (GitHubUser): The repository owner
        default_branch (str): The default branch name
        size (int): Repository size in KB
        archived (bool): Whether the repository is archived
        disabled (bool): Whether the repository is disabled
        private (bool): Whether the repository is private
        fork (bool): Whether the repository is a fork
        topics (List[str]): Repository topics/tags
    """

    id: int = Field(..., description="The unique repository ID")
    name: str = Field(..., description="The name of the repository")
    full_name: str = Field(..., description="The full name of the repository (owner/repo)")
    description: str | None = Field(None, description="The description of the repository")
    html_url: str = Field(..., description="URL to the repository on GitHub")
    language: str | None = Field(None, description="The primary programming language")
    stargazers_count: int = Field(..., description="Number of stars")
    forks_count: int = Field(..., description="Number of forks")
    open_issues_count: int = Field(..., description="Number of open issues")
    created_at: str = Field(..., description="Creation timestamp")
    updated_at: str = Field(..., description="Last update timestamp")
    pushed_at: str = Field(..., description="Last push timestamp")
    owner: GitHubUser = Field(..., description="The repository owner")
    default_branch: str = Field(..., description="The default branch name")
    size: int = Field(..., description="Repository size in KB")
    archived: bool = Field(..., description="Whether the repository is archived")
    disabled: bool = Field(..., description="Whether the repository is disabled")
    private: bool = Field(..., description="Whether the repository is private")
    fork: bool = Field(..., description="Whether the repository is a fork")
    topics: list[str] = Field(default_factory=list, description="Repository topics/tags")


class LanguageStats(BaseModel):
    """Statistics for a programming language.

    Attributes:
        language (str): The programming language name
        count (int): Number of repositories using this language
        repositories (List[GitHubRepository]): List of repositories using this language
        total_stars (int): Total stars across all repositories
        average_stars (float): Average stars per repository
    """

    language: str = Field(..., description="The programming language name")
    count: int = Field(..., description="Number of repositories using this language")
    repositories: list[GitHubRepository] = Field(
        ..., description="List of repositories using this language"
    )
    total_stars: int = Field(..., description="Total stars across all repositories")
    average_stars: float = Field(..., description="Average stars per repository")


class TrendingData(BaseModel):
    """Complete trending data structure.

    Attributes:
        fetched_at (datetime.datetime): When the data was fetched
        total_repositories (int): Total number of repositories fetched
        languages (Dict[str, LanguageStats]): Statistics by programming language
        repositories_by_language (Dict[str, List[GitHubRepository]]): Repositories grouped by language
    """

    fetched_at: datetime.datetime = Field(..., description="When the data was fetched")
    total_repositories: int = Field(..., description="Total number of repositories fetched")
    languages: dict[str, LanguageStats] = Field(
        ..., description="Statistics by programming language"
    )
    repositories_by_language: dict[str, list[GitHubRepository]] = Field(
        ..., description="Repositories grouped by language"
    )


class ReadmeData(BaseModel):
    """README file data model.

    Attributes:
        repository_full_name (str): The full name of the repository
        content (str): The README content
        encoding (str): The encoding of the content
        size (int): Size of the README file
        download_url (Optional[str]): URL to download the README
        fetched_at (datetime.datetime): When the README was fetched
    """

    repository_full_name: str = Field(..., description="The full name of the repository")
    content: str = Field(..., description="The README content")
    encoding: str = Field(..., description="The encoding of the content")
    size: int = Field(..., description="Size of the README file")
    download_url: str | None = Field(None, description="URL to download the README")
    fetched_at: datetime.datetime = Field(..., description="When the README was fetched")
