# Vault Tool Framework Agents

This directory contains Claude Code agents designed to work with the vault tool framework.

## Available Agents

### docs-updater

**File**: `docs-updater.md`

**Purpose**: Documentation Synchronization Specialist that maintains accurate, current project documentation reflecting the true state of development work.

**When to Use**:

- After completing a significant feature or milestone
- When preparing for a commit
- When the user explicitly says 'time for a commit' or 'update the docs'
- After refactoring or architectural changes
- When session state has evolved significantly
- When project structure has been modified

**Key Responsibilities**:

- Analyzes current project state and recent changes
- Updates core documentation files (CLAUDE.md, session_memory.json, docs/ directory)
- Maintains accuracy with current development status
- Preserves context and historical information
- Prepares documentation for commits

**Usage Pattern**:
The docs-updater agent is automatically triggered by Claude Code when documentation synchronization is needed. It works systematically through documentation files, making targeted updates based on actual project changes.

## Installing Agents

To use these agents with Claude Code:

1. Copy the agent file to your Claude Code agents directory
2. The agent will be available for use in your development sessions
3. Claude Code will automatically use the agent when appropriate trigger conditions are met

## Agent Development

These agents follow Claude Code agent specification format with:

- YAML frontmatter defining name, description, model, and color
- Detailed system prompt defining responsibilities and behavior
- Specific trigger conditions and usage examples