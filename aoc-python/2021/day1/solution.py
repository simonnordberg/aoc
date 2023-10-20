from __future__ import annotations

from pathlib import Path

from aoc.util import solution


@solution(no=1)
def solve_one(data):
    return sum(data[d + 1] > data[d] for d in range(len(data) - 1))


@solution(no=2)
def solve_two(data):
    return sum(sum(data[i + 1:i + 4]) > sum(data[i:i + 3]) for i in range(len(data) - 3))


def parse_input(file='input'):
    return list(map(int, Path(file).read_text().strip().split("\n")))


if __name__ == '__main__':
    data = parse_input('input')
    solve_one(data)
    solve_two(data)
