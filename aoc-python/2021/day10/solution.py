from __future__ import annotations

from collections import deque
from copy import deepcopy

from aoc.util import solution, read_file

CORRUPT_SCORES = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

INCOMPLETE_SCORES = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

PAIRS = {
    "{": "}",
    "(": ")",
    "[": "]",
    "<": ">",
}


def solve(xs):
    corrupt_score = 0
    incomplete_scores = []

    for line in xs:
        corrupt = False
        queue = deque()
        for char in line:
            assert char in PAIRS.keys() or char in PAIRS.values()
            if char in PAIRS.keys():
                queue.append(char)
            elif char in PAIRS.values():
                top = queue.pop()
                expected = PAIRS[top]
                if expected != char:
                    # print("expected {}, but found {} instead".format(expected, char))
                    corrupt_score += CORRUPT_SCORES[char]
                    corrupt = True
                    break

        if corrupt:
            continue

        incomplete_score = 0
        while queue:
            top = queue.pop()
            expected = PAIRS[top]
            incomplete_score *= 5
            incomplete_score += INCOMPLETE_SCORES[expected]
        incomplete_scores.append(incomplete_score)
    return corrupt_score, incomplete_scores


@solution(no=1)
def solve_one(xs):
    return solve(xs)[0]


@solution(no=2)
def solve_two(xs):
    scores = solve(xs)[1]
    scores.sort()
    return scores[len(scores) // 2]


def parse(line):
    return [*line.strip()]


if __name__ == '__main__':
    _data = list(map(parse, read_file("input")))
    solve_one(deepcopy(_data))
    solve_two(deepcopy(_data))
