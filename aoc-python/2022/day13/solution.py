from __future__ import annotations

import json
import math
from enum import Enum
from itertools import zip_longest
from pathlib import Path

from aoc.util import solution


class Compare(Enum):
    CorrectOrder = 1
    UnknownOrder = 0
    IncorrectOrder = -1


def compare(left, right) -> Compare:
    if left is None and right is not None:
        return Compare.CorrectOrder
    elif left is not None and right is None:
        return Compare.IncorrectOrder
    elif isinstance(left, int) and isinstance(right, int):
        if left < right:
            return Compare.CorrectOrder
        elif left > right:
            return Compare.IncorrectOrder
    elif isinstance(left, list) and isinstance(right, list):
        for l, r in zip_longest(left, right, fillvalue=None):
            match compare(l, r):
                case Compare.CorrectOrder:
                    return Compare.CorrectOrder
                case Compare.IncorrectOrder:
                    return Compare.IncorrectOrder
    elif isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    return Compare.UnknownOrder


@solution(no=1)
def solve_one(packets):
    return sum([i + 1 if r == Compare.CorrectOrder else 0 for i, r in
                enumerate([compare(left, right) for left, right in zip(*[iter(packets)] * 2)])])


@solution(no=2)
def solve_two(packets):
    dividers = [[[2]], [[6]]]
    packets.extend(dividers)

    for i in range(len(packets) - 1):
        for j in range(i, len(packets)):
            if compare(packets[i], packets[j]) == Compare.IncorrectOrder:
                tmp = packets[i]
                packets[i] = packets[j]
                packets[j] = tmp

    return math.prod([i + 1 for i, x in enumerate(packets) if x in dividers])


def parse_packets(file='input'):
    return [json.loads(line) for line in Path(file).read_text().strip().split("\n") if line.strip()]


if __name__ == '__main__':
    packets = parse_packets()
    solve_one(packets)
    solve_two(packets)
