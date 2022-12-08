from __future__ import annotations

from aoc.util import solution


@solution(no=1)
def solve_one(input):
    pass


@solution(no=2)
def solve_two(input):
    pass


def parse_input(file='input'):
    return open(file).read().split("\n")


if __name__ == '__main__':
    input = parse_input()
    solve_one(input)
    solve_two(input)
