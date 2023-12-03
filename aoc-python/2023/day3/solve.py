import re
import sys
from collections import defaultdict
from copy import copy
from math import prod

from util import *


def solve(grid):
    parts = defaultdict(int)
    gears = defaultdict(set)

    for p in grid:
        n = grid[p]
        if n.isnumeric():
            for dx in range(0, len(n)):
                cursor = Point(p.x + dx, p.y)
                for dir in DIRECTIONS:
                    scan = cursor + dir
                    if scan in grid and not grid[scan].isdigit():
                        parts[p] = int(n)
                        if grid[scan] == "*":
                            gears[scan].add(p)

    return (sum(parts.values()),
            sum(prod(int(grid[p]) for p in gear) for gear in gears.values() if len(gear) == 2))


@solution(no=1)
def solve_one(grid):
    return solve(grid)[0]


@solution(no=2)
def solve_two(grid):
    return solve(grid)[1]


if __name__ == '__main__':
    grid = {}
    for y, line in enumerate(sys.stdin.read().split("\n")):
        for m in re.finditer(r"[0-9]+", line):
            grid[Point(m.start(), y)] = m.group(0)
        for m in re.finditer(r"[^0-9.]", line):
            grid[Point(m.start(), y)] = m.group(0)

    solve_one(copy(grid))
    solve_two(copy(grid))
