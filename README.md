<center>

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

</center>

🚀 **A modern Python tool to analyze GitHub trending repositories with web scraping capabilities, language categorization, and comprehensive README collection**

Perfect for researchers, developers, and data scientists who want to monitor trends and collect repository data for analysis and research purposes.

## ✨ Features

### 🔍 **GitHub Trending Analysis**

- **Web scraping + API**: Combines GitHub trending page scraping with official API for complete data
- **Multi-language support**: Supports Python, Go, Rust, and other languages
- **Time period flexibility**: Daily, weekly, and monthly trending analysis
- **Comprehensive data collection**: Stars, forks, issues, creation dates, topics, and complete metadata

### 📊 **Data Collection & Processing**

- **README harvesting**: Automatic download and processing of README files with proper encoding
- **Structured data models**: Type-safe Pydantic models for all data structures
- **JSON export**: Clean, structured output for easy integration with other tools
- **Error resilience**: Continues processing even when individual repositories fail

### 🤖 **AI-Powered Analysis**

- **OpenAI Integration**: Generate intelligent technical reports for trending repositories
- **Automated Insights**: AI-powered analysis of repository purpose, highlights, and technical details
- **Multi-Provider Support**: Works with OpenAI and Azure OpenAI services
- **Markdown Reports**: Generate professional technical reports in markdown format

### 🔧 **Developer Experience**

- **GitHub API integration**: Official API with intelligent rate limiting and retry logic
- **Logfire logging**: Advanced logging with structured output for debugging
- **Configuration management**: Flexible settings via environment variables
- **Beautiful UI**: BeautifulSoup-powered HTML parsing for trending page scraping

### 🏗️ **Technical Architecture**

- **Modern Python**: Uses Python 3.10+ features with full type hints
- **Pydantic V2**: Latest data validation and serialization
- **Session management**: Persistent HTTP sessions with proper headers
- **Rate limit handling**: Smart delays and monitoring of GitHub API limits
- **Modular design**: Clean separation between client, models, analysis, and business logic
- **AI Analysis Engine**: OpenAI-powered repository analysis and report generation
- **Documentation**: Comprehensive code documentation and usage examples
- **Release automation**: Semantic versioning and release drafting
- **Auto-labeling**: Intelligent PR categorization

### 📚 **Documentation**

- **MkDocs Material**: Beautiful, responsive documentation
- **Auto-generation**: Scripts to generate docs from code and notebooks
- **API documentation**: Automatic API reference generation
- **Blog support**: Built-in blog functionality for project updates

### 🤖 **Automation Scripts**

- **Project initialization**: `scripts/initpyrepo.go` for creating personalized projects
- **Documentation generation**: `scripts/gen_docs.py` for auto-generating documentation
- **Makefile commands**: Common development tasks automated

## 🚀 Quick Start

### Prerequisites

- Python 3.10+ installed
- Git installed
- Internet connection for GitHub API access

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Mai0313/trending_ai.git
    cd trending_ai
    ```

2. Install dependencies:

    ```bash
    uv sync  # or pip install -r requirements.txt if you don't have uv
    ```

3. (Optional) Set up GitHub Token for higher API limits:

    ```bash
    cp .env.example .env
    # Edit .env and add your GitHub token:
    # GITHUB_TOKEN=your_github_token_here
    ```

### Basic Usage

Run the analyzer to get trending repositories for a specific language:

```bash
python main.py
```

This will:

- ✅ Scrape GitHub trending page for repository names
- ✅ Fetch detailed information via GitHub API
- ✅ Download README files with proper encoding handling
- ✅ Save structured data to `./data/` directory with timestamps

### Configuration Options

You can customize the analysis by modifying the client parameters in `main.py`:

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

### Understanding the Output

The program generates files in the `./data/` directory:

- **trending_repos_YYYY-MM-DD_HH:MM:SS.json**: Complete repository data with README content

Each repository entry includes:

- Basic info: name, description, URL, stars, forks
- Owner details: username, avatar, profile URL
- Timestamps: created, updated, last pushed
- Topics and programming language
- Complete README content with metadata

### Example Output

```bash
🚀 TrendingAI - GitHub Trending Repositories Analyzer
============================================================
📊 Analyzing trending repositories...
Fetched page 1, got 100 repositories
Total repositories fetched: 300

