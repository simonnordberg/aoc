from __future__ import annotations

import re
from pathlib import Path
from typing import List

from aoc.util import solution, Point, NORTH, EAST, SOUTH, WEST


def solve(rows: List[List[str | None]], instructions: List[str], cube: bool = False) -> int:
    pos = Point(rows[0].index("."), 0)
    dir = EAST
    cubew = len(rows) // 3

    path = {}

    def change_dir(current: Point, ins: str) -> Point:
        if current == NORTH:
            return EAST if ins == "R" else WEST
        elif current == EAST:
            return SOUTH if ins == "R" else NORTH
        elif current == SOUTH:
            return WEST if ins == "R" else EAST
        else:
            return NORTH if ins == "R" else SOUTH

    def debug():
        for y in range(len(rows)):
            for x in range(len(rows[y])):
                c = rows[y][x]
                p = Point(x, y)
                if p in path:
                    c = path[p]
                print(c if c else " ", end='')
            print()

    def wrap(point: Point) -> Point:
        nonlocal rows
        return Point(point.x % len(rows[0]), point.y % len(rows))

    def step(current: Point, steps: int, direction: Point):
        nonlocal rows

        for n in range(steps):
            if cube:  # todo
                target = current + direction
                sqx, sqy = target.x % cubew, target.y % cubew
            else:
                target = wrap(current + direction)
                if rows[target.y][target.x] == ".":  # move is ok
                    current = target
                elif rows[target.y][target.x] == "#":  # hit a wall
                    pass
                elif rows[target.y][target.x] is None:  # wrap around
                    while True:  # find the opposite edge and resume operation there
                        target = wrap(target - direction)
                        if rows[target.y][target.x] is None:  # found the edge, now take a step back and validate move
                            target = wrap(target + direction)
                            if rows[target.y][target.x] == ".":
                                current = target
                            break
                path[current] = {NORTH: "^", SOUTH: "v", EAST: ">", WEST: "<"}[dir]
        return current

    for ins in instructions:
        match ins:
            case "L" | "R":
                dir = change_dir(dir, ins)
                path[pos] = {NORTH: "^", SOUTH: "v", EAST: ">", WEST: "<"}[dir]
            case _:
                pos = step(current=pos, steps=int(ins), direction=dir)
    # debug()
    return 1000 * (pos.y + 1) + 4 * (pos.x + 1) + {EAST: 0, SOUTH: 1, WEST: 2, NORTH: 3}[dir]


@solution(no=1)
def solve_one(rows, instructions):
    return solve(rows, instructions, cube=False)


@solution(no=2)
def solve_two(rows, instructions):
    return solve(rows, instructions, cube=True)


def parse_input(file='input2'):
    board, instructions = Path(file).read_text().split("\n\n")

    ncols = max(len(row) for row in board.split("\n"))
    rows = []
    for row in board.split("\n"):
        rows.append(list(map(lambda x: None if x == " " else x, row.ljust(ncols))))
    return rows, list([x for x in re.split(r"(\d+)", instructions) if x != ""])


if __name__ == '__main__':
    rows, instructions = parse_input()
    solve_one(rows, instructions)
    # solve_two(rows, instructions)
