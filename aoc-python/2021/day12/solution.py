from __future__ import annotations

from collections import Counter
from copy import deepcopy
from dataclasses import dataclass, field
from typing import List, Set

from aoc.util import solution, read_file


@dataclass
class Node:
    name: str
    neighbours: Set[Node] = field(default_factory=lambda: set())

    def __eq__(self, other: Node) -> bool:
        return isinstance(other, Node) and self.name == other.name

    def __repr__(self) -> str:
        return f"{self.name} -> {','.join(map(lambda x: x.name, self.neighbours))}"

    def __hash__(self) -> int:
        return hash(self.__repr__())


def find_all_paths(nodes: List[Node], start: Node, end: Node, path=None, allow_some_revisit=False):
    if path is None:
        path = []

    path = path + [start]

    if start == end:
        return [path]

    paths = []
    for node in start.neighbours:
        if allow_some_revisit:
            if node.name in ["start"]:
                continue

            c = Counter(path)

            small_cave_visited = any([k for k, v in c.items() if k.name.islower() and v > 1])
            if node.name.islower() and small_cave_visited and node in path:
                continue

            for p in find_all_paths(nodes, node, end, path, allow_some_revisit):
                paths.append(p)
        else:
            if node not in path or node.name.isupper():
                for p in find_all_paths(nodes, node, end, path):
                    paths.append(p)

    return paths


def find_node(nodes, name):
    for node in nodes:
        if node.name == name:
            return node
    return None


def create_nodes(edges):
    nodes = []

    for x1, x2 in edges:
        n1 = find_node(nodes, x1)
        if n1 is None:
            n1 = Node(x1)
            nodes.append(n1)

        n2 = find_node(nodes, x2)
        if n2 is None:
            n2 = Node(x2)
            nodes.append(n2)

        n1.neighbours.add(n2)
        n2.neighbours.add(n1)

    return nodes


@solution(no=1)
def solve_one(edges):
    nodes = create_nodes(edges)
    paths = find_all_paths(
        nodes,
        find_node(nodes, "start"),
        find_node(nodes, "end"),
        None,
        False
    )
    return len(paths)


@solution(no=2)
def solve_two(edges):
    nodes = create_nodes(edges)
    paths = find_all_paths(
        nodes,
        find_node(nodes, "start"),
        find_node(nodes, "end"),
        None,
        True
    )
    return len(paths)


def parse(line):
    return line.strip().split("-")


# Day 12: Passage Pathing
if __name__ == '__main__':
    _data = list(map(parse, read_file("input")))
    solve_one(deepcopy(_data))
    solve_two(deepcopy(_data))