============================================================
TRENDING REPOSITORIES SUMMARY
============================================================
Fetched at: 2025-07-18 12:43:55
Total repositories: 300
Programming languages: 15

Language             Count      Total Stars     Avg Stars
------------------------------------------------------------
Python               45         4500            100.0
JavaScript           38         3040            80.0
TypeScript           25         3750            150.0
Go                   20         2400            120.0
Rust                 15         2250            150.0

✅ Analysis complete!
📁 Results saved in the 'output' directory
📊 Total repositories analyzed: 300
📚 README files downloaded: 285
🌐 Programming languages found: 15
```

## 📁 Project Structure

```
trending_ai/
├── main.py                 # Main entry point
├── src/trending_ai/        # Core package
│   ├── __init__.py
│   ├── models.py          # Pydantic data models
│   ├── client.py          # GitHub API client with web scraping
│   └── analysis.py        # AI-powered repository analysis
├── data/                  # Generated JSON data files
├── .env.example          # Environment variables template
├── pyproject.toml        # Project configuration with uv
├── Makefile             # Development commands
└── README.md
```

## 🛠️ Available Commands

```bash
# Run the main analyzer
python main.py              # Analyze today's trending repositories

# Development
make clean                   # Clean autogenerated files
make format                  # Run pre-commit hooks
make test                   # Run all tests
make gen-docs               # Generate documentation

# Dependencies
uv add <package>            # Add production dependency
uv add <package> --dev      # Add development dependency
uv sync                     # Install all dependencies
```

## ⚙️ Configuration

### GitHub Token Setup (Recommended)

To avoid rate limiting and access private repositories, set up a GitHub Personal Access Token:

1. Go to [GitHub Settings > Developer settings > Personal access tokens](https://github.com/settings/tokens)
2. Create a new token with public repository access
3. Set the token as an environment variable:
    ```bash
    export GITHUB_TOKEN=ghp_your_token_here
    ```
    Or create a `.env` file:
    ```bash
    echo "GITHUB_TOKEN=ghp_your_token_here" > .env
    ```

### API Rate Limits

- **Without token**: 60 requests/hour
- **With token**: 5,000 requests/hour

### Customizing Collection Parameters

Edit the configuration in `main.py`:

```python
from src.trending_ai.client import GitHubAPIClient

# Initialize client with custom settings
client = GitHubAPIClient(
    api_key="your_token_here",  # Or set GITHUB_TOKEN env var
    per_page=100,  # Repositories per API call
    max_pages=10,  # Maximum pages to fetch
    rate_limit_delay=1.0,  # Delay between requests (seconds)
)

# Get trending repositories
repos = client.get_trendings(
    language="python",  # "python", "go", "rust", or None for all
    since="daily",  # "daily", "weekly", or "monthly"
    limit=50,  # Optional: limit number of repositories
)
```

## 🎯 What's Included

### Core Components

- **GitHub Trending Scraper**: Scrapes GitHub trending page using BeautifulSoup
- **GitHub API Client**: Fetches detailed repository information via official API
- **AI Analysis Engine**: OpenAI-powered analysis for generating technical reports
- **Data Models**: Type-safe Pydantic models for repositories, users, and README data
- **README Collector**: Downloads and processes README files with encoding detection
- **JSON Export**: Structured data export with timestamps

### Data Collection Features

- **Hybrid Approach**: Combines web scraping (for trending discovery) with API (for detailed data)
- **Comprehensive Metadata**: Stars, forks, issues, dates, topics, owner info, and more
- **Multi-language Support**: Filter by specific programming languages or collect all
- **README Extraction**: Full content extraction with Base64 decoding and encoding handling
- **AI Analysis**: Generate intelligent technical reports about repository purpose and highlights
- **Progress Logging**: Structured logging with Logfire for debugging and monitoring

### Technical Capabilities

- **Rate Limit Management**: Intelligent handling of GitHub API rate limits with delays
- **Error Recovery**: Continues processing even when individual repositories fail
- **Session Management**: Persistent HTTP sessions with proper headers and user agents
- **Configuration Management**: Environment variable support via pydantic-settings
- **Type Safety**: Full type annotations and Pydantic validation throughout

### Development Tools

- **uv**: Fast Python dependency management
- **ruff**: Lightning-fast Python linter and formatter
- **pytest**: Comprehensive testing framework
- **pre-commit**: Git hooks for code quality
- **Pydantic**: Data validation and serialization
- **Type hints**: Full type annotation support

### Use Cases

- **Research**: Academic research on programming language trends
- **Market Analysis**: Understanding popular technologies and frameworks
- **Developer Insights**: Staying updated with emerging projects
- **Content Creation**: Blog posts and articles about trending technologies
- **Portfolio Inspiration**: Discovering interesting projects to learn from
- **AI-Powered Reports**: Generate intelligent technical analysis reports for trending repositories

## 🔧 Advanced Usage

### AI Analysis Integration

Generate intelligent technical reports for repositories:

```python
from src.trending_ai.analysis import TrendingAnalysis
from src.trending_ai.client import GitHubAPIClient

