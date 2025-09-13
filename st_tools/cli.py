import pathlib


def main():
    path = pathlib.Path.cwd()
    print(f"Hello from {path}")
