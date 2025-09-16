# Vault Tool Framework

A standardized framework for building CLI tools that process Obsidian vaults and markdown collections. This framework provides consistent project structure, dependency management, and coding patterns for vault tool development.

## Quick Start

### Creating a New Vault Tool

1. **Create your project directory:**
   ```bash
   mkdir my-vault-tool
   cd my-vault-tool
   ```

2. **Ask Claude to set up the project:**
   ```
   Please set up a new vault tool project called "my-vault-tool" following the
   framework patterns in VAULT_TOOL_SETUP.md. Include data processing capabilities.
   ```

3. **Claude will automatically:**
   - Copy templates from this framework
   - Set up UV project configuration
   - Create modular architecture (`core/parsers.py` + `core/analyzer.py`)
   - Configure testing and development tools
   - Generate required documentation

### Manual Setup (Alternative)

If you prefer manual setup, follow the detailed guide in [VAULT_TOOL_SETUP.md](VAULT_TOOL_SETUP.md).

## Framework Components

### Templates Directory

Ready-to-use boilerplate files:

- **`templates/pyproject.toml`** - UV project configuration with modern Python dependencies
- **`templates/CLAUDE.md`** - Project-specific guidance for Claude Code
- **`templates/ARCHITECTURE.md`** - Required architecture documentation template
- **`templates/main.py`** - CLI entry point with subcommand structure
- **`templates/README.md`** - Project README template

### Configuration Files

- **`gitignore`** - Comprehensive .gitignore for Python vault tools
- **`VAULT_TOOL_SETUP.md`** - Complete setup guide and framework documentation

## Architecture Patterns

### Modular Data Processing Tools

For tools that process structured data, use the recommended modular architecture:

```
your-tool/
├─ your_tool_name/
│  ├─ main.py              # CLI entry point
│  ├─ core/
│  │  ├─ parsers.py        # Input format detection and parsing
│  │  └─ analyzer.py       # Analysis algorithms (configurable)
│  └─ utils/               # Shared utilities
├─ tests/                  # Test suite
├─ doc/
│  └─ ARCHITECTURE.md      # Required documentation
└─ pyproject.toml          # UV configuration
```

### Key Design Principles

- **Separation of Concerns**: Parsing and analysis are independently testable
- **Configurability**: Avoid hardcoded constants, use parameterized classes
- **Extensibility**: Subcommand CLI structure supports future features
- **UV-Exclusive**: All dependency management through UV

## Development Workflow

### Standard Commands

```bash
# Development mode (recommended)
uv run python -m your_tool_name.main [command] [options]

# Install dependencies
uv sync

# Run tests
uv run python -m pytest tests/ -v

# Code quality
uv run ruff check .
uv run black .
uv run mypy .

# System installation (optional)
uv tool install --editable .
```

### Common Patterns

#### CLI Structure (Subcommands)
```bash
tool-name analyze input.csv --year 2024 --format csv --output results.json
tool-name export processed_data.json --format csv
```

#### Error Handling
```python
def validate_path(path: Path, verbose: int = 0) -> Path:
    if not path.exists():
        error_msg = f"Error: Path does not exist: {path}"
        if verbose > 0:
            error_msg += f"\\nCurrent working directory: {Path.cwd()}"
        print(error_msg, file=sys.stderr)
        sys.exit(1)
    return path.resolve()
```

## Framework Benefits

- **Consistency**: All vault tools follow the same patterns
- **Quality**: Built-in testing, linting, and type checking
- **Maintainability**: Modular architecture scales with complexity
- **Documentation**: Required architecture documentation
- **Development Speed**: Templates and patterns reduce setup time

## Getting Help

1. **Setup Issues**: Refer to [VAULT_TOOL_SETUP.md](VAULT_TOOL_SETUP.md) troubleshooting section
2. **Architecture Questions**: See framework patterns in the setup guide
3. **Claude Integration**: The framework includes CLAUDE.md templates for optimal Claude Code assistance

## Examples

The framework has been used to create various vault tools:

- Data processing tools with CSV/markdown input parsing
- Analysis tools with configurable parameters
- Export tools with multiple output formats
- Workflow automation tools

Each follows the same modular architecture and development patterns outlined in this framework.