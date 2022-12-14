from __future__ import annotations

from itertools import pairwise
from pathlib import Path

from aoc.util import solution, Point, sign, SOUTH, SOUTH_WEST, SOUTH_EAST

SAND_ORIGIN = Point(500, 0)
ROCK = "#"
SAND = "o"
ORIGIN = "+"


def solve(cave, abyss_depth, cave_depth=None, target=None):
    while True:
        grain = SAND_ORIGIN
        while True:
            if cave_depth is not None:
                cave[Point(grain.x, cave_depth)] = ROCK
                cave[Point(grain.x - 1, cave_depth)] = ROCK
                cave[Point(grain.x + 1, cave_depth)] = ROCK

            if grain.y > abyss_depth:
                return sum(1 for v in cave.values() if v == SAND)

            if grain + SOUTH not in cave:
                grain += SOUTH
                continue

            if grain + SOUTH_WEST not in cave:
                grain += SOUTH_WEST
                continue

            if grain + SOUTH_EAST not in cave:
                grain += SOUTH_EAST
                continue

            cave[grain] = SAND

            if target is not None and grain == target:
                return sum(1 for v in cave.values() if v == SAND)

            break


def max_depth(cave) -> int:
    return max({k: v for k, v in cave.items() if v == ROCK}, key=lambda k: k.y).y


@solution(no=1)
def solve_one(cave):
    return solve(cave, abyss_depth=max_depth(cave) + 1)


@solution(no=2)
def solve_two(cave):
    depth = max_depth(cave)
    return solve(cave, abyss_depth=depth + 3, cave_depth=depth + 2, target=Point(500, 0))


def parse_input(file='input'):
    cave = {SAND_ORIGIN: ORIGIN}

    for line in Path(file).read_text().strip().split("\n"):
        waypoints = [Point(int(px), int(py))
                     for px, py in (point.split(',')
                                    for point in line.split('->'))]
        for src, dst in pairwise(waypoints):
            cave[src] = ROCK
            while src != dst:
                src += Point(sign(dst.x - src.x), sign(dst.y - src.y))
                cave[src] = ROCK
    return cave


if __name__ == '__main__':
    solve_one(parse_input())
    solve_two(parse_input())
