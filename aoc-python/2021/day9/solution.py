from __future__ import annotations

from collections import deque
from copy import deepcopy

from aoc.util import solution, read_file, Point, NORTH, EAST, SOUTH, WEST

dirs = [NORTH, EAST, SOUTH, WEST]


@solution(no=1)
def solve_one(xs):
    grid = {}
    for y in range(0, len(xs)):
        for x in range(0, len(xs[y])):
            grid[Point(x, y)] = xs[y][x]

    result = 0

    for point in grid:
        if all(point + dir not in grid or
               (point + dir in grid and grid[point] < grid[point + dir])
               for dir in dirs):
            result += 1 + grid[point]

    return result


@solution(no=2)
def solve_two(xs):
    grid = {}
    for y in range(0, len(xs)):
        for x in range(0, len(xs[y])):
            grid[Point(x, y)] = xs[y][x]

    seen = set()
    basins = []

    for point in grid:
        if point in seen or grid[point] == 9:
            continue

        queue = deque()
        queue.append(point)
        size = 0

        while queue:
            point = queue.popleft()
            if point in seen or grid[point] == 9:
                continue

            seen.add(point)
            size += 1

            for dir in dirs:
                nxt = point + dir
                if nxt in grid:
                    queue.append(nxt)

        basins.append(size)

    basins.sort(reverse=True)
    return basins[0] * basins[1] * basins[2]


def parse(line):
    return list(map(int, list(line)))


if __name__ == '__main__':
    _data = list(map(parse, read_file("input")))
    solve_one(deepcopy(_data))
    solve_two(deepcopy(_data))
