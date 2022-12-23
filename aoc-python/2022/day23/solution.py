from __future__ import annotations

from collections import deque
from pathlib import Path
from typing import List

from aoc.util import *
from aoc.util import Point

ALL_DIRECTIONS = [NORTH, NORTH_EAST, EAST, SOUTH_EAST, SOUTH, SOUTH_WEST, WEST, NORTH_WEST]


def simulate(grid: set[Point], rounds=10, break_when_gridlocked=False) -> int | None:
    directions = deque([[NORTH, NORTH_EAST, NORTH_WEST],
                        [SOUTH, SOUTH_EAST, SOUTH_WEST],
                        [WEST, NORTH_WEST, SOUTH_WEST],
                        [EAST, NORTH_EAST, SOUTH_EAST]])

    def has_neighbours(elf: Point) -> bool:
        return any(elf + d in grid for d in ALL_DIRECTIONS)

    def propose_move(elf: Point, dirs: deque[list[Point]]) -> Point | None:
        for d1, d2, d3 in dirs:
            if not any(elf + d in grid for d in [d1, d2, d3]):
                return elf + d1
        return None

    def debug(round: int):
        x_min, y_min = min(grid, key=lambda p: p.x).x, min(grid, key=lambda p: p.y).y
        x_max, y_max = max(grid, key=lambda p: p.x).x, max(grid, key=lambda p: p.y).y

        print(f"> Round: {round + 1}")
        for y in range(y_min, y_max + 1):
            for x in range(x_min, x_max + 1):
                point = Point(x, y)
                print('#' if point in grid else '.', end='')
            print()
        print(f"< Round: {round + 1}")

    # debug(-1)

    for i in range(rounds):
        proposed_moves: dict[Point, List[Point]] = {}
        for elf in grid:
            if not has_neighbours(elf):
                continue

            move = propose_move(elf, directions)
            if not move:
                continue

            if move in proposed_moves:
                proposed_moves[move].append(elf)
            else:
                proposed_moves[move] = [elf]

        if break_when_gridlocked and len(proposed_moves) == 0:
            return i + 1

        for target, elves in [(target, elves)
                              for target, elves in proposed_moves.items() if len(elves) == 1]:
            grid.remove(elves[0])
            grid.add(target)

        directions.rotate(-1)
        # debug(i)

    x_min, y_min = min(grid, key=lambda p: p.x).x, min(grid, key=lambda p: p.y).y
    x_max, y_max = max(grid, key=lambda p: p.x).x, max(grid, key=lambda p: p.y).y

    if break_when_gridlocked:
        return None
    return ((1 + x_max - x_min) * (1 + y_max - y_min)) - len(grid)


@solution(no=1)
def solve_one(grid):
    return simulate(grid=grid, rounds=10)


@solution(no=2)
def solve_two(grid):
    return simulate(grid=grid, rounds=2000, break_when_gridlocked=True)


def parse_input(file='input'):
    grid = set()
    for y, row in enumerate(Path(file).read_text().strip().split("\n")):
        for x, col in enumerate(row):
            if col == "#":
                grid.add(Point(x, y))
    return grid


if __name__ == '__main__':
    solve_one(parse_input())
    solve_two(parse_input())
