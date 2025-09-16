# Vault Tool Framework Setup Guide

This guide helps you initialize new projects within the vault tool framework. These tools share a common architecture for processing Obsidian vaults and text repositories.

## Framework Overview

The vault tool framework provides a standardized approach for building CLI tools that:

- Process Obsidian vaults and markdown collections
- Use UV for dependency management and packaging
- Follow consistent project structure and coding standards
- Integrate with Claude Code for development assistance
- Maintain comprehensive documentation and testing

## UV Setup

### Prerequisites

Ensure you have UV installed:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
# or: brew install uv
```

### Manual Setup

1. **Create project directory:**
   ```bash
   mkdir your-tool-name
   cd your-tool-name
   ```

2. **Initialize UV project:**
   ```bash
   uv init --package
   ```

3. **Create proper package structure:**
   ```bash
   # Create the main package directory (replace hyphens with underscores)
   mkdir -p your_tool_name/core your_tool_name/utils tests doc

   # Create __init__.py files
   touch your_tool_name/__init__.py
   touch your_tool_name/core/__init__.py
   touch your_tool_name/utils/__init__.py
   touch tests/__init__.py
   ```

   **Modular Architecture Guidelines:**

   For data processing tools, use modular separation between parsing and analysis:
   - `core/parsers.py` - Input format detection and data parsing logic
   - `core/analyzer.py` - Analysis algorithms and business logic
   - `core/models.py` - Data models and type definitions (if needed)

   This separation enables independent testing, easier maintenance, and cleaner code organization. Avoid monolithic modules that combine parsing and analysis functions.

   **Note**: UV may create an empty `src/` directory during initialization. This can be safely ignored for the vault tool framework - we use the package directory directly at the root level.

4. **Configure pyproject.toml:**
   ```toml
   [project]
   name = "your-tool-name"
   version = "0.1.0"
   description = "Your tool description"
   requires-python = ">=3.10"
   readme = "README.md"
   license = "MIT"  # Optional: See LICENSE file or specify your preferred license
   authors = [{ name = "Contributors" }]
   dependencies = [
       # Add your core dependencies here
       # For visualization tools, use: "matplotlib>=3.7.0"
       # For data processing: "pandas>=2.0.0" (if needed)
   ]

   [project.optional-dependencies]
   test = [
       "pytest>=8.0",
       "pytest-cov>=4.0",
       "pytest-mock>=3.0",
   ]
   dev = [
       "ruff>=0.6.0",
       "black>=24.0",
       "mypy>=1.9.0",
   ]

   [project.scripts]
   your-tool-name = "your_tool_name.main:main"

   [tool.uv]
   package = true

   [tool.setuptools]
   packages = ["your_tool_name", "your_tool_name.core", "your_tool_name.utils"]

   [tool.pytest.ini_options]
   testpaths = ["tests"]
   addopts = "-q"

   [tool.black]
   target-version = ["py310"]
   line-length = 100

   [tool.ruff]
   line-length = 100
   target-version = "py310"

   [tool.ruff.lint]
   select = ["E", "F", "I", "UP", "B", "S"]
   ignore = []

   [build-system]
   requires = ["setuptools>=61.0", "wheel"]
   build-backend = "setuptools.build_meta"
   ```

5. **Create main entry point:**
   ```bash
   # Create your_tool_name/main.py with CLI entry point
   # Use relative imports: from .core.module import function
   ```

6. **Set up test structure:**
   ```bash
   # Create test files in tests/ directory
   # Test imports should use: from your_tool_name.module import function
   ```

7. **Install dependencies:**
   ```bash
   uv sync
   # Add test dependencies
   uv add --optional test pytest pytest-cov pytest-mock
   ```

8. **Replace default .gitignore:**
   ```bash
   # UV creates a minimal .gitignore - replace with comprehensive version
   # Copy from vault-tool-tool/gitignore or use this template
   ```

   **Comprehensive .gitignore Template:**
   ```gitignore
   # Byte-compiled / optimized / DLL files
   __pycache__/
   *.py[cod]
   *$py.class

   # C extensions
   *.so

   # Distribution / packaging
   .Python
   build/
   develop-eggs/
   dist/
   downloads/
   eggs/
   .eggs/
   lib/
   lib64/
   parts/
   sdist/
   var/
   wheels/
   share/python-wheels/
   *.egg-info/
   .installed.cfg
   *.egg
   MANIFEST

   # PyInstaller
   #  Usually these files are written by a python script from a template
   #  before PyInstaller builds the exe, so as to inject date/other infos into it.
   *.manifest
   *.spec

   # Installer logs
   pip-log.txt
   pip-delete-this-directory.txt

   # Unit test / coverage reports
   htmlcov/
   .tox/
   .nox/
   .coverage
   .coverage.*
   .cache
   nosetests.xml
   coverage.xml
   *.cover
   *.py,cover
   .hypothesis/
   .pytest_cache/
   cover/

   # Translations
   *.mo
   *.pot

   # Django stuff:
   *.log
   local_settings.py
   db.sqlite3
   db.sqlite3-journal

   # Flask stuff:
   instance/
   .webassets-cache

   # Scrapy stuff:
   .scrapy

   # Sphinx documentation
   docs/_build/

   # PyBuilder
   .pybuilder/
   target/

   # Jupyter Notebook
   .ipynb_checkpoints

   # IPython
   profile_default/
   ipython_config.py

   # pyenv
   #   For a library or package, you might want to ignore these files since the code is
   #   intended to run in multiple environments; otherwise, check them in:
   # .python-version

   # pipenv
   #   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
   #   However, in case of collaboration, if having platform-specific dependencies or dependencies
   #   having no cross-platform support, pipenv may install dependencies that don't work, or not
   #   install all needed dependencies.
   #Pipfile.lock

   # poetry
   #   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
   #   This is especially recommended for binary packages to ensure reproducibility, and is more
   #   commonly ignored for libraries.
   #   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
   #poetry.lock

   # pdm
   #   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
   #pdm.lock
   #   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
   #   in version control.
   #   https://pdm.fming.dev/#use-with-ide
   .pdm.toml

   # PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
   __pypackages__/

   # Celery stuff
   celerybeat-schedule
   celerybeat.pid

   # SageMath parsed files
   *.sage.py

   # Environments
   .env
   .venv
   env/
   venv/
   ENV/
   env.bak/
   venv.bak/

   # Spyder project settings
   .spyderproject
   .spyproject

   # Rope project settings
   .ropeproject

   # mkdocs documentation
   /site

   # mypy
   .mypy_cache/
   .dmypy.json
   dmypy.json

   # Pyre type checker
   .pyre/

   # pytype static type analyzer
   .pytype/

   # Cython debug symbols
   cython_debug/

   # PyCharm
   #  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
   #  be added to the global gitignore or merged into this project gitignore. For PyCharm
   #  Community Edition, use 'PyCharm CE' instead of 'PyCharm'.
   .idea/

   # macOS
   .DS_Store
   .AppleDouble
   .LSOverride

   # Icon must end with two \r
   Icon

   # Thumbnails
   ._*

   # Files that might appear in the root of a volume
   .DocumentRevisions-V100
   .fseventsd
   .Spotlight-V100
   .TemporaryItems
   .Trashes
   .VolumeIcon.icns
   .com.apple.timemachine.donotpresent

   # Directories potentially created on remote AFP share
   .AppleDB
   .AppleDesktop
   Network Trash Folder
   Temporary Items
   .apdisk

   # General
   *.swp
   *.swo
   *~

   # Log files
   *.log

   # Temporary files
   tmp/
   temp/

   # IDE files
   .vscode/
   *.sublime-project
   *.sublime-workspace

   # Claude Code configuration
   .claude/

   # Project-specific files (add as needed)
   tag_migration_log.json
   tag-*.json
   ```

   **Note**: Add project-specific patterns to the end of .gitignore as needed (e.g., `emojis.nogit.json`, log files, temporary data files).

9. **Test the setup:**
   ```bash
   # Development testing
   uv run python -m your_tool_name.main --help
   uv run python -m pytest tests/ -v
   ```

## Installation Methods

### Development Usage (Recommended)

For development and testing, use the UV run method which works reliably:

```bash
# Primary development usage
uv run python -m your_tool_name.main [command] [options]

