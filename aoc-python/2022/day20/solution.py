from __future__ import annotations

from collections import deque
from pathlib import Path

from aoc.util import solution


def solve(nums, key=1, times=1):
    pairs = [(i, v * key) for i, v in enumerate(nums)]
    queue = deque(pairs)
    for _ in range(times):
        for i, v in pairs:
            queue.rotate(-queue.index((i, v)))
            queue.popleft()
            queue.rotate(-v % len(queue))
            queue.appendleft((i, v))
    values = [v for k, v in queue]
    return sum(values[(values.index(0) + n) % len(values)] for n in (1000, 2000, 3000))


@solution(no=1)
def solve_one(nums):
    return solve(nums)


@solution(no=2)
def solve_two(nums):
    return solve(nums, key=811589153, times=10)


def parse_input(file='input'):
    return list(map(int, Path(file).read_text().strip().split("\n")))


if __name__ == '__main__':
    lines = parse_input()
    solve_one(lines)
    solve_two(lines)
