from __future__ import annotations

import re

from aoc.util import solution


class Node(object):
    def __init__(self, type, name, size, parent):
        self.type = type
        self.name = name
        self.size = size
        self.parent = parent
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def totalsize(self):
        return sum(c.totalsize() for c in self.children) + self.size

    def __repr__(self) -> str:
        return f"type: {self.type}, " \
               f"name: {self.name}, " \
               f"size: {self.size}, " \
               f"totalsize: {self.totalsize()}, " \
               f"children: {self.children}, " \
               f"parent: {self.parent}"


size_re = re.compile(r"(\d+) ([\w.]+)")


def build_tree(input):
    root = pwd = Node('dir', '/', 0, None)

    for row in input:
        if row == '$ cd /':
            pwd = root
        elif row == '$ cd ..':
            pwd = pwd.parent
        elif row.startswith('$ cd'):
            pwd = Node('dir', row.split("$ cd ")[1], 0, pwd)
            pwd.parent.add_child(pwd)
        elif row == '$ ls':
            pass
        elif row.startswith("dir "):
            pass
        elif size_re.match(row):
            size, file = size_re.match(row).groups()
            pwd.add_child(Node('file', file, int(size), pwd))

    return root


def visit_node(node, callback):
    if node is None:
        return
    callback(node)
    for n in node.children:
        visit_node(n, callback)


@solution(no=1)
def solve_one(input):
    dirs = []
    visit_node(build_tree(input), lambda x: dirs.append(x))
    return sum(filter(lambda x: x < 100000, (d.totalsize() for d in dirs if d.type == 'dir')))


@solution(no=2)
def solve_two(input):
    root = build_tree(input)
    free_space = 70000000 - root.totalsize()
    to_free = 30000000 - free_space

    dirs = []
    visit_node(root, lambda x: dirs.append(x))
    return min(filter(lambda x: x > to_free, (d.totalsize() for d in dirs if d.type == 'dir')))


def parse_input(file='input'):
    return open(file).read().split("\n")


if __name__ == '__main__':
    input = parse_input()
    solve_one(input)
    solve_two(input)
