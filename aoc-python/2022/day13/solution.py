from __future__ import annotations

import json
import math
from enum import IntEnum
from functools import cmp_to_key
from itertools import zip_longest
from pathlib import Path

from aoc.util import solution


class Compare(IntEnum):
    CorrectOrder = -1
    UnknownOrder = 0
    IncorrectOrder = 1


def compare(left, right) -> Compare:
    if left is None:
        return Compare.CorrectOrder
    elif right is None:
        return Compare.IncorrectOrder
    elif isinstance(left, int) and isinstance(right, int):
        if left < right:
            return Compare.CorrectOrder
        elif left > right:
            return Compare.IncorrectOrder
    elif isinstance(left, list) and isinstance(right, list):
        for l, r in zip_longest(left, right):
            c = compare(l, r)
            if c is not Compare.UnknownOrder:
                return c
    elif isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    return Compare.UnknownOrder


@solution(no=1)
def solve_one(packets):
    return sum(i + 1 for i, r in enumerate([compare(left, right) for left, right in zip(*[iter(packets)] * 2)]) if
               r == Compare.CorrectOrder)


@solution(no=2)
def solve_two(packets):
    dividers = [[[2]], [[6]]]
    packets.extend(dividers)

    return math.prod(i + 1 for i, x in enumerate(sorted(packets, key=cmp_to_key(compare))) if x in dividers)


def parse_packets(file='input'):
    return [json.loads(line) for line in Path(file).read_text().strip().split("\n") if line.strip()]


if __name__ == '__main__':
    packets = parse_packets()
    solve_one(packets)
    solve_two(packets)
