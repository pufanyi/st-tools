import argparse
from .submit import submit

def main(args: argparse.Namespace):
    command = args.command
    if command == "submit":
        submit(args)
    else:
        print(f"Unknown command: {command}")