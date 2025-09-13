import argparse

from .submit import configure_parser as configure_submit_parser


def main():
    """st-tools CLI entry point."""
    parser = argparse.ArgumentParser(description="st-tools CLI")
    subparsers = parser.add_subparsers(dest="command", help="sub-command help")
    subparsers.required = True

    # Configure subparsers for each command
    configure_submit_parser(subparsers)

    args = parser.parse_args()

    # Execute the command
    args.func(args)


if __name__ == "__main__":
    main()