# Running tests
uv run python -m pytest tests/ -v

# Code quality checks
uv run ruff check .
uv run black .
uv run mypy .
```

### System-Wide Installation (Optional)

Installing as a system command generally works well but development mode is still recommended:

```bash
# Install as system tool
uv tool install --editable .

# If successful, you can use:
your-tool-name [command] [options]
```

**Note**: While `uv tool install` typically succeeds, development mode (`uv run python -m`) is recommended for active development as it ensures you're always using the latest code changes without reinstalling.

### Troubleshooting Installation Issues

**Problem**: `ModuleNotFoundError: No module named 'your_tool_name.main'`

**Solution**: Use development method for testing:
```bash
uv run python -m your_tool_name.main [args]
```

**Problem**: Import errors in tests

**Solution**: Ensure test imports use full package path:
```python
from your_tool_name.core.module import function
```

**Problem**: Package structure not recognized

**Solution**: Verify all `__init__.py` files exist and pyproject.toml packages list is correct.

**Problem**: Changes not reflected after system installation

**Solution**: Reinstall with `uv tool install --editable .` or use development mode for active development.

### Automated Setup

Ask Claude to set up the project for you:

> "Please set up a new vault tool project called [tool-name] following the framework patterns. Include [specific requirements]."

Claude will:
- Create the modular directory structure (core/parsers.py + core/analyzer.py for data tools)
- Configure pyproject.toml with appropriate dependencies and modern version minimums
- Replace UV's minimal .gitignore with comprehensive vault tool framework version
- Set up testing framework with comprehensive coverage
- Create REQUIRED architecture documentation (doc/ARCHITECTURE.md)
- Configure development tools and error handling patterns
- Implement subcommand CLI structure for extensibility
- Set up configurable parameter patterns (avoid hardcoded constants)

## Project CLAUDE.md Template

Create a `CLAUDE.md` file in your project root with these sections:

```markdown
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
- 2-space indentation (per global CLAUDE.md)
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
```

## Documentation Templates

### README.md Structure

```markdown
# your-tool-name

