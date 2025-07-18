<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

⚠️ **IMPORTANT**: After making any code changes, adding features, or updating functionality, you MUST update .github/copilot-instructions.md to reflect the current project state and capabilities.

# Project Background

This is TrendingAI, a Python application designed to analyze GitHub trending repositories. The tool fetches trending repositories using GitHub's API, categorizes them by programming language, downloads their README files, and generates comprehensive analysis reports. It's perfect for researchers, developers, and data scientists who want to stay updated with the latest trending projects across different programming languages.

# Project Structure / Features

## Core Application Features

- **GitHub API Integration**: Uses GitHub's official API to fetch trending repositories with proper rate limiting and error handling
- **Language Categorization**: Automatically organizes repositories by programming language
- **README Collection**: Downloads and stores README files from all trending repositories
- **Data Export**: Generates structured JSON reports and organized file outputs
- **Progress Tracking**: Real-time console output showing analysis progress

## Architecture Components

- **Main Entry Point**: `main.py` - Primary script to run the complete analysis
- **Core Package**: `src/trending_ai/` - Contains all application logic
    - `models.py` - Pydantic data models for type-safe data structures
    - `github_client.py` - GitHub API client with rate limiting
    - `analyzer.py` - Data processing and analysis logic
- **Output Directory**: `output/` - Generated reports and README files
- **Configuration**: `.env` file support for GitHub token and other settings

## Data Models (Pydantic)

- **GitHubUser**: User/organization information
- **GitHubRepository**: Complete repository metadata (stars, forks, language, etc.)
- **LanguageStats**: Statistics aggregated by programming language
- **TrendingData**: Complete analysis results container
- **ReadmeData**: README file content and metadata

## Key Capabilities

- **Trending Analysis**: Fetches repositories with recent activity and high engagement
- **Multi-language Support**: Processes repositories across all programming languages
- **Statistical Analysis**: Calculates totals, averages, and distributions by language
- **File Organization**: Saves data in organized directory structure with timestamps
- **Error Recovery**: Continues processing even when individual repositories fail

## Dependencies

- **requests**: HTTP client for GitHub API calls
- **pydantic**: Data validation and serialization
- **pydantic-settings**: Configuration management

## Project Usage

This application is designed to analyze GitHub trending repositories by:

1. **Running the main analyzer**: `python main.py` - Fetches today's trending repositories
2. **Categorizing by language**: Automatically groups repositories by programming language
3. **Collecting README files**: Downloads README content for analysis and research
4. **Generating reports**: Creates timestamped JSON reports and organized file outputs

## Output Structure

The application generates several types of output files:

- **trending_summary_YYYYMMDD_HHMMSS.json**: Overall statistics and language breakdown
- **repositories\_[Language]\_YYYYMMDD_HHMMSS.json**: Detailed repository data per language
- **readmes_YYYYMMDD_HHMMSS/**: Directory containing all downloaded README files

## Configuration Options

- **GitHub Token**: Set `GITHUB_TOKEN` environment variable for higher API rate limits
- **API Parameters**: Modify `GitHubAPIConfig` in main.py for custom behavior
- **Output Directory**: Default is `output/` but can be customized
- **Time Periods**: Support for daily, weekly, and monthly trending analysis

# Rule Sheet

<!-- This section outlines the coding standards, practices, and guidelines to follow when contributing to this project. It ensures consistency, maintainability, and quality across the codebase. -->

<!-- Example -->

<!-- ## Coding Style

- Follow `ruff-check` and `ruff-format` for code style and formatting using `pre-commit` hooks.
- Follow PEP 8 naming conventions:
    - snake_case for functions and variables
    - PascalCase for classes
    - UPPER_CASE for constants
- Follow the Python version specified in the `pyproject.toml` or `.python-version` file.
- Use pydantic model, and all pydantic models should include `Field`, and `description` should be included.
- Maximum line length of 99 characters
- Use absolute imports over relative imports
- Use `pytest` for testing, and all tests should be placed in the `tests/` directory

### Example

```python
from pydantic import BaseModel, Field


class User(BaseModel):
    """Example User model.

    Attributes:
        name (str): The name of the user
    """

    name: str = Field(..., description="The name of the user")


def foo(self, extra_input: str) -> str:
    """Example function.

    Args:
        extra_input (str): Extra input for the function

    Returns:
        str: Result of the function
    """
    return f"Hello, {self.name} and {extra_input}"
```

## Type Hints

- Use type hints for all function parameters and returns
- Use `TypeVar` for generic types
- Use `Protocol` for duck typing

## Documentation

- Use Google-style docstrings
- All documentation should be in English
- Use proper inline comments for better mkdocs support
- Document environment setup

## Dependencies

- Use `uv` for dependency management
- Separate dev dependencies by adding `--dev` flag when adding dependencies
    - Production:
        - Add Dependencies: `uv add <package>`
        - Remove Dependencies: `uv remove <package>`
    - Development:
        - Add Dependencies: `uv add <package> --dev`
        - Remove Dependencies: `uv remove <package> --dev`
- Regularly update dependencies -->
