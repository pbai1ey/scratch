#!/usr/bin/env python3
import sys
from monkey import Monkey


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: script.py <name>")
        return 1

    name = sys.argv[1]

    age = input("Enter monkey's age: ")
    favorite_food = input("Enter monkey's favorite food: ")

    monkey = Monkey(name, age, favorite_food)
    print(monkey)

    return 0


if __name__ == "__main__":
    sys.exit(main())