[Brief description and purpose]

[ASCII diagram showing data flow if applicable]

## Quick start

- Install with uv: `uv tool install --editable .`
- Basic usage: `your-tool-name [command] [options]`
- Run tests: `uv run pytest tests/`

## Commands

[Detailed command documentation]

## Installation

This project uses uv for dependency management.

```bash
uv tool install --editable .
# or for development
uv sync
```

## Documentation

- Architecture: `doc/ARCHITECTURE.md`
- [Other relevant docs]

## Project layout

[Directory structure overview]
```

### Architecture Documentation (REQUIRED)

**MANDATORY**: Every vault tool project must include comprehensive architecture documentation.

Create `doc/ARCHITECTURE.md`:

```markdown
# Architecture

## Overview

[High-level system description explaining the tool's purpose and approach]

## Module Structure

### Core Modules

- **`core/parsers.py`** - Input format detection and data parsing logic
  - Functions: `detect_format()`, `parse_csv()`, `parse_markdown()`, etc.
  - Responsibility: Convert various input formats to standardized data structures

- **`core/analyzer.py`** - Analysis algorithms and business logic
  - Class: `DataAnalyzer` (parameterized, configurable)
  - Responsibility: Process parsed data and generate insights

- **`utils/`** - Shared utilities for file operations, logging, validation

### Design Principles

- **Separation of Concerns**: Parsing and analysis are independently testable
- **Configurability**: Avoid hardcoded constants, use parameterized classes
- **Extensibility**: Subcommand structure supports future feature additions

## Data Flow

[Process flow description from input → parsing → analysis → output]

## Design Decisions

### Modular vs Monolithic Architecture

**Decision**: Use separate `parsers.py` and `analyzer.py` modules

**Rationale**: Enables independent testing, easier maintenance, and cleaner separation between data ingestion and business logic. While a single module is simpler initially, the modular approach scales better for long-term development.

### Configurable Parameters

**Decision**: Pass configuration parameters to analyzer constructor rather than using module-level constants

**Rationale**: Makes the tool adaptable to different datasets and use cases without code changes.

[Additional key architectural choices and rationale]
```

## docs-updater Agent Integration

### Installation (Optional)

The docs-updater agent is available in this framework repository but is **not automatically installed**. To use it:

1. **Manual Installation** (recommended for control):
   ```bash
   # Copy the agent to your Claude Code agents directory
   cp agents/docs-updater.md ~/.claude/agents/

   # Or create a symlink to stay updated with framework changes
   ln -s $(pwd)/agents/docs-updater.md ~/.claude/agents/docs-updater.md
   ```

2. **Verify Installation**:
   The agent will appear in Claude Code's available agents list and can be triggered when documentation synchronization is needed.

**Note**: The docs-updater agent works with any project type, not just vault tools. It intelligently detects your project structure and adapts its documentation approach accordingly.

### When to Use

Use the docs-updater agent proactively in these scenarios:

1. **After completing significant features** - When you've implemented a major component
2. **Before commits** - When preparing to commit substantial changes
3. **After refactoring** - When architectural changes affect documentation
4. **Explicit requests** - When the user says "update the docs" or "time for a commit"

### Usage Pattern

```markdown
# In your conversations with Claude:
user: "I've finished implementing the core scanner functionality"
claude: "I'll use the docs-updater agent to ensure all documentation is current with the new scanner implementation."
```

### Best Practices

- The agent must be manually installed to be available
- Let Claude trigger the docs-updater agent when appropriate trigger conditions are met
- The agent will synchronize all documentation with current code state
- It updates README, architecture docs, and code comments
- Always run before major commits

## Common Patterns & Idioms

### CLI Framework Choice

Choose the appropriate CLI framework based on your tool's complexity:

#### **argparse (Recommended for Simple Tools)**
- **Use when**: Zero external dependencies desired, simple command structure
- **Benefits**: Part of standard library, lightweight, sufficient for most vault tools
- **Example**: emoji-sniper uses argparse for scan/substitute commands

```python
# Simple argparse structure
import argparse

def create_parser():
    parser = argparse.ArgumentParser(description="Tool description")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    scan_parser = subparsers.add_parser("scan", help="Scan files")
    scan_parser.add_argument("vault_path", type=Path, help="Vault directory")
    scan_parser.add_argument("--format", choices=["json", "txt"], default="json")

    return parser
```

#### **click (Advanced CLI Features)**
- **Use when**: Complex command hierarchies, rich help formatting, advanced validation needed
- **Benefits**: Better help generation, parameter validation, command chaining
- **Example**: tagex uses click for vault-first argument structure with global options

```python
# click structure with global options
import click

@click.group()
@click.argument('vault_path', type=click.Path(exists=True))
@click.option('--tag-types', type=click.Choice(['both', 'frontmatter', 'inline']))
@click.pass_context
def main(ctx, vault_path, tag_types):
    ctx.ensure_object(dict)
    ctx.obj['vault_path'] = vault_path
    ctx.obj['tag_types'] = tag_types

@main.command()
@click.option('--format', type=click.Choice(['json', 'csv', 'txt']))
@click.pass_context
def extract(ctx, format):
    # Access global options via ctx.obj
    pass
```

**Framework Selection Guidelines:**
- **Simple tools** (1-3 commands, basic options): Use argparse
- **Complex tools** (many commands, global options, rich help): Use click
- **Zero dependencies preferred**: Use argparse
- **Rich CLI experience needed**: Use click

### CLI Structure

#### Pattern 1: Subcommand-Based (Recommended for Data Processing Tools)

```python
# main.py - Standard argparse structure with subcommands
import argparse
from pathlib import Path

def create_parser():
    parser = argparse.ArgumentParser(description="Tool description")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add analyze subcommand (common for data tools)
    analyze_parser = subparsers.add_parser("analyze", help="Analyze input data")
    analyze_parser.add_argument("input", nargs="?", default="-", help="Input file or '-' for stdin")
    analyze_parser.add_argument("--format", help="Input format (auto-detected if not specified)")
    analyze_parser.add_argument("--output", help="Output file path")
    analyze_parser.add_argument("--year", type=int, help="Year to analyze (configurable)")
    analyze_parser.add_argument("-v", "--verbose", action="count", default=0, help="Increase verbosity")

    # Add export subcommand
    export_parser = subparsers.add_parser("export", help="Export processed data")
    export_parser.add_argument("input", help="Input file")
    export_parser.add_argument("--format", choices=["csv", "json"], default="csv", help="Export format")

    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.command == "analyze":
        # Import your modular components
        from .core.parsers import detect_format, parse_input
        from .core.analyzer import analyze_data

        # Handle analyze command with configurable parameters
        pass
    elif args.command == "export":
        # Handle export command
        pass

if __name__ == "__main__":
    main()
```

#### Pattern 2: Single Command with Options (Simple Tools)

```python
# main.py - Simple single-purpose tool
import argparse
import sys
from pathlib import Path

def create_parser():
    parser = argparse.ArgumentParser(
        description="Analyze data from various formats"
    )
    parser.add_argument(
        "input",
        nargs="?",
        default="-",
        help="Input file or '-' for stdin"
    )
    parser.add_argument(
        "--output",
        help="Output file path"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="count",
        default=0,
        help="Increase verbosity"
    )
    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()

    try:
        # Process the input
        process_data(args.input, args.output, args.verbose)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```

### Module Organization

```
your-tool/
├─ your_tool_name/     # Main package directory
│  ├─ __init__.py
│  ├─ main.py          # CLI entry point
│  ├─ core/            # Core business logic
│  │  ├─ __init__.py
│  │  ├─ parsers.py    # Input format detection and parsing
│  │  ├─ analyzer.py   # Analysis algorithms (parameterized)
│  │  └─ models.py     # Data models
│  └─ utils/           # Shared utilities
│     ├─ __init__.py
│     ├─ file_ops.py   # File operations
│     └─ logging_setup.py # Logging configuration
├─ tests/              # Test suite
│  ├─ __init__.py
│  ├─ test_parsers.py  # Test parsing logic
│  ├─ test_analyzer.py # Test analysis logic
│  └─ test_models.py
├─ doc/                # Documentation
└─ pyproject.toml      # Project configuration
```

### Configurable Parameters Pattern

Avoid hardcoded constants in core logic. Make analysis functions parameterizable:

```python
# Good: Configurable analyzer
class DataAnalyzer:
    def __init__(self, target_year: int = None):
        self.target_year = target_year or datetime.now().year

    def analyze(self, data: list, **kwargs) -> dict:
        # Use self.target_year for filtering
        filtered_data = [item for item in data if item.year == self.target_year]
        return self._compute_analysis(filtered_data)

# Bad: Hardcoded constants
TARGET_YEAR = 2025  # Hardcoded at module level

def analyze_data(data: list) -> dict:
    # Locked to specific year
    filtered_data = [item for item in data if item.year == TARGET_YEAR]
    return compute_analysis(filtered_data)
```

### Path Handling

```python
from pathlib import Path

def process_path(target: Path) -> None:
    """Always use pathlib.Path for file operations."""
    if target.is_file():
        # Process single file
        pass
    elif target.is_dir():
        # Process directory
        for file_path in target.rglob("*.md"):
            # Process each file
            pass
```

### Logging Setup

```python
import logging
from pathlib import Path

def setup_logging(log_dir: Path = Path("log"), verbose: int = 0):
    """Standard logging configuration."""
    log_dir.mkdir(exist_ok=True)

    level = logging.WARNING
    if verbose == 1:
        level = logging.INFO
    elif verbose >= 2:
        level = logging.DEBUG

    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_dir / "tool.log"),
            logging.StreamHandler()
        ]
    )
