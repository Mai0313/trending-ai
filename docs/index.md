# TrendingAI - GitHub Trending Repositories Analyzer

[![python](https://img.shields.io/badge/-Python_3.10_%7C_3.11_%7C_3.12-blue?logo=python&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![uv](https://img.shields.io/badge/-uv_dependency_management-2C5F2D?logo=python&logoColor=white)](https://docs.astral.sh/uv/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![tests](https://github.com/Mai0313/trending_ai/actions/workflows/test.yml/badge.svg)](https://github.com/Mai0313/trending_ai/actions/workflows/test.yml)
[![code-quality](https://github.com/Mai0313/trending_ai/actions/workflows/code-quality-check.yml/badge.svg)](https://github.com/Mai0313/trending_ai/actions/workflows/code-quality-check.yml)
[![codecov](https://codecov.io/gh/Mai0313/trending_ai/branch/master/graph/badge.svg)](https://codecov.io/gh/Mai0313/trending_ai)
[![license](https://img.shields.io/badge/License-MIT-green.svg?labelColor=gray)](https://github.com/Mai0313/trending_ai/tree/master?tab=License-1-ov-file)
[![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/Mai0313/trending_ai/pulls)
[![contributors](https://img.shields.io/github/contributors/Mai0313/trending_ai.svg)](https://github.com/Mai0313/trending_ai/graphs/contributors)

🚀 **A modern Python tool to analyze GitHub trending repositories with web scraping capabilities, language categorization, and comprehensive README collection**

Perfect for researchers, developers, and data scientists who want to monitor trends and collect repository data for analysis and research purposes.

## Why Use TrendingAI?

TrendingAI combines the best of both worlds: web scraping for trend discovery and official GitHub API for comprehensive data collection. This hybrid approach ensures you get complete and accurate information about trending repositories.

- **Comprehensive Data Collection**: Get complete repository metadata, README files, and owner information
- **Modern Python Stack**: Built with Python 3.10+, Pydantic V2, and modern best practices
- **Production Ready**: Includes rate limiting, error handling, and structured logging
- **Easy Integration**: Clean JSON output for seamless integration with other tools

## 🎯 Key Features

### **Hybrid Data Collection**

- **GitHub Trending Scraping**: Uses BeautifulSoup to scrape GitHub's trending page for repository discovery
- **GitHub API Integration**: Fetches detailed repository information via official API
- **README Collection**: Downloads and processes README files with proper encoding detection
- **Multi-language Support**: Filter by specific programming languages or collect all

### **Modern Development Stack**

- **Python 3.10+** with modern syntax and type hints
- **Pydantic V2** for data validation and serialization
- **requests** for HTTP client with session management
- **BeautifulSoup4** with lxml parser for fast HTML parsing
- **logfire** for structured logging and monitoring

### **Production-Ready Features**

- **Rate Limit Handling**: Intelligent management of GitHub API rate limits
- **Error Recovery**: Continues processing even when individual repositories fail
- **Configuration Management**: Environment variable support via pydantic-settings
- **Structured Output**: Clean JSON export with timestamps for easy analysis
- **Makefile commands** for common development tasks

## 🚀 Getting Started

### Quick Setup

=== "Basic Installation"

    ```bash
    # Clone the repository
    git clone https://github.com/Mai0313/trending_ai.git
    cd trending_ai

    # Install dependencies with uv
    uv sync

    # Set up GitHub token (optional but recommended)
    export GITHUB_TOKEN=your_github_token_here
    ```

=== "Development Setup"

    ```bash
    # Clone and setup for development
    git clone https://github.com/Mai0313/trending_ai.git
    cd trending_ai

    # Install with dev dependencies
    uv sync --dev

    # Set up pre-commit hooks
    make format

    # Run tests
    make test
    ```

=== "Docker Setup"

    ```bash
    # Using Docker Compose
    docker-compose up --build

    # Or using the Dockerfile directly
    docker build -t trending-ai .
    docker run -e GITHUB_TOKEN=your_token trending-ai
    ```

### Basic Usage

```bash
# Run the analyzer to get trending Python repositories
python main.py

# Output will be saved to ./data/ directory
# Example: trending_repos_2024-07-18_12:30:45.json
```

### Configuration

Customize the analysis by modifying `main.py`:

```python
from src.trending_ai.client import GitHubAPIClient


def main():
    client = GitHubAPIClient()
    repos = client.get_trendings(
        language="python",  # Options: "python", "go", "rust", None
        since="daily",  # Options: "daily", "weekly", "monthly"
        limit=50,  # Optional: limit number of repos
    )
```

## 📁 Project Structure

```
trending_ai/
├── main.py                 # Main entry point
├── src/trending_ai/        # Core package
│   ├── __init__.py
│   ├── models.py          # Pydantic data models
│   └── client.py          # GitHub API client with web scraping
├── data/                  # Generated JSON data files
├── docs/                  # MkDocs documentation
├── scripts/               # Utility scripts
├── pyproject.toml         # Project configuration with uv
├── Makefile              # Development commands
└── README.md
```

## 🔧 Core Components

### Data Models

TrendingAI uses Pydantic V2 for type-safe data structures:

```python
class GitHubRepository(BaseModel):
    """Complete repository information including README content."""

    id: int
    name: str
    full_name: str
    description: str | None
    html_url: str
    language: str | None
    stargazers_count: int
    forks_count: int
    # ... and many more fields
    readme: ReadmeData | None  # Embedded README content
```

### GitHub API Client

The `GitHubAPIClient` combines web scraping and API calls:

- **Trending Discovery**: Scrapes GitHub trending page with BeautifulSoup
- **Data Enrichment**: Fetches detailed information via GitHub API
- **Rate Limiting**: Intelligent handling of API limits
- **Error Recovery**: Continues processing even when individual requests fail

### Output Format

Generated JSON files include complete repository data:

```json
{
  "id": 123456789,
  "name": "awesome-python-project",
  "full_name": "user/awesome-python-project",
  "description": "An amazing Python project",
  "language": "Python",
  "stargazers_count": 1234,
  "readme": {
    "content": "# Awesome Python Project\n\nThis is...",
    "encoding": "utf-8",
    "size": 2048,
    "fetched_at": "2024-07-18_12:30:45"
  }
}
```

## 🛠️ Development

### Available Commands

```bash
# Run the main analyzer
python main.py

# Development commands
make clean                   # Clean autogenerated files
make format                  # Run pre-commit hooks
make test                   # Run all tests
make gen-docs               # Generate documentation

# Dependency management
uv add <package>            # Add production dependency
uv add <package> --dev      # Add development dependency
uv sync                     # Install all dependencies
```

### Testing

```bash
# Run tests with coverage
make test

# Run specific test files
pytest tests/test_client.py

# Run with verbose output
pytest -v
```

## ⚙️ Configuration

### GitHub Token Setup

For higher API rate limits (5000/hour vs 60/hour):

```bash
# Set as environment variable
export GITHUB_TOKEN=ghp_your_token_here

# Or create .env file
echo "GITHUB_TOKEN=ghp_your_token_here" > .env
```

### Client Configuration

Customize the GitHub API client:

```python
client = GitHubAPIClient(
    api_key="your_token",  # GitHub token
    per_page=100,  # Items per API call
    max_pages=10,  # Maximum pages to fetch
    rate_limit_delay=1.0,  # Delay between requests
)
```

## � Use Cases

- **Research**: Academic research on programming language trends
- **Market Analysis**: Understanding popular technologies and frameworks
- **Developer Insights**: Staying updated with emerging projects
- **Content Creation**: Blog posts about trending technologies
- **Portfolio Inspiration**: Discovering interesting projects to learn from

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. Fork the repository
2. Create a feature branch
3. Make your changes with tests
4. Run `make format` and `make test`
5. Submit a pull request

See our [Contributing Guide](contributing/) for more details.

## 📚 API Reference

For detailed API documentation, visit: [https://mai0313.github.io/trending_ai/](https://mai0313.github.io/trending_ai/)

## 👥 Contributors

[![Contributors](https://contrib.rocks/image?repo=Mai0313/trending_ai)](https://github.com/Mai0313/trending_ai/graphs/contributors)

---

**🌟 Ready to analyze GitHub trends?** Start by running `python main.py` and explore the trending repositories! 🚀
