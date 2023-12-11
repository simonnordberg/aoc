import sys
from itertools import combinations

INPUT = sys.stdin.read().strip().split("\n")


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


G = [[col for col in row] for row in INPUT]
N_ROWS = len(G)
N_COLS = len(G[0])

empty_rows = [y for y in range(N_ROWS) if all(G[y][x] != "#" for x in range(N_COLS))]
empty_cols = [x for x in range(N_COLS) if all(G[y][x] != "#" for y in range(N_ROWS))]
pairs = [(x, y) for y in range(N_ROWS) for x in range(N_COLS) if G[y][x] == "#"]


for part, scale_factor in [("p1", 2 - 1), ("p2", int(1e6 - 1))]:
    dist = []
    for (x1, y1), (x2, y2) in combinations(pairs, 2):
        d = manhattan_distance(x1, y1, x2, y2)
        d += scale_factor * sum(min(y1, y2) <= er <= max(y1, y2) for er in empty_rows)
        d += scale_factor * sum(min(x1, x2) <= ec <= max(x1, x2) for ec in empty_cols)
        dist.append(d)
    assert sum(dist) == (10490062 if part == "p1" else 382979724122)
    print(f"{part}:", sum(dist))
