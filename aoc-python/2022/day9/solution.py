from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from aoc.util import solution


@dataclass
class Point:
    x: int
    y: int

    def move(self, dir: str):
        match dir:
            case 'R':
                self.x += 1
            case 'U':
                self.y += 1
            case 'L':
                self.x -= 1
            case 'D':
                self.y -= 1

    def follow(self, other: 'Point'):
        dx = other.x - self.x
        dy = other.y - self.y

        if abs(dx) <= 1 and abs(dy) <= 1:
            return

        self.x += int(dx / abs(dx)) if abs(dx) > 0 else 0
        self.y += int(dy / abs(dy)) if abs(dy) > 0 else 0

    def __hash__(self):
        return hash(repr(self))


def solve(rows: [int], n: int) -> int:
    knots = [Point(0, 0) for _ in range(n)]
    visited = set()

    for line in rows:
        dir, steps = line.split()

        for _ in range(int(steps)):
            knots[0].move(dir)
            for leader, follower in zip(knots, knots[1:]):
                follower.follow(leader)

            visited.add(knots[-1])

    return len(visited)


@solution(no=1)
def solve_one(rows: [str]) -> int:
    return solve(rows, 2)


@solution(no=2)
def solve_two(rows: [str]) -> int:
    return solve(rows, 10)


def parse_input(file='input'):
    return Path(file).read_text().strip().split("\n")


if __name__ == '__main__':
    rows = parse_input()
    solve_one(rows)
    solve_two(rows)
