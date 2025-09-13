import argparse


def configure_parser(subparsers):
    """Configure the parser for the 'submit' command."""
    parser = subparsers.add_parser("submit", help="Submit a solution")
    parser.set_defaults(func=submit)


def submit(args: argparse.Namespace):
    """The entry point for the 'submit' command."""
    print(args)
