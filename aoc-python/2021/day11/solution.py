from __future__ import annotations

from collections import deque
from copy import deepcopy

from aoc.util import solution, read_file, Point, NORTH_WEST, WEST, SOUTH_WEST, SOUTH, SOUTH_EAST, EAST, NORTH_EAST, \
    NORTH

DIRS = [NORTH, NORTH_EAST, EAST, SOUTH_EAST, SOUTH, SOUTH_WEST, WEST, NORTH_WEST]


def solve(xs, steps=100, break_on_all_flash=False):
    grid = {}

    for y in range(0, len(xs)):
        for x in range(0, len(xs[y])):
            grid[Point(x, y)] = (xs[y][x], False)

    flashes = 0

    for n in range(0, steps):
        queue = deque()

        if break_on_all_flash and all(grid[p][1] for p in grid.keys()):
            return flashes, n

        for point in grid.keys():
            e, flashed = grid[point]
            grid[point] = (e, False)
            queue.append(point)

        while queue:
            point = queue.popleft()
            e, flashed = grid[point]
            if not flashed:
                grid[point] = (e + 1, flashed)
                if e + 1 > 9:
                    flashes += 1
                    grid[point] = (0, True)
                    for dir in DIRS:
                        if point + dir in grid:
                            queue.append(point + dir)

    return flashes, None


@solution(no=1)
def solve_one(xs):
    return solve(xs, steps=100, break_on_all_flash=False)[0]


@solution(no=2)
def solve_two(xs):
    return solve(xs, steps=1_000_000, break_on_all_flash=True)[1]


def parse(line):
    return list(map(int, [*line.strip()]))


if __name__ == '__main__':
    _data = list(map(parse, read_file("input")))
    solve_one(deepcopy(_data))
    solve_two(deepcopy(_data))
