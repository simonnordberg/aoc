from __future__ import annotations

from copy import deepcopy

from aoc.util import solution, read_file, ints


@solution(no=1)
def solve_one(data):
    pass


@solution(no=2)
def solve_two(data):
    pass


def parse(line):
    return ints(line.strip())


if __name__ == '__main__':
    data = list(map(parse, read_file("input")))
    solve_one(deepcopy(data))
    solve_two(deepcopy(data))
