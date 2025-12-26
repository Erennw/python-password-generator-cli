#!/usr/bin/env python3

import argparse
import random
import string


def generate_password(length: int, use_digits: bool, use_symbols: bool) -> str:
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("No characters available to generate password.")

    return "".join(random.choice(characters) for _ in range(length))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Simple Python CLI tool to generate secure passwords."
    )

    parser.add_argument(
        "-l", "--length",
        type=int,
        default=12,
        help="Length of the password (default: 12)"
    )
    parser.add_argument(
        "--digits",
        action="store_true",
        help="Include digits in the password"
    )
    parser.add_argument(
        "--symbols",
        action="store_true",
        help="Include symbols in the password"
    )

    args = parser.parse_args()

    try:
        password = generate_password(
            length=args.length,
            use_digits=args.digits,
            use_symbols=args.symbols
        )
        print(f"Generated password: {password}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
