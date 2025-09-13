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

## Output Design Specification

When presenting information to the user, especially for script execution or previews, the following `rich`-based design should be used to ensure a consistent and aesthetically pleasing user experience.

### Script Execution Plan

Before executing a command or script, display a summary using a `rich.panel.Panel`.

-   **Title:** The panel should have a title, e.g., `[bold yellow]Script Execution Plan[/bold yellow]`.
-   **Border:** Use a distinct border style, e.g., `border_style="blue"`.
-   **Content:** The panel should clearly display:
    1.  **Working Directory:** The directory where the command will run. (e.g., `[bold magenta]Working Directory:[/] [cyan]/path/to/dir[/]`)
    2.  **Environment Variables:** Any *custom* environment variables being set for the command. (e.g., `[green]VAR_NAME[/] = [yellow]"value"[/]`)
    3.  **Command:** The command or script to be executed. This should be syntax-highlighted using `rich.syntax.Syntax` with the `bash` lexer and a theme like `monokai`.

This provides the user with a clear, readable confirmation of what is about to happen.