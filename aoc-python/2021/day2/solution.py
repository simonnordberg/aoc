from __future__ import annotations

from pathlib import Path

from aoc.util import solution


@solution(no=1)
def solve_one(data):
    horizontal, depth = 0, 0
    for row in data:
        match row.split(" "):
            case "forward", n:
                horizontal += int(n)
            case "down", n:
                depth += int(n)
            case "up", n:
                depth -= int(n)
    return horizontal * depth


@solution(no=2)
def solve_two(data):
    horizontal, depth, aim = 0, 0, 0
    for row in data:
        match row.split(" "):
            case "forward", n:
                horizontal += int(n)
                depth += int(n) * aim
            case "down", n:
                aim += int(n)
            case "up", n:
                aim -= int(n)
    return horizontal * depth


def parse_input(file='input'):
    return Path(file).read_text().strip().split("\n")


if __name__ == '__main__':
    data = parse_input('input')
    solve_one(data)
    solve_two(data)
