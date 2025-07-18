# Python Project Template

[![python](https://img.shields.io/badge/-Python_3.10_%7C_3.11_%7C_3.12-blue?logo=python&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![uv](https://img.shields.io/badge/-uv_dependency_management-2C5F2D?logo=python&logoColor=white)](https://docs.astral.sh/uv/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![tests](https://github.com/Mai0313/trending_ai/actions/workflows/test.yml/badge.svg)](https://github.com/Mai0313/trending_ai/actions/workflows/test.yml)
[![code-quality](https://github.com/Mai0313/trending_ai/actions/workflows/code-quality-check.yml/badge.svg)](https://github.com/Mai0313/trending_ai/actions/workflows/code-quality-check.yml)
[![codecov](https://codecov.io/gh/Mai0313/trending_ai/branch/master/graph/badge.svg)](https://codecov.io/gh/Mai0313/trending_ai)
[![license](https://img.shields.io/badge/License-MIT-green.svg?labelColor=gray)](https://github.com/Mai0313/trending_ai/tree/master?tab=License-1-ov-file)
[![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/Mai0313/trending_ai/pulls)
[![contributors](https://img.shields.io/github/contributors/Mai0313/trending_ai.svg)](https://github.com/Mai0313/trending_ai/graphs/contributors)

🚀 **A comprehensive Python project template designed to help developers quickly bootstrap new projects with complete CI/CD pipelines, modern tooling, and best practices.**

The template includes everything needed to start a professional Python project without spending time on infrastructure setup.

**Other Languages**: [English](https://github.com/Mai0313/trending_ai/blob/master/README.md) | [中文](https://github.com/Mai0313/trending_ai/blob/master/README_cn.md)

## Why Use This Template?

This template eliminates the time-consuming setup of project infrastructure, allowing you to focus on building your application. It provides:

- **Zero-configuration CI/CD**: Complete GitHub Actions workflows out of the box
- **Modern Python tooling**: Latest best practices with uv, ruff, and pytest
- **Professional development environment**: VS Code Dev Container with optimized terminal setup
- **Comprehensive documentation**: Auto-generated docs with MkDocs Material
- **Quality assurance**: Pre-commit hooks, testing, and coverage reporting

## 🎯 Key Features

### **Modern Development Stack**

- **Python 3.10, 3.11, 3.12** support with uv dependency management
- **Ruff** for ultra-fast linting and formatting
- **pytest** with coverage reporting and parallel execution
- **Pre-commit hooks** for automated code quality checks

### **Complete CI/CD Pipeline**

- **Automated testing** across multiple Python versions
- **Code quality gates** with ruff validation
- **GitHub Pages deployment** for documentation
- **Release automation** with semantic versioning
- **Auto-labeling** for pull requests

### **Production-Ready Infrastructure**

- **Docker support** with multi-stage builds
- **VS Code Dev Container** with zsh, oh-my-zsh, and powerlevel10k
- **MkDocs documentation** with Material theme
- **Makefile commands** for common development tasks

### **Intelligent Automation**

- **Project initialization script** (`scripts/initpyrepo.go`) for personalized setup
- **Documentation generation** (`scripts/gen_docs.py`) from code and notebooks
- **Auto-generated API docs** from Python code
- **Blog functionality** for project updates

## 🚀 Getting Started

### Quick Setup Options

=== "GitHub Template"

    1. Click [**Use this template**](https://github.com/Mai0313/trending_ai/generate)
    2. Configure your new repository
    3. Clone and start developing

=== "Initialization Script"

    ```bash
    # Clone the template
    git clone https://github.com/Mai0313/trending_ai.git
    cd trending_ai

    # Run the initialization script
    go run scripts/initpyrepo.go

    # Follow the prompts to customize your project
    ```

=== "Manual Setup"

    ```bash
    # Clone the repository
    git clone https://github.com/Mai0313/trending_ai.git
    cd trending_ai

    # Install uv if not already installed
    make uv-install

    # Install dependencies
    uv sync

    # Set up pre-commit hooks
    make format
    ```

=== "Quick Customization"

    ```bash
    # Clone the repository
    git clone https://github.com/Mai0313/trending_ai.git
    cd trending_ai

    # Replace with your project name (snake_case)
    find . -type f -name "*.py" -o -name "*.md" -o -name "*.toml" | xargs sed -i 's/trending_ai/your_project_name/g'

    # Replace with your project title (PascalCase)
    find . -type f -name "*.py" -o -name "*.md" -o -name "*.toml" | xargs sed -i 's/TrendingAI/YourProjectTitle/g'

    # Install and setup
    make uv-install && uv sync && make format
    ```

### Development Workflow

```bash
# Run tests
make test

# Format code
make format

# Generate documentation
make gen-docs

# Clean artifacts
make clean
```

## 📁 Project Structure

The template follows Python packaging best practices with a clean, organized structure:

```
├── .devcontainer/          # VS Code Dev Container setup
│   ├── Dockerfile         # Development environment
│   └── devcontainer.json  # VS Code configuration
├── .github/
│   ├── workflows/         # CI/CD pipelines
│   │   ├── test.yml      # Multi-version testing
│   │   ├── code-quality-check.yml
│   │   ├── deploy.yml    # Documentation deployment
│   │   └── release_drafter.yml
│   └── copilot-instructions.md
├── docker/
│   ├── Dockerfile        # Production container
│   └── docker-compose.yaml
├── docs/                 # MkDocs documentation
│   ├── index.md
│   ├── installation/
│   └── blog/
├── scripts/              # Automation tools
│   ├── initpyrepo.go    # Project initialization
│   └── gen_docs.py      # Documentation generation
├── src/
│   └── trending_ai/   # Main package
├── tests/               # Test suite
├── pyproject.toml       # Project configuration
├── .pre-commit-config.yaml
├── Makefile            # Development commands
└── README.md
```

## 🔧 Configuration Files

The template includes comprehensive configuration for:

- **`pyproject.toml`**: Project metadata, dependencies, and tool configurations
- **`.pre-commit-config.yaml`**: Code quality hooks with ruff
- **`pytest` configuration**: Testing, coverage, and reporting setup
- **`mkdocs.yml`**: Documentation generation and deployment
- **Docker configurations**: Development and production containers

## 🎨 Customization

### Project Name Customization

This template is designed for quick customization through simple global replacements:

1. **Replace package name**: Change all instances of `trending_ai` to your project name (recommended: snake_case)
2. **Replace project title**: Change all instances of `TrendingAI` to your project title (recommended: PascalCase)
3. **Update metadata**: Modify author, description, and other details in `pyproject.toml`

**Example commands:**

```bash
# If your project is called "awesome_project"
find . -type f -name "*.py" -o -name "*.md" -o -name "*.toml" | xargs sed -i 's/trending_ai/awesome_project/g'
find . -type f -name "*.py" -o -name "*.md" -o -name "*.toml" | xargs sed -i 's/TrendingAI/AwesomeProject/g'
```

### Dependency Management

```bash
# Add production dependencies
uv add requests pydantic

# Add development dependencies
uv add pytest black --dev

# Update all dependencies
uv sync
```

### Documentation

The template uses MkDocs with Material theme and supports:

- **Auto-generated API docs** from Python docstrings
- **Jupyter notebook integration** with automatic conversion
- **Blog functionality** for project updates
- **Custom themes** and styling

### CI/CD Customization

All workflows are modular and can be customized:

- **Testing matrix**: Modify Python versions in `.github/workflows/test.yml`
- **Code quality**: Adjust ruff rules in `pyproject.toml`
- **Documentation**: Configure MkDocs deployment in `.github/workflows/deploy.yml`
- **Release process**: Customize release drafting and versioning

## 🏢 Enterprise Features

### Security & Compliance

- **Dependency scanning** with automated updates
- **Security linting** with bandit integration
- **License compliance** tracking
- **Secrets management** best practices

### Team Development

- **Standardized development environment** with Dev Containers
- **Code review automation** with quality gates
- **Consistent coding standards** enforced by pre-commit hooks
- **Documentation requirements** for all public APIs

## 🌟 Success Stories

This template has been used to bootstrap:

- **Machine Learning projects** with GPU support
- **Web APIs** with FastAPI and async support
- **Data processing pipelines** with scientific computing stack
- **CLI tools** with modern Python packaging

## 📚 Learn More

- [Installation Guide](installation/index.md) - Detailed setup instructions
- [Development Workflow](workflows/) - Best practices for development
- [CI/CD Configuration](cicd/) - Understanding the automation
- [Customization Guide](customization/) - Adapting for your needs

## 🤝 Contributing

We welcome contributions! Whether it's:

- 🐛 **Bug reports** and fixes
- ✨ **Feature requests** and implementations
- 📝 **Documentation** improvements
- 🎨 **Template enhancements**

See our [Contributing Guide](contributing/) for details.

## 👥 Contributors

[![Contributors](https://contrib.rocks/image?repo=Mai0313/trending_ai)](https://github.com/Mai0313/trending_ai/graphs/contributors)

Made with [contrib.rocks](https://contrib.rocks)

---

**Ready to start your next Python project?** [Use this template](https://github.com/Mai0313/trending_ai/generate) and focus on building amazing applications! 🚀
