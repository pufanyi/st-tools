import os
import shlex
import subprocess
from pathlib import Path

from InquirerPy import inquirer
from rich.console import Console, Group
from rich.panel import Panel
from rich.syntax import Syntax
from rich.text import Text


class Script:
    def __init__(
        self,
        script: str | os.PathLike,
        env: dict[str, str] | None = None,
        cwd: str | os.PathLike | None = None,
    ):
        script_file: Path | None = None
        if isinstance(script, os.PathLike):
            script_file = Path(script)
            if not script_file.exists() or not script_file.is_file():
                raise FileNotFoundError(
                    f"Script {script_file} does not exist, or is not a file"
                )
        elif isinstance(script, str):
            try:
                script_file = Path(script)
                if not script_file.exists() or not script_file.is_file():
                    script_file = None
            except Exception:
                script_file = None
        else:
            raise ValueError(f"Invalid script type: {type(script)}")

        if script_file is None:
            self.script = script
        else:
            self.script = f"sh {shlex.quote(script_file.resolve().as_posix())}"

        self.env = os.environ.copy()
        if env:
            self.env.update(env)

        self.custom_env = env or {}
        self.cwd = Path(cwd).resolve() if cwd else Path.cwd()

    def get_script(self):
        final_script_lines = []
        final_script_lines.append(f"cd {shlex.quote(self.cwd.resolve().as_posix())}")
        for key, value in self.env.items():
            final_script_lines.append(f"export {shlex.quote(key)}={shlex.quote(value)}")
        final_script_lines.append(self.script)

        script_body = "\n".join(final_script_lines)
        quoted_script = shlex.quote(script_body)
        final_script = f"zsh -c {quoted_script}"
        return final_script

    def output_script(self, console: Console | None = None):
        console = console or Console()

        lines = [
            Text.from_markup(f"[bold magenta]Working Directory:[/] [cyan]{self.cwd}[/]")
        ]

        if self.custom_env:
            lines.append(Text.from_markup("\n[bold magenta]Environment Variables:[/]"))
            for key, value in self.custom_env.items():
                lines.append(
                    Text.from_markup(f'  [green]{key}[/] = [yellow]"{value}"[/]')
                )

        lines.append(Text.from_markup("\n[bold magenta]Command to be executed:[/]"))

        script_syntax = Syntax(self.script, "bash", theme="monokai", line_numbers=False)

        render_group = Group(*lines, script_syntax)

        panel = Panel(
            render_group,
            title="[bold yellow]Script Execution Plan[/bold yellow]",
            border_style="blue",
            padding=(1, 2),
        )
        console.print(panel)
        return panel

    def execute(self, need_confirm: bool = True):
        script = self.get_script()
        if need_confirm:
            console = Console()
            self.output_script(console)
            confirm = inquirer.confirm(
                message="Are you sure you want to execute this script?"
            ).execute()
            if not confirm:
                return False
        subprocess.run(self.get_script(), shell=True)
        return True
