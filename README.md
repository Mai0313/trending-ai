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

🚀 **A powerful tool to analyze GitHub trending repositories, categorize them by programming language, and collect README files for analysis**

Perfect for researchers, developers, and data scientists who want to stay updated with the latest trending projects across different programming languages.

**Other Languages**: [English](README.md) | [中文](README_cn.md)

## ✨ Features

### 🔍 **GitHub Trending Analysis**

- **Multi-language categorization**: Automatically organize repositories by programming language
- **Comprehensive data collection**: Stars, forks, issues, creation date, and more
- **README harvesting**: Bulk download of README files for content analysis
- **Trending periods**: Support for daily, weekly, and monthly trending data

### � **Data Processing & Export**

- **Structured output**: JSON format for easy integration with other tools
- **Language statistics**: Count, total stars, average stars per language
- **Detailed repository info**: Full metadata for each trending repository
- **Export organization**: Separate files by language and time-stamped outputs

### 🔧 **Developer Experience**

- **GitHub API integration**: Official API usage for reliable data access
- **Rate limiting**: Smart handling of API rate limits with automatic delays
- **Error handling**: Robust error handling for network issues and API limitations
- **Progress tracking**: Real-time progress updates during data collection

### �️ **Technical Features**

- **Type safety**: Full type hints with Pydantic models
- **Configuration**: Flexible configuration for API settings and output preferences
- **Extensible**: Modular design for easy feature additions
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

Run the analyzer to get today's trending repositories:

```bash
python main.py
```

This will:

- ✅ Fetch trending repositories from GitHub
- ✅ Categorize them by programming language
- ✅ Download README files for all repositories
- ✅ Generate detailed analysis reports in the `output/` directory

### Understanding the Output

The program generates several files in the `output/` directory:

1. **trending_summary_YYYYMMDD_HHMMSS.json**: Overall statistics and language breakdown
2. **repositories\_[Language]\_YYYYMMDD_HHMMSS.json**: Detailed repository data for each language
3. **readmes_YYYYMMDD_HHMMSS/**: Directory containing all downloaded README files

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
│   ├── github_client.py   # GitHub API client
│   └── analyzer.py        # Data analysis and processing
├── output/                # Generated reports and data
├── .env.example          # Environment variables template
├── pyproject.toml        # Project configuration
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

To avoid rate limiting, set up a GitHub Personal Access Token:

1. Go to [GitHub Settings > Developer settings > Personal access tokens](https://github.com/settings/tokens)
2. Create a new token (no special permissions needed, just public repo access)
3. Copy `.env.example` to `.env`:
    ```bash
    cp .env.example .env
    ```
4. Add your token:
    ```bash
    GITHUB_TOKEN=ghp_your_token_here
    ```

### API Rate Limits

- **Without token**: 60 requests/hour
- **With token**: 5,000 requests/hour

### Customizing Analysis Parameters

Edit the configuration in `main.py`:

```python
config = GitHubAPIConfig(
    token=github_token,
    per_page=100,  # Repositories per API call
    max_pages=3,  # Maximum pages to fetch
    rate_limit_delay=1.0,  # Delay between requests (seconds)
)
```

## 🎯 What's Included

### Core Components

- **GitHub API Client**: Robust client with rate limiting and error handling
- **Data Models**: Type-safe Pydantic models for all data structures
- **Language Analyzer**: Intelligent categorization and statistical analysis
- **README Collector**: Bulk download and organization of README files
- **Export System**: Multiple output formats for different use cases

### Data Collection Features

- **Trending Repository Detection**: Uses GitHub's search API with smart filters
- **Comprehensive Metadata**: Stars, forks, issues, dates, topics, and more
- **Multi-language Support**: Automatic detection and categorization
- **README Extraction**: Full content extraction with encoding handling
- **Progress Reporting**: Real-time updates during data collection

### Analysis Capabilities

- **Language Statistics**: Repository counts, star distributions, averages
- **Trend Analysis**: Historical data and growth patterns
- **Content Organization**: Structured file organization by language and date
- **Export Flexibility**: JSON, Markdown, and raw text formats

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

## 🔧 Advanced Usage

### Custom Analysis Periods

Modify the time period for trending analysis:

```python
# In main.py, change the 'since' parameter:
trending_data = analyzer.analyze_trending_repositories(since="weekly")  # or "monthly"
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
