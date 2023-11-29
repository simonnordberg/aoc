import argparse
import os
import requests


def validate_session_cookie(cookie):
    if cookie is None or cookie.strip() == "":
        raise ValueError("Session cookie is missing or empty. Check your .env file.")


def write_to_file(content, filename):
    with open(filename, 'w') as file:
        file.write(content)


def fetch_input(year, day, cookie):
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    response = requests.get(url, cookies={'session': cookie})
    return response.text


def main():
    session_cookie = os.getenv('AOC_SESSION')
    validate_session_cookie(session_cookie)

    parser = argparse.ArgumentParser(description='Fetch Advent of Code puzzle input.')
    parser.add_argument('year', type=int, help='Year of the puzzle')
    parser.add_argument('day', type=int, help='Day of the puzzle (1-25)')
    parser.add_argument('-o', '--output', default='input', help='Output file name (default: "input")')
    args = parser.parse_args()

    if not (1 <= args.day <= 25):
        parser.error("Day must be between 1 and 25")

    inp = fetch_input(args.year, args.day, session_cookie)
    write_to_file(inp, args.output)


if __name__ == "__main__":
    main()