```

### Error Handling

#### Comprehensive Error Handling with Verbose Mode

```python
import sys
import logging
from pathlib import Path

def validate_path(path: Path, verbose: int = 0) -> Path:
    """Standard path validation with verbose error details."""
    if not path.exists():
        error_msg = f"Error: Path does not exist: {path}"
        if verbose > 0:
            error_msg += f"\nCurrent working directory: {Path.cwd()}"
            error_msg += f"\nParent directory exists: {path.parent.exists()}"
        print(error_msg, file=sys.stderr)
        sys.exit(1)

    if verbose >= 2:
        print(f"Debug: Validated path: {path.resolve()}", file=sys.stderr)

    return path.resolve()

def handle_processing_error(error: Exception, input_path: str, verbose: int = 0) -> None:
    """Standard error handling for data processing."""
    error_msg = f"Error processing {input_path}: {error}"

    if verbose > 0:
        import traceback
        error_msg += f"\n\nDetailed traceback:\n{traceback.format_exc()}"

    print(error_msg, file=sys.stderr)
    sys.exit(1)
```

#### Standard Path Validation

```python
import sys
from pathlib import Path

def validate_path(path: Path) -> Path:
    """Standard path validation."""
    if not path.exists():
        print(f"Error: Path does not exist: {path}", file=sys.stderr)
        sys.exit(1)
    return path.resolve()
