from __future__ import annotations

from collections import Counter
from copy import deepcopy
from pathlib import Path

from aoc.util import solution, sign


def solve(data, diagonals=False):
    points = []
    for row in data:
        x1 = int(row.split()[0].split(",")[0])
        y1 = int(row.split()[0].split(",")[1])
        x2 = int(row.split()[2].split(",")[0])
        y2 = int(row.split()[2].split(",")[1])

        if x1 == x2 or y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    points.append((x, y))
        elif diagonals:
            dx = sign(x2-x1)
            dy = sign(y2-y1)

            for x in range(x1, x2 + dx, dx):
                points.append((x, y1))
                y1 += dy

    return len([x for (x, y) in Counter(points).items() if y > 1])


@solution(no=1)
def solve_one(data):
    return solve(data)


@solution(no=2)
def solve_two(data):
    return solve(data, diagonals=True)


def parse_input(file='input'):
    return Path(file).read_text().strip().split("\n")


if __name__ == '__main__':
    data = parse_input("input")
    solve_one(deepcopy(data))
    solve_two(deepcopy(data))
