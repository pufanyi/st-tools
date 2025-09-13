# Gemini's Notes: st-tools Project

This document provides a high-level overview of the `st-tools` project. It should be updated frequently to reflect the current state of the project and serve as a quick reference for developers.

## Project Overview

`st-tools` is a Python command-line interface (CLI) tool designed to streamline development workflows. The main source code is located in the `st_tools/` directory.

## Project Structure

*   `st_tools/cli/main.py`: The main entry point for the CLI, using `argparse` to handle commands.
*   `st_tools/cli/submit.py`: Implements the logic for the `submit` subcommand.
*   `st_tools/script/script.py`: Contains the `Script` class responsible for preparing and displaying command execution plans.
*   `pyproject.toml`: Defines project metadata, dependencies, and the `st-tools` script entry point.
*   `GEMINI.md`: This file, containing essential project information.

## Dependencies & Tooling

*   **Dependency Manager**: The project uses `uv`. Dependencies are listed in `pyproject.toml` and locked in `uv.lock`.
    *   To add a new dependency, run: `uv add <dependency-name>`
*   **Main Dependency**: `rich` is used for all rich text and formatted output in the terminal.
*   **Dev Dependencies**:
    *   `ruff`: For linting and code formatting.
    *   `pre-commit`: For managing and executing pre-commit hooks.

## Running the CLI

The CLI is exposed via the `st-tools` command, which is defined in the `[project.scripts]` section of `pyproject.toml`.

Example usage:
```bash
st-tools submit <path/to/script>
```

## Development Guidelines

### `rich` Library Usage

When working with the `rich` library, please adhere to the following:

*   **`Group` vs. `RenderGroup`**: `RenderGroup` is deprecated. Use `Group` imported from `rich.console` to group renderable elements.
*   **Markup Closing Tags**: Ensure all markup tags are closed correctly and in the proper order. An opening tag like `[bold magenta]` must be closed with a corresponding `[/]` or `[/bold magenta]`. An incorrect closing tag (e.g., `[/magenta]`) will raise a `rich.errors.MarkupError`.

### Output Design Specification

To ensure a consistent user experience, all script execution previews must use the following `rich`-based design.

**Script Execution Plan Panel:**

*   **Component**: `rich.panel.Panel`
*   **Title**: `[bold yellow]Script Execution Plan[/bold yellow]`
*   **Border Style**: `blue`
*   **Content**: The panel should clearly display:
    1.  **Working Directory**: e.g., `[bold magenta]Working Directory:[/] [cyan]/path/to/dir[/]`
    2.  **Environment Variables**: List any custom environment variables being set.
    3.  **Command**: The command to be executed, syntax-highlighted using `rich.syntax.Syntax` with the `bash` lexer.
