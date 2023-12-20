import sys
from collections import defaultdict
from typing import List, Tuple

INPUT = sys.stdin.read().strip()
DIRS = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}


def solve(start: List[Tuple[int, int]]):
    grid = defaultdict(int)
    for p in start:
        grid[p] += 1
    for i, x in enumerate(INPUT):
        pos = start[i % len(start)]
        pos = tuple(a + b for a, b in zip(pos, DIRS[x]))
        grid[pos] += 1
        start[i % len(start)] = pos
    return sum(v > 0 for v in grid.values())


p1 = solve([(0, 0)])
print("p1:", p1)

p2 = solve([(0, 0), (0, 0)])
print("p2:", p2)

assert p1 == 2081
assert p2 == 2341
