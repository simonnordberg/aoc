from __future__ import annotations

from pathlib import Path

from aoc.util import solution


@solution(no=1)
def solve_one(lines):
    pass


@solution(no=2)
def solve_two(lines):
    pass


def parse_input(file='input'):
    return Path(file).read_text().strip().split("\n")


if __name__ == '__main__':
    lines = parse_input()
    solve_one(lines)
    solve_two(lines)
