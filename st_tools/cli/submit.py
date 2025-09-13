import argparse

from ..script.script import Script


def configure_parser(subparsers):
    """Configure the parser for the 'submit' command."""
    parser = subparsers.add_parser("submit", help="Submit a solution")
    parser.set_defaults(func=submit)
    parser.add_argument("script", type=str, help="The script to submit")
    parser.add_argument("--env", type=str, help="The environment variables to set")
    parser.add_argument("--cwd", type=str, help="The current working directory")


def submit(args: argparse.Namespace):
    """The entry point for the 'submit' command."""
    command = Script(args.script, args.env, args.cwd)
    command.execute()
