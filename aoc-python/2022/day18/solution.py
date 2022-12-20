from __future__ import annotations

from pathlib import Path

from aoc.util import solution


def adjacent(x, y, z) -> (int, int, int):
    return {(x + 1, y, z), (x - 1, y, z),
            (x, y + 1, z), (x, y - 1, z),
            (x, y, z + 1), (x, y, z - 1)}


@solution(no=1)
def solve_one(cubes):
    grid = {tuple(c) for c in cubes}
    return 6 * len(cubes) - sum(1 for cube in cubes for a in adjacent(*cube) if a in grid)


@solution(no=2)
def solve_two(cubes):
    pass


def parse_input(file='input'):
    return [(x, y, z) for x, y, z in (map(int, row.split(',')) for row in Path(file).read_text().strip().split("\n"))]


if __name__ == '__main__':
    cubes = parse_input()
    solve_one(cubes)
    solve_two(cubes)
