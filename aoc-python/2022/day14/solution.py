from __future__ import annotations

from pathlib import Path

from aoc.util import solution

SAND_ORIGIN = (500, 0)
ROCK = "#"
SAND = "o"
ORIGIN = "+"


def solve(cave, abyss_depth, cave_depth=None, target=None):
    while True:
        sx, sy = SAND_ORIGIN
        while True:
            if cave_depth is not None:
                cave[(sx, cave_depth)] = ROCK
                cave[(sx - 1, cave_depth)] = ROCK
                cave[(sx + 1, cave_depth)] = ROCK

            if sy > abyss_depth:
                print(f"Hit the abyss at depth {abyss_depth}")
                return sum(1 for v in cave.values() if v == SAND)

            if (sx, sy + 1) not in cave:  # down
                sy += 1
                continue

            if (sx - 1, sy + 1) not in cave:  # down-left
                sx -= 1
                sy += 1
                continue

            if (sx + 1, sy + 1) not in cave:  # down-right
                sx += 1
                sy += 1
                continue

            cave[(sx, sy)] = SAND

            if target is not None and (sx, sy) == target:
                return sum(1 for v in cave.values() if v == SAND)

            break


@solution(no=1)
def solve_one(cave):
    abyss_depth = max({k: v for k, v in cave.items() if v == ROCK}, key=lambda x: x[1])[1] + 1
    return solve(cave, abyss_depth=abyss_depth)


@solution(no=2)
def solve_two(cave):
    cave_floor = max({k: v for k, v in cave.items() if v == ROCK}, key=lambda x: x[1])[1] + 2
    return solve(cave, abyss_depth=cave_floor+1, cave_depth=cave_floor, target=(500, 0))


def parse_input(file='input'):
    cave = {SAND_ORIGIN: ORIGIN}

    for line in Path(file).read_text().strip().split("\n"):
        waypoints = []
        for point in line.strip().split("->"):
            px, py = point.strip().split(",")
            waypoints.append((int(px), int(py)))

        for w in range(len(waypoints) - 1):
            x1, y1 = waypoints[w]
            x2, y2 = waypoints[w + 1]
            dx, dy = x2 - x1, y2 - y1
            if dx != 0:
                step = int(dx / abs(dx))
                for x in range(x1, x1 + dx + step, step):
                    cave[(int(x), int(y1))] = ROCK
            if dy != 0:
                step = int(dy / abs(dy))
                for y in range(y1, y1 + dy + step, step):
                    cave[(int(x1), int(y))] = ROCK

    return cave


if __name__ == '__main__':
    solve_one(parse_input())
    solve_two(parse_input())
