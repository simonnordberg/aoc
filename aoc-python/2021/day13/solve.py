import sys
from copy import copy

from util import *


def print_sheet(sheet):
    mx = max(x for (x, y) in sheet) + 1
    my = max(y for (x, y) in sheet) + 1

    print("> Sheet")
    for y in range(0, my):
        for x in range(0, mx):
            if (x, y) in sheet:
                print("#", end='')
            else:
                print(".", end='')
        print()
    print("< Sheet")


def solve(xs, folds):
    for axis, dist in folds:
        dist = int(dist)
        xd = set()

        for (x, y) in xs:
            if axis == "y" and y > dist:
                y = dist - abs(y - dist)
            elif axis == "x" and x > dist:
                x = dist - abs(x - dist)
            xd.add((x, y))

        xs = xd

    return xs


@solution(no=1)
def solve_one(xs, folds):
    return len(solve(xs, folds[:1]))


@solution(no=2)
def solve_two(xs, folds):
    print_sheet(solve(xs, folds))
    return None


def parse(line):
    return ints(line.strip())


if __name__ == '__main__':
    xs = []
    folds = []
    for line in sys.stdin:
        if line.strip().startswith("fold"):
            folds.append(line.split()[2].split("="))
        elif len(line.strip()) > 0:
            xs.append(ints(line.strip()))

    solve_one(copy(xs), copy(folds))
    solve_two(copy(xs), copy(folds))