```

#### Optional Dependency Handling

```python
import sys

def create_plot(output_path: str, data: dict) -> None:
    """Create plot with graceful fallback for missing dependencies."""
    if not output_path:
        return

    try:
        import matplotlib.pyplot as plt
    except ImportError as e:
        print(f"--plot requested but matplotlib unavailable: {e}", file=sys.stderr)
        return

    # Create plot with matplotlib
    plt.figure(figsize=(10, 6))
    # ... plotting code ...
    plt.savefig(output_path)
    plt.close()
```

#### File Operation Error Handling

```python
from pathlib import Path
from typing import Union

def read_input_file(path: Union[str, Path]) -> str:
    """Read file with proper error handling."""
    if path == "-" or not path:
        return sys.stdin.read()

    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Input file does not exist: {path}")

    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except PermissionError:
        raise PermissionError(f"Permission denied reading file: {path}")
    except UnicodeDecodeError:
        raise ValueError(f"File is not valid UTF-8: {path}")
```

### Testing Patterns

```python
import pytest
import tempfile
from pathlib import Path
from your_tool_name.core.scanner import ScannerClass

@pytest.fixture
def temp_dir():
    """Provide temporary directory for tests."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)

def test_core_functionality(temp_dir):
    """Test core functionality with temp files."""
    test_file = temp_dir / "test.md"
    test_file.write_text("# Test content")

    # Import from your package
    scanner = ScannerClass()
    result = scanner.process(test_file)

    assert test_file.exists()
    assert result is not None
```

## UV Workflow Standards

Always use UV for all Python operations:

```bash
# Correct - Development workflow
uv run python -m pytest tests/ -v
uv run python -m your_tool_name.main [args]
uv sync
uv add --optional test pytest pytest-cov pytest-mock

# Optional - System installation (may have issues)
uv tool install --editable .

# Avoid - Direct python usage
python -m pytest tests/
python -m your_tool_name.main
pip install -e .
```

**Development Workflow Notes:**
- Use `uv run python -m` prefix for reliable execution
- Test dependencies should be added with `--optional test` flag
- Package module path uses underscores (your_tool_name) not hyphens
- System installation with `uv tool install` may fail due to import path issues

This ensures consistent dependency management and virtual environment handling across all vault tools.

## Practical Insights

### Project Initialization Notes

- UV may create additional directories (like `src/`) that can be safely ignored for vault tools
- The framework uses a flat package structure at the root level for simplicity
- Focus on the core functionality first; documentation can be refined iteratively

### CLI Design Guidelines

- **Simple tools**: Use Pattern 2 (single command with options) for focused, single-purpose tools
- **Complex tools**: Use Pattern 1 (subcommands) when you have multiple distinct operations
- **Data processing tools**: Prefer Pattern 1 (subcommands) for extensibility, even if starting simple. Benefits include format auto-detection, multiple output modes, and future command additions. Often benefit from stdin/stdout support with `-` convention
- **Analysis tools**: Consider multiple output formats (text, CSV, charts) for flexibility. Use subcommands to organize different analysis types

### Development Workflow Tips

- Start with `uv run python -m your_tool.main --help` to verify basic CLI structure
- Test with sample data early to validate parsing and core logic
- Use the test suite to ensure reliability before system installation
- Consider optional dependencies (like matplotlib) and provide graceful fallbacks

### Common Patterns by Tool Type

#### Data Processing Tools (Recommended Architecture)

For tools that process structured data (CSV, logs, exports), follow the movie-tool pattern:

**Architecture**: `core/parsers.py` + `core/analyzer.py` separation
```python
# core/parsers.py - Format detection and parsing
def detect_format(input_data: str) -> str:
    """Auto-detect input format from content."""
    if input_data.startswith("file name,watched"):
        return "csv"
    elif "|" in input_data and "---|" in input_data:
        return "markdown"
    # Add more format detection logic

def parse_input(data: str, format_type: str = None) -> list:
    """Parse input data based on detected or specified format."""
    if not format_type:
        format_type = detect_format(data)

    if format_type == "csv":
        return parse_csv(data)
    elif format_type == "markdown":
        return parse_markdown(data)
    # Handle other formats

# core/analyzer.py - Configurable analysis
class DataAnalyzer:
    def __init__(self, target_year: int = None, **config):
        self.target_year = target_year or datetime.now().year
        self.config = config

    def analyze(self, parsed_data: list) -> dict:
        """Perform analysis with configurable parameters."""
        filtered_data = self._filter_by_year(parsed_data)
        return self._compute_statistics(filtered_data)
```

**CLI Structure**: Use subcommands even for simple tools to enable future expansion
```bash
tool-name analyze input.csv --year 2024 --format csv --output results.json
tool-name export processed_data.json --format csv
```

#### Other Tool Types

- **File processors**: Path validation → file iteration → transformation → output
- **Report generators**: Data collection → analysis → formatting → export
- **Workflow tools**: Command chaining → state management → progress tracking