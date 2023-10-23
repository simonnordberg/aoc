from __future__ import annotations

from copy import deepcopy
from pathlib import Path

from aoc.util import solution


@solution(no=1)
def solve_one(data):
    pass


@solution(no=2)
def solve_two(data):
    pass


def parse_input(file='input'):
    return Path(file).read_text().strip().split("\n")


if __name__ == '__main__':
    data = parse_input("input")
    solve_one(deepcopy(data))
    solve_two(deepcopy(data))
