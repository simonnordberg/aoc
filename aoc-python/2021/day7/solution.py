from __future__ import annotations

from copy import deepcopy

from aoc.util import solution, read_file, ints


@solution(no=1)
def solve_one(ll):
    ll.sort()
    mid = ll[len(ll) // 2]
    return sum(abs(l - mid) for l in ll)


@solution(no=2)
def solve_two(ll):
    return min(sum(cost(abs(x - l)) for l in ll) for x in range(min(ll), max(ll)))


def cost(n):
    return (n * (n + 1)) // 2


def parse(line):
    return ints(line.strip())


if __name__ == '__main__':
    data = list(map(parse, read_file("input")))[0]
    solve_one(deepcopy(data))
    solve_two(deepcopy(data))
