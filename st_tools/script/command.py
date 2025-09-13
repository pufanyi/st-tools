import os
from pathlib import Path
from rich import print


class Script:
    def __init__(
        self,
        script: str | os.PathLike,
        env: dict[str, str] | None = None,
        cwd: str | os.PathLike | None = None,
    ):
        self.script = Path(script).resolve()
        if not self.script.exists() or not self.script.is_file():
            raise FileNotFoundError(
                f"Script {self.script} does not exist, or is not a file"
            )
        self.env = os.environ.copy()
        if env:
            self.env.update(env)
        self.cwd = Path(cwd).resolve() if cwd else Path.cwd()
    
    def output(self):
        pass

    def execute(self, need_confirm: bool = True):
        pass
