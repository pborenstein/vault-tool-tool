#!/usr/bin/env python3
"""
Main CLI entry point for your-tool-name.

This module provides the command-line interface using argparse with subcommands
for extensibility. Choose between Pattern 1 (subcommands) or Pattern 2 (single command)
based on your tool's complexity.
"""

import argparse
import sys
from pathlib import Path

def create_parser():
    """Create the argument parser with subcommands."""
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
    """Main entry point."""
    parser = create_parser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    try:
        if args.command == "analyze":
            # Import your modular components
            from .core.parsers import detect_format, parse_input
            from .core.analyzer import DataAnalyzer

            # Handle analyze command with configurable parameters
            print(f"Analyzing {args.input}")

        elif args.command == "export":
            # Handle export command
            print(f"Exporting {args.input} as {args.format}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()