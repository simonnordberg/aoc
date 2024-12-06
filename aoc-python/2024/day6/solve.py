import sys

from util import *


def walk(G, start):
    pos, dir, seen = start, NORTH, set()

    while pos + dir in G and (pos, dir) not in seen:
        seen |= {(pos, dir)}
        while G[pos + dir] == "#":
            dir = {NORTH: EAST, EAST: SOUTH, SOUTH: WEST, WEST: NORTH}[dir]
        pos += dir

    return {pos for pos, _ in seen}, (pos, dir) in seen


G = {
    Point(x, y): c
    for y, line in enumerate(sys.stdin.read().strip().split("\n"))
    for x, c in enumerate(line)
}

start = min(p for p in G if G[p] == "^")
path, _ = walk(G, start)
print(len(path) + 1)
print(sum(walk(G | {p: '#'}, start)[1] for p in path) + 1)
