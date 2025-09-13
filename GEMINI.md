# Gemini's Notes: st-tools Project

This document is intended to be a living document that provides a high-level overview of the `st-tools` project. It should be updated frequently to reflect the current state of the project.

## Project Overview

This is a Python command-line interface (CLI) tool named `st-tools`. The source code is located in the `st_tools/` directory.

## Packaging and Dependencies

*   **Configuration:** The project is configured using `pyproject.toml`.
*   **Dependency Manager:** Uses `uv` for dependency management, with dependencies locked in `uv.lock`. To add a new dependency, use the `uv add <dependency-name>` command.
*   **Main Dependency:** `rich` for rich text formatting in the terminal.
*   **Development Dependencies:** `ruff` for linting and `pre-commit` for git hooks.

## Structure and Execution

*   **Entry Point:** The CLI is exposed via the `st-tools` command, which is defined in `[project.scripts]` in `pyproject.toml`.
*   **Main Function:** The script entry point maps to the `main` function in `st_tools/cli/main.py`.
*   **Command Structure:** The CLI uses `argparse` with subparsers to handle different commands. The only command implemented so far is `submit`, with its logic stub in `st_tools/cli/submit.py`.

## Documentation

This file (`GEMINI.md`) should be reviewed and updated frequently (e.g., after each code change) to ensure that the information is always up-to-date and accurately reflects the project's status. It's important to check for any misunderstandings or incorrect information.
