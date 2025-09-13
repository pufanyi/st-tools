import os
from pathlib import Path

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
            self.script = f"sh {script_file.resolve()}"

        self.env = os.environ.copy()
        if env:
            self.env.update(env)

        self.custom_env = env or {}
        self.cwd = Path(cwd).resolve() if cwd else Path.cwd()

    def output_script(self):
        console = Console()

        lines = [
            Text.from_markup(
                f"[bold magenta]Working Directory:[/] [cyan]{self.cwd}[/]"
            )
        ]

        if self.custom_env:
            lines.append(
                Text.from_markup("\n[bold magenta]Environment Variables:[/]")
            )
            for key, value in self.custom_env.items():
                lines.append(Text.from_markup(f'  [green]{key}[/] = [yellow]"{value}"[/]'))

        lines.append(Text.from_markup("\n[bold magenta]Command to be executed:[/magenta]"))

        script_syntax = Syntax(self.script, "bash", theme="monokai", line_numbers=False)

        render_group = Group(*lines, script_syntax)

        panel = Panel(
            render_group,
            title="[bold yellow]Script Execution Plan[/bold yellow]",
            border_style="blue",
            expand=False,
            padding=(1, 2),
        )
        console.print(panel)

    def execute(self, need_confirm: bool = True):
        pass
