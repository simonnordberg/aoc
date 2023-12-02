import re
import sys
from collections import defaultdict
from math import prod

from util import *


@solution(no=1)
def solve_one(xs):
    return sum(a for a, b in xs if
               max(c["red"] for c in b) <= 12 and
               max(c["green"] for c in b) <= 13 and
               max(c["blue"] for c in b) <= 14)


@solution(no=2)
def solve_two(xs):
    xd = []
    for _, rounds in xs:
        m = defaultdict(int)
        for r in rounds:
            for k, v in r.items():
                m[k] = max(m[k], v)
        xd.append(prod(v for _, v in m.items()))
    return sum(xd)


def parse(line):
    parts = line.strip().split(":")
    game = sum(ints(parts[0]))
    rounds = []
    for round in parts[1].split(";"):
        cubes = defaultdict(int)
        for n, color in re.findall(r"(\d+) (\w+)", round):
            cubes[color] = int(n)
        rounds.append(cubes)
    return game, rounds


if __name__ == '__main__':
    lines = sys.stdin.readlines()
    solve_one(list(map(parse, lines)))
    solve_two(list(map(parse, lines)))
