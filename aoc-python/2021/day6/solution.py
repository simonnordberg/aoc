from __future__ import annotations

from collections import defaultdict
from copy import deepcopy

from aoc.util import solution, read_file, ints


def solve(data, days):
    curr = defaultdict(int)
    for k in data:
        curr[k] += 1

    for _ in range(days):
        nxt = defaultdict(int)
        for k, v in curr.items():
            if k == 0:
                nxt[6] += v
                nxt[8] += v
            else:
                nxt[k - 1] += v
        curr = nxt
    return sum(curr.values())


@solution(no=1)
def solve_one(data):
    return solve(data, 80)


@solution(no=2)
def solve_two(data):
    return solve(data, 256)


def parse(line):
    return ints(line.strip())


if __name__ == '__main__':
    data = parse(read_file("input")[0])
    solve_one(deepcopy(data))
    solve_two(deepcopy(data))
