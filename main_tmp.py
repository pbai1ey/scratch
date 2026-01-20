#!/usr/bin/env python3
import sys


def main(args):
    """Main entry point."""
    if len(args) < 2:
        print("Usage: script.py <arg>")
        return 1

    print(f"Argument: {args[1]}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
