from __future__ import annotations

import functools
import re
from dataclasses import dataclass
from pathlib import Path

from aoc.util import solution


@dataclass
class Valve:
    id: str
    flow: int
    neighbours: [str]

    def __hash__(self):
        return hash(repr(self))


@functools.cache
def max_flow(current: Valve, opened: tuple, time_left) -> int:
    if time_left <= 0:
        return 0

    best = 0
    if current.flow > 0 and current.id not in opened:
        best = current.flow*(time_left-1)+max_flow(current, (*opened, current.id), time_left-1)

    for n in current.neighbours:
        best = max(best, max_flow(valves[n], opened, time_left-1))

    return best


@solution(no=1)
def solve_one(valves: dict[str: Valve]) -> int:
    return max_flow(valves["AA"], (), 30)


@solution(no=2)
def solve_two(valves: dict[str: Valve]) -> int:
    pass


valve_re = re.compile(r"Valve (\w{2}) has flow rate=(\d+); .*?valve.? ([,\s\w]+)$")


def parse_valve(line):
    m = valve_re.match(line)
    return Valve(id=m.group(1),
                 flow=int(m.group(2)),
                 neighbours=m.group(3).split(", "))


def parse_input(file='input'):
    valves = {}
    for line in Path(file).read_text().strip().split("\n"):
        valve = parse_valve(line)
        valves[valve.id] = valve
    return valves


if __name__ == '__main__':
    valves = parse_input()
    solve_one(valves)
    solve_two(valves)
