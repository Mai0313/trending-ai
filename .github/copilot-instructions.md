<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

⚠️ **IMPORTANT**: After making any code changes, adding features, or updating functionality, you MUST update .github/copilot-instructions.md to reflect the current project state and capabilities.

# Project Background

<!-- This section provides context about the project, its purpose, and any relevant background information -->

<!-- Example -->

<!-- This is a comprehensive Python project template designed to help developers quickly bootstrap new projects with complete CI/CD pipelines, modern tooling, and best practices. The template includes everything needed to start a professional Python project without spending time on infrastructure setup. -->

# Project Structure / Features

<!-- This section outlines the key features and structure of the project, including directories, files, and their purposes -->

<!-- Example -->

<!-- ## Core Infrastructure

- **Modern Python**: Supports Python 3.10, 3.11, and 3.12
- **Dependency Management**: Uses `uv` for fast and reliable dependency management
- **Project Structure**: src/ layout following Python packaging best practices
- **Docker Support**: Multi-stage Dockerfile for development and production
- **VS Code Dev Container**: Fully configured development environment with zsh, oh-my-zsh, and powerlevel10k

## Code Quality & Testing

- **Pre-commit Hooks**: Automated code formatting and linting with ruff
- **Testing Framework**: pytest with coverage reporting, parallel execution, and detailed reporting
- **Code Coverage**: Comprehensive coverage tracking with HTML and XML reports
- **Type Checking**: Full type hint support and validation

## CI/CD Pipeline

- **Automated Testing**: Multi-version Python testing on pull requests
- **Code Quality Checks**: Automated ruff checks and pre-commit validation
- **Documentation Deployment**: Automatic GitHub Pages deployment for MkDocs
- **Release Management**: Automated release drafting and semantic versioning
- **Auto-labeling**: Intelligent PR labeling based on changes

## Documentation

- **MkDocs**: Material theme with automatic API documentation generation
- **Auto-generated Docs**: Scripts to generate documentation from Python code and Jupyter notebooks
- **Blog Support**: Built-in blog functionality for project updates

## Automation Scripts

- **Project Initialization**: Go script (`scripts/initpyrepo.go`) for creating new projects from template
- **Documentation Generation**: Python script (`scripts/gen_docs.py`) for auto-generating docs from code

## Project Usage

This template is designed to be cloned and customized for new Python projects. Developers can use the initialization script to create new projects with personalized configurations while maintaining all the CI/CD and tooling benefits.

## Template Customization Strategy

When users clone this project, they can quickly customize it by performing global replacements:

- **Replace `trending_ai`** → Replace with their actual project name (snake_case format)
- **Replace `TrendingAI`** → Replace with their project title (PascalCase format)

This allows users to instantly personalize the entire project structure, package names, imports, and documentation while keeping all the CI/CD infrastructure intact. -->

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
