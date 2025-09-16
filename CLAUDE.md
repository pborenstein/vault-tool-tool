# CLAUDE.md

This file provides guidance to Claude Code when working with the vault-tool-tool repository.

## Project Overview

This repository provides a standardized framework for building CLI tools that process Obsidian vaults and markdown collections. It includes setup guides, templates, and common patterns for vault tool development.

## Repository Structure

- `VAULT_TOOL_SETUP.md` - Comprehensive setup guide and framework documentation
- `templates/` - Reusable boilerplate files for new projects
- `gitignore` - Standard .gitignore template for vault tools

## Development Commands

```bash
# Navigate to templates directory
cd templates

# Copy templates to new project
cp pyproject.toml /path/to/new-project/
cp CLAUDE.md /path/to/new-project/
cp main.py /path/to/new-project/your_tool_name/
```

## Framework Usage Pattern

When helping users create new vault tools:

1. **Reference the setup guide**: Always start with `VAULT_TOOL_SETUP.md`
2. **Use template files**: Copy relevant templates from `templates/` directory
3. **Follow modular architecture**: Implement `core/parsers.py` + `core/analyzer.py` separation for data tools
4. **Include required documentation**: Always create `doc/ARCHITECTURE.md`

## Key Framework Principles

- UV-exclusive workflow for dependency management
- Modular architecture with separation of parsing and analysis
- Configurable parameters (avoid hardcoded constants)
- Comprehensive error handling with verbose modes
- Subcommand CLI structure for extensibility

## Template Files

- `templates/pyproject.toml` - UV project configuration with modern dependencies
- `templates/CLAUDE.md` - Project-specific Claude guidance template
- `templates/ARCHITECTURE.md` - Required architecture documentation template
- `templates/main.py` - CLI entry point with subcommand structure
- `templates/README.md` - Project README template
- `gitignore` - Comprehensive .gitignore for Python projects

## Coding Standards

- Python 3.10+ required
- UV for all dependency management (no pip/python direct usage)
- Type hints for public functions
- pathlib.Path for file operations
- Modular separation between parsing and analysis logic
- Comprehensive error handling patterns

## Project Creation Workflow

1. User creates new directory and asks Claude to reference `VAULT_TOOL_SETUP.md`
2. Claude should use templates from this repository
3. Follow the modular architecture patterns
4. Create all required documentation files
5. Set up proper UV configuration and testing framework