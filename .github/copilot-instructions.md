<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

⚠️ **IMPORTANT**: After making any code changes, adding features, or updating functionality, you MUST update .github/copilot-instructions.md to reflect the current project state and capabilities.

# Project Background

This is TrendingAI, a modern Python application that analyzes GitHub trending repositories using a hybrid approach combining web scraping and official GitHub API. The tool scrapes GitHub's trending page to discover trending repositories, then uses the GitHub API to fetch comprehensive metadata and README files. It's designed for researchers, developers, and data scientists who need to collect and analyze trending repository data for research, market analysis, or staying updated with technology trends.

# Project Structure / Features

## Core Application Features

- **Hybrid Data Collection**: Combines GitHub trending page web scraping with official API for complete data
- **Multi-language Support**: Supports filtering by specific programming languages (Python, Go, Rust) or collecting all languages
- **README Processing**: Automatic download and processing of README files with proper encoding detection (Base64, UTF-8)
- **AI-Powered Analysis**: Generate intelligent technical reports using OpenAI/Azure OpenAI for repository analysis
- **Structured Data Export**: Exports comprehensive JSON data with timestamps for easy integration with other tools
- **Intelligent Rate Limiting**: Handles GitHub API rate limits with automatic delays and monitoring

## Architecture Components

- **Main Entry Point**: `main.py` - Simple script that demonstrates basic usage
- **Core Package**: `src/trending_ai/` - Contains all application logic
    - `models.py` - Pydantic V2 data models for type-safe data structures
    - `client.py` - GitHub API client with web scraping capabilities and rate limiting
    - `analysis.py` - AI-powered repository analysis using OpenAI/Azure OpenAI
- **Output Directory**: `data/` - Generated JSON files with repository data and README content
- **Configuration**: Environment variables and Pydantic settings for GitHub token and client configuration

## Data Models (Pydantic V2)

- **GitHubUser**: User/organization information (login, ID, avatar, profile URL, account type)
- **GitHubRepository**: Complete repository metadata including stars, forks, language, topics, timestamps, and embedded README
- **ReadmeData**: README file content with metadata (content, encoding, size, download URL, fetch timestamp)
- **OpenAIConfig**: Configuration settings for OpenAI and Azure OpenAI integration
- **TrendingAnalysis**: AI analysis engine with OpenAI client management and repository analysis capabilities

## Key Capabilities

- **Trending Discovery**: Scrapes GitHub trending page using BeautifulSoup to find trending repository names
- **API Data Enrichment**: Uses GitHub API to fetch complete repository metadata for each discovered repository
- **README Collection**: Downloads README files for all repositories with proper encoding handling
- **AI Analysis**: Generates intelligent technical reports using OpenAI models for repository analysis
- **Error Recovery**: Robust error handling that continues processing even when individual repositories fail
- **Structured Logging**: Uses Logfire for advanced logging with structured output for debugging

## Dependencies

- **requests**: HTTP client for both web scraping and GitHub API calls
- **beautifulsoup4**: HTML parsing for GitHub trending page scraping
- **lxml**: Fast XML and HTML parser backend for BeautifulSoup
- **pydantic**: Data validation and serialization (V2)
- **pydantic-settings**: Configuration management via environment variables
- **logfire**: Advanced logging with structured output
- **openai**: OpenAI API client for AI-powered repository analysis

## Project Usage

This application is designed to collect GitHub trending repository data by:

1. **Running the main collector**: `python main.py` - Fetches trending repositories for Python (configurable)
2. **Web scraping**: Scrapes GitHub trending page to discover repository names
3. **API enrichment**: Fetches detailed metadata for each repository via GitHub API
4. **README collection**: Downloads and processes README files with proper encoding
5. **Data export**: Saves structured JSON data with timestamps to `./data/` directory

## Output Structure

The application generates JSON files in the `data/` directory:

- **trending_repos_YYYY-MM-DD_HH:MM:SS.json**: Complete repository data including:
    - Repository metadata (stars, forks, language, topics, timestamps)
    - Owner information (username, avatar, profile URL)
    - Embedded README content with metadata
    - All data in a single structured JSON array

## Configuration Options

- **GitHub Token**: Set `GITHUB_TOKEN` environment variable for higher API rate limits (5000/hour vs 60/hour)
- **Language Filter**: Configure in `main.py` - supports "python", "go", "rust", or None for all languages
- **Time Period**: Configure trending period - "daily", "weekly", or "monthly"
- **Rate Limiting**: Configurable delays and pagination settings via `GitHubAPIConfig`
- **Output Location**: Data is saved to `./data/` directory with automatic directory creation
- **AI Analysis**: Configure OpenAI/Azure OpenAI settings via environment variables for AI-powered repository analysis

# Rule Sheet

## Coding Style

- Follow `ruff` for code style and formatting using `pre-commit` hooks
- Follow PEP 8 naming conventions:
    - snake_case for functions and variables
    - PascalCase for classes
    - UPPER_CASE for constants
- Follow Python 3.10+ features and syntax
- Use Pydantic V2 models, and all Pydantic models must include `Field` with `description`
- Maximum line length of 99 characters
- Use absolute imports over relative imports
- Use `pytest` for testing, and all tests should be placed in the `tests/` directory

### Example

```python
from pydantic import BaseModel, Field


class GitHubRepository(BaseModel):
    """GitHub repository model.

    Attributes:
        name (str): The name of the repository
        stargazers_count (int): Number of stars
    """

    name: str = Field(..., description="The name of the repository")
    stargazers_count: int = Field(..., description="Number of stars")


def fetch_repository_data(repo_name: str) -> GitHubRepository:
    """Fetch repository data from GitHub API.

    Args:
        repo_name (str): Full repository name (owner/repo)

    Returns:
        GitHubRepository: Repository data object
    """
    # Implementation here
    pass
```

## Type Hints

- Use type hints for all function parameters and returns
- Use `typing.Literal` for string enums (e.g., `Literal["daily", "weekly", "monthly"]`)
- Use union types with `|` syntax (Python 3.10+)
- Use `dict[str, Any]` instead of `Dict[str, Any]`

## Documentation

- Use Google-style docstrings for all functions and classes
- All documentation should be in English
- Document all Pydantic model fields with descriptions
- Include type information and examples where helpful

## Dependencies

- Use `uv` for dependency management
- Separate dev dependencies by adding `--dev` flag when adding dependencies
    - Production:
        - Add Dependencies: `uv add <package>`
        - Remove Dependencies: `uv remove <package>`
    - Development:
        - Add Dependencies: `uv add <package> --dev`
        - Remove Dependencies: `uv remove <package> --dev`
- Keep dependencies minimal and up-to-date

## Web Scraping and API Guidelines

- Always respect robots.txt and rate limits
- Use proper User-Agent headers for web scraping
- Implement error handling for both network and parsing errors
- Use GitHub API for detailed data, web scraping only for discovery
- Handle encoding properly when processing README files
- Implement retry logic with exponential backoff for API calls

## Logging and Monitoring

- Use Logfire for structured logging
- Log important events like API calls, rate limit status, and errors
- Include relevant context in log messages (repo names, URLs, etc.)
- Use appropriate log levels (info, warning, error)

## Error Handling

- Use try/except blocks for network operations
- Continue processing other items when individual items fail
- Provide meaningful error messages
- Log errors with sufficient context for debugging
