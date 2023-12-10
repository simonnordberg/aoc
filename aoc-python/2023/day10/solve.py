import sys
from collections import deque

from util import *

INPUT = sys.stdin.read().strip().split("\n")

G = {}
for y in range(len(INPUT)):
    for x in range(len(INPUT[y])):
        G[Point(x, y)] = INPUT[y][x]

S = [k for k, v in G.items() if v == "S"]


def print_graph(G):
    for y in range(max(p.y for p in G)):
        for x in range(max(p.x for p in G)):
            print(G[Point(x, y)], end="")
        print()


def furthest_node(G, start):
    node, distance = start, 0

    seen = set()
    seen.add(node)
    Q = deque([(node, distance)])

    while Q:
        node, distance = Q.popleft()

        neighbours = []
        if node + NORTH in G and G[node + NORTH] in ["|", "F", "7"]:
            neighbours.append(node + NORTH)
        if node + EAST in G and G[node + EAST] in ["-", "7", "J"]:
            neighbours.append(node + EAST)
        if node + SOUTH in G and G[node + SOUTH] in ["|", "L", "J"]:
            neighbours.append(node + SOUTH)
        if node + WEST in G and G[node + WEST] in ["-", "L", "F"]:
            neighbours.append(node + WEST)

        for t in neighbours:
            if t not in seen:
                seen.add(t)
                Q.append((t, distance + 1))

    return node, distance


print("p1:", furthest_node(G, S[0])[1])
