from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path

from aoc.util import solution, transpose, flatten


@dataclass
class Item:
    value: int
    marked: bool = False


@dataclass
class Board:
    items: list[list[Item]]
    solved: bool = False

    def mark_value(self, value):
        for j in range(0, len(self.items)):
            for i in range(0, len(self.items[j])):
                if self.items[j][i].value == value:
                    self.items[j][i].marked = True

    def check_horizontal(self):
        for r in self.items:
            if all(x.marked for x in r):
                return True
        return False

    def check_vertical(self):
        for r in transpose(self.items):
            if all(x.marked for x in r):
                return True
        return False

    def check_bingo(self):
        return self.check_vertical() or self.check_horizontal()

    def sum_unmarked(self):
        return sum(x.value for x in flatten(self.items) if not x.marked)


def solve(lines):
    solves = []

    draws = map(int, lines[0].split(","))
    boards = []
    for line in range(1, len(lines)):
        cols = list(map(int, lines[line].split()))
        if len(cols) == 0:
            boards.append(Board(items=[]))
        else:
            boards[-1].items.append([Item(value=col) for col in cols])

    for draw in draws:
        for board in boards:
            if not board.solved:
                board.mark_value(draw)
                if board.check_bingo():
                    board.solved = True
                    solves.append(draw * board.sum_unmarked())

    return solves


@solution(no=1)
def solve_one(lines):
    return solve(lines)[0]


@solution(no=2)
def solve_two(lines):
    return solve(lines)[-1]


def parse_input(file='input'):
    return Path(file).read_text().strip().split("\n")


# Bingo
if __name__ == '__main__':
    data = parse_input("input")
    solve_one(deepcopy(data))
    solve_two(deepcopy(data))
