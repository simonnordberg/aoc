import sys

INPUT = sys.stdin.read().strip()


def print_grid(G):
    for y in range(len(G)):
        print("".join(G[y]))
    print()


def rotate(G):
    return [list(x) for x in zip(*G[::-1])]


def slide(G):
    w, h = G[0], len(G)
    for x in range(len(w)):
        for _ in range(h):
            for y in range(h):
                if y > 0 and G[y - 1][x] == "." and G[y][x] == "O":
                    G[y - 1][x] = "O"
                    G[y][x] = "."
    return G


def score(G):
    result = 0
    h = len(G)
    for y in range(len(G)):
        for x in range(len(G[0])):
            if G[y][x] == "O":
                result += h - y
    return result


G = [[c for c in line] for line in INPUT.split("\n")]
print("p1:", score(slide(G)))

CACHE = {}
target = 1_000_000_000
t = 0
while t < target:
    t += 1
    for _ in range(4):
        G = rotate(slide(G))

    # Detect cycle and ffwd
    key = tuple(item for row in G for item in row)
    if key in CACHE:
        cycle = t - CACHE[key]
        skip = (target - t) // cycle
        t += skip * cycle
    CACHE[key] = t
print("p2:", score(G))
