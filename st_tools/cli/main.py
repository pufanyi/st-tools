import argparse
import sys

from .submit import submit


def main():
    """st-tools CLI entry point."""
    parser = argparse.ArgumentParser(description="st-tools CLI")
    subparsers = parser.add_subparsers(dest="command", help="sub-command help")
    subparsers.required = True

    args = parser.parse_args()

    if args.command == "submit":
        submit(args)
    else:
        print(f"Unknown command: {args.command}")
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
