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


def DFS(G, v, seen=None, path=None):
    if seen is None:
        seen = []
    if path is None:
        path = [v]

    seen.append(v)

    paths = []

    if v + NORTH in G and G[v + NORTH] in ["|", "F"]:
        tmp.append(v + NORTH)
    if v + EAST in G and G[v + EAST] in ["-", "7", "J"]:
        tmp.append(v + EAST)
    if v + SOUTH in G and G[v + SOUTH] in ["|", "L", "J"]:
        tmp.append(v + SOUTH)
    if v + WEST in G and G[v + WEST] in ["-", "L", "F"]:
        tmp.append(v + WEST)
    for t in tmp:
        if t not in seen:
            tpath = path + [t]
            paths.append(tuple(tpath))
            paths.extend(DFS(G, t, seen, tpath))

    return paths


def furthest_node(G, start):
    seen = set()
    Q = deque([start])
    seen.add(start)

    while Q:
        node = Q.popleft()

        neighbours = []
        if node + NORTH in G and G[node + NORTH] in ["|", "F"]:
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
                Q.append(t)

        

paths = DFS(G, S[0])
print_graph(G)
for p in paths:
    print(p)
print(max(len(p) for p in paths))
