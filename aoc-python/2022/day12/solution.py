from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from aoc.util import solution


@dataclass
class Node:
    x: int
    y: int
    value: int
    visited: int = False
    parent: Node = None

    def __eq__(self, other: Node) -> bool:
        return isinstance(other, Node) and self.x == other.x and self.y == other.y

    def __repr__(self) -> str:
        if self.parent:
            return f"({self.x}, {self.y}) -> ({self.parent.x}, {self.parent.y})"
        else:
            return f"({self.x}, {self.y}) -> (None)"


class Queue(object):
    def __init__(self):
        self.items: [Node] = []

    def push(self, elm: Node):
        self.items.append(elm)

    def dequeue(self) -> Node:
        return self.items.pop(0)

    def empty(self) -> bool:
        return len(self.items) == 0

    def __repr__(self) -> str:
        return f"{self.items}"


def get_neighbours(rows, node: Node) -> [Node]:
    neighbours = []
    if node.y > 0 and rows[node.y - 1][node.x].value - node.value <= 1:
        neighbours.append(rows[node.y - 1][node.x])
    if node.x < len(rows[node.y]) - 1 and rows[node.y][node.x + 1].value - node.value <= 1:
        neighbours.append(rows[node.y][node.x + 1])
    if node.y < len(rows) - 1 and rows[node.y + 1][node.x].value - node.value <= 1:
        neighbours.append(rows[node.y + 1][node.x])
    if node.x > 0 and rows[node.y][node.x - 1].value - node.value <= 1:
        neighbours.append(rows[node.y][node.x - 1])
    return list(filter(lambda x: not x.visited, neighbours))


def solve(rows, starts: [Node], end: Node):
    routes = []

    for start in starts:
        for y in range(len(rows)):
            for x in range(len(rows[y])):
                rows[y][x].visited = False
                rows[y][x].parent = None

        queue = Queue()
        start.visited = True
        queue.push(start)

        while not queue.empty():
            n = queue.dequeue()
            if n == end:
                break

            for neighbour in get_neighbours(rows, n):
                neighbour.visited = True
                neighbour.parent = n
                queue.push(neighbour)

        node = end
        steps = []
        while node is not None:
            steps.append(node)
            node = node.parent

        routes.append(len(steps) - 1)

    return min(filter(lambda x: x > 0, routes))


@solution(no=1)
def solve_one(rows, starts: [Node], end: Node):
    return solve(rows, starts, end)


@solution(no=2)
def solve_two(rows, starts: [Node], end: Node):
    return solve(rows, starts, end)


START_NODE = ord('S') - ord('a')
END_NODE = ord('E') - ord('a')
LOWEST_ELEVATION = ord('a') - ord('a')
HIGHEST_ELEVATION = ord('z') - ord('a')


def parse_input(file='input', multiple_starts=False) -> ([[Node]], [Node], Node):
    rows = []
    for y, row in enumerate(Path(file).read_text().strip().split("\n")):
        rows.append([])
        for x, col in enumerate(row):
            rows[y].append(Node(x, y, ord(col) - ord('a')))

    starts, end = [], None
    for y in range(len(rows)):
        for x in range(len(rows[y])):
            if rows[y][x].value == START_NODE:
                starts.append(rows[y][x])
            elif multiple_starts and rows[y][x].value == LOWEST_ELEVATION:
                starts.append(rows[y][x])
            elif rows[y][x].value == END_NODE:
                end = rows[y][x]

    for start in starts:
        start.value = LOWEST_ELEVATION
    end.value = HIGHEST_ELEVATION
    return rows, starts, end


if __name__ == '__main__':
    rows, starts, end = parse_input()
    solve_one(rows, starts, end)

    rows, starts, end = parse_input(multiple_starts=True)
    solve_two(rows, starts, end)
