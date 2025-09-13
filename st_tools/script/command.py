import os
from pathlib import Path


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

        self.cwd = Path(cwd).resolve() if cwd else Path.cwd()

    def output_script(self):
        pass

    def execute(self, need_confirm: bool = True):
        pass
