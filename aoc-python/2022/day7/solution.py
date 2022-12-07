from __future__ import annotations

import re

from aoc.util import solution


class Node(object):
    parent: Node
    children: []
    name: str
    size: int
    type: str

    def __init__(self, type, name, size, parent):
        self.type = type
        self.name = name
        self.size = size
        self.parent = parent
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def totalsize(self):
        return sum([c.totalsize() for c in self.children]) + self.size

    def __repr__(self) -> str:
        return f"type: {self.type}, " \
               f"name: {self.name}, " \
               f"size: {self.size}, " \
               f"totalsize: {self.totalsize()}, " \
               f"children: {self.children}, " \
               f"parent: {self.parent}"


list_re = re.compile(r"(\d+) ([\w.]+)")
cmd_re = re.compile(r"\$ (\w+) ([\w.]+)")


def build_tree(input):
    root = node = Node('dir', '/', 0, None)

    for row in input:
        if cmd_re.match(row):
            cmd, target = cmd_re.match(row).groups()
            match cmd:
                case 'cd':
                    match target:
                        case '/':
                            node = root
                        case '..':
                            node = node.parent
                        case _:
                            node = Node('dir', target, 0, node)
                            node.parent.add_child(node)
        if list_re.match(row):
            size, file = list_re.match(row).groups()
            node.add_child(Node('file', file, int(size), node))

    return root


def visit_node(node, callback):
    if node is None:
        return

    callback(node)
    for n in node.children:
        visit_node(n, callback)


@solution(no=1)
def solve_one(input):
    def callback(node):
        if node.type == 'dir' and node.totalsize() <= 100000:
            dirs.append(node)

    root = build_tree(input)
    dirs = []
    visit_node(root, callback)
    return sum([d.totalsize() for d in dirs])


@solution(no=2)
def solve_two(input):
    root = build_tree(input)
    used_space = root.totalsize()
    total_disk_space = 70000000
    required_unused_space = 30000000
    additional_required = required_unused_space - (total_disk_space - used_space)

    def callback(node):
        if node.type == 'dir' and node.totalsize() > additional_required:
            dirs.append(node)

    dirs = []
    visit_node(root, callback)
    return min([d.totalsize() for d in dirs])


def parse_input(file='input'):
    return open(file).read().split("\n")


if __name__ == '__main__':
    input = parse_input()
    solve_one(input)
    solve_two(input)
