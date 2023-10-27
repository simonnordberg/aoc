from __future__ import annotations

from collections import defaultdict, deque
from copy import deepcopy

from aoc.util import solution, read_file


def solve(graph: dict[list], allow_some_revisit: bool):
    queue = deque()
    queue.append(["start"])

    paths = []

    while queue:
        path = queue.popleft()
        start = path[-1]

        for node in graph[start]:
            if allow_some_revisit:
                if node == "start":
                    continue

                if node.islower():
                    # not allowed to visit more than one small cave/node twice
                    visited = [p for p in path if p.islower()]
                    if node in path and len(set(visited)) != len(visited):
                        continue
            else:
                if node in path and node.islower():
                    continue

            npath = path + [node]
            if node == "end":
                paths.append(npath)
            else:
                queue.append(npath)

    return len(paths)


@solution(no=1)
def solve_one(graph):
    return solve(graph, False)


@solution(no=2)
def solve_two(graph):
    return solve(graph, True)


def parse(line):
    return line.strip().split("-")


# Day 12: Passage Pathing
if __name__ == '__main__':
    xs = list(map(parse, read_file("input")))
    graph = defaultdict(list)
    for e1, e2 in xs:
        graph[e1].append(e2)
        graph[e2].append(e1)

    solve_one(deepcopy(graph))
    solve_two(deepcopy(graph))
