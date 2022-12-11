from __future__ import annotations

from pathlib import Path

from aoc.util import solution


def solve(lines, callback):
    X, cycle = 1, 0
    for line in lines:
        instr, value, *_ = line.split() + [None]

        instr_len = 2 if instr == "addx" else 1
        for _ in range(instr_len):
            callback(cycle, X)
            cycle += 1

        if instr == "addx":
            X += int(value)


@solution(no=1)
def solve_one(lines):
    def callback(cycle, X):
        if cycle + 1 in [20, 60, 100, 140, 180, 220]:
            signals.append((cycle + 1) * X)

    signals = []
    solve(lines, callback)
    return sum(signals)


@solution(no=2)
def solve_two(lines):
    def callback(cycle, X):
        row, col = cycle // 40, cycle % 40
        screen[row] += "#" if col in [X - 1, X, X + 1] else "."

    screen = [""] * 6
    solve(lines, callback)
    [print(row) for row in screen]
    return None


def parse_input(file='input'):
    return Path(file).read_text().strip().split("\n")


if __name__ == '__main__':
    lines = parse_input()
    solve_one(lines)
    solve_two(lines)
