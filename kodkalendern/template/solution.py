from pathlib import Path

from aoc.util import solution


@solution(no=1)
def solve_one(data):
    pass


def parse_input(file='input'):
    return Path(file).read_text().strip().split("\n")


if __name__ == '__main__':
    data = parse_input()
    solve_one(data)