# Set up OpenAI configuration
analyzer = TrendingAnalysis(
    base_url="https://api.openai.com/v1",  # or Azure endpoint
    api_key="your_openai_api_key",
    model="gpt-4",  # or your preferred model
)

# Get repositories and analyze
client = GitHubAPIClient()
repos = client.get_trendings(language="python", since="daily")

for repo in repos:
    technical_report = analyzer.get_analysis(repo)
    print(f"Analysis for {repo.full_name}:\n{technical_report}")
```

### Environment Variables for AI Analysis

```bash
# OpenAI Configuration
export OPENAI_API_TYPE="openai"  # or "azure"
export OPENAI_BASE_URL="https://api.openai.com/v1"
export OPENAI_API_KEY="sk-proj-..."

# For Azure OpenAI
export OPENAI_API_TYPE="azure"
export AZURE_OPENAI_ENDPOINT="https://your-resource.openai.azure.com"
export AZURE_OPENAI_API_KEY="your_azure_key"
export OPENAI_API_VERSION="2024-02-01"
```

### Custom Analysis Periods

Modify the time period for trending analysis:

```python
# In main.py, change the 'since' parameter:
repos = client.get_trendings(since="weekly")  # or "monthly"
```

### Language-Specific Analysis

Focus on specific programming languages:

```python
# Add language filtering in github_client.py
repositories = self.github_client.get_trendings(language="Python", since="daily")
```

### Batch Processing

For large-scale analysis, implement batch processing:

```python
languages = ["Python", "JavaScript", "TypeScript", "Go", "Rust"]
for lang in languages:
    repos = client.get_trendings(language=lang)
    # Process each language separately
```

## 🚨 Error Handling & Troubleshooting

### Common Issues

1. **Rate Limit Exceeded**

    - Solution: Add GitHub token or increase delay between requests
    - Error: `403 Forbidden` or `X-RateLimit-Remaining: 0`

2. **Network Timeouts**

    - Solution: Check internet connection and GitHub API status
    - Error: `ConnectionError` or `TimeoutError`

3. **Missing README Files**

    - Normal behavior: Not all repositories have README files
    - Info: Check console output for "No README found" messages

4. **Encoding Issues**

    - Solution: Program handles multiple encodings automatically
    - Info: UTF-8 is used as fallback encoding

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Ways to Contribute

- 🐛 **Report bugs**: Open an issue with detailed reproduction steps
- 💡 **Suggest features**: Propose new analysis capabilities or improvements
- 📖 **Improve documentation**: Help make the docs clearer and more comprehensive
- 🔧 **Submit code**: Fix bugs or implement new features via pull requests

### Development Setup

1. Fork the repository
2. Clone your fork:
    ```bash
    git clone https://github.com/your-username/trending_ai.git
    ```
3. Install development dependencies:
    ```bash
    uv sync --dev
    ```
4. Set up pre-commit hooks:
    ```bash
    make format
    ```

### Pull Request Guidelines

- Follow the existing code style (enforced by ruff)
- Add tests for new functionality
- Update documentation as needed
- Ensure all tests pass before submitting

## 📖 Documentation

For detailed API documentation and advanced usage examples, visit: [https://mai0313.github.io/trending_ai/](https://mai0313.github.io/trending_ai/)

## 👥 Contributors

[![Contributors](https://contrib.rocks/image?repo=Mai0313/trending_ai)](https://github.com/Mai0313/trending_ai/graphs/contributors)

Made with [contrib.rocks](https://contrib.rocks)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**🌟 If you find TrendingAI useful, please consider giving it a star on GitHub!**
