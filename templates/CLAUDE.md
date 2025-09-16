# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

## Project Overview

[Brief description of what your tool does and its primary use cases]

## Development Commands

```bash
# Install dependencies
uv sync

# Add test dependencies
uv add --optional test pytest pytest-cov pytest-mock

# Primary CLI usage (development)
uv run python -m your_tool_name.main [command] [options]

# System-wide tool (if installation succeeds)
uv tool install --editable .
your-tool-name [command] [options]

# Run tests
uv run python -m pytest tests/ -v

# Linting and formatting
uv run ruff check .
uv run black .
uv run mypy .
```

## Documentation

- [doc/ARCHITECTURE.md](doc/ARCHITECTURE.md) - System architecture (REQUIRED)
- [tests/README.md](tests/README.md) - Test suite documentation

## Architecture Notes

### Core Modules

- **`core/`** - [Core functionality description]
- **`utils/`** - [Utility functions description]
- **`tests/`** - [Test suite description]

### Key Features

- [List key features and design principles]

## Coding Standards

- Python 3.10+ required
- 4-space indentation
- Type hints required for public functions
- Use pathlib.Path for file operations
- Prefer logging over print (except CLI output in main.py)
- UV-exclusive workflow (no direct python/pip usage)

## Testing Guidelines

- Framework: pytest
- Test files: `test_*.py` in `tests/` directory
- Test functions: `test_*`
- Run tests: `uv run pytest tests/`
- Coverage target: 80%+ for core modules