import argparse
import os
import sys

import requests


def write_to_file(content, filename, debug=False):
    with open(filename, "w") as file:
        file.write(content)
        if debug:
            print(content)


def fetch_input(year, day, cookie):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    response = requests.get(url, cookies={"session": cookie})
    return response.text.strip()


def main():
    cookie = os.getenv("AOC_SESSION")
    if cookie is None or cookie.strip() == "":
        raise ValueError("Session cookie is missing or empty. Check your .env file.")

    parser = argparse.ArgumentParser(description="Fetch Advent of Code puzzle input.")
    parser.add_argument("year", type=int, help="Year of the puzzle")
    parser.add_argument("day", type=int, help="Day of the puzzle (1-25)")
    parser.add_argument(
        "-o", "--output", default="input", help='Output file name (default: "input")'
    )
    args = parser.parse_args()

    if not (1 <= args.day <= 25):
        parser.error("Day must be between 1 and 25")

    write_to_file(fetch_input(args.year, args.day, cookie), args.output, debug=True)


if __name__ == "__main__":
    main()
