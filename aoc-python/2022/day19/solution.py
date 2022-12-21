from __future__ import annotations

import math
import re
from pathlib import Path

from aoc.util import solution

NUM_MATERIALS = 4
NUM_ROBOT_TYPES = 4


def importance_rank(item):
    _, (robots, inv, mined) = item
    return 100000 * mined[3] + 100 * mined[2] + 10 * mined[1] + mined[0]


def bfs(building_costs: list, robots: tuple, minutes: int, queue_depth: int):
    max_mined = 0
    threshold = minutes
    queue = list()
    queue.append((minutes, (robots, (0, 0, 0, 0), (0, 0, 0, 0))))

    while queue:
        minutes_remaining, (robots, inv, mined) = queue.pop(0)

        if minutes_remaining < threshold:
            queue.sort(key=importance_rank, reverse=True)
            queue = queue[:queue_depth]
            threshold = minutes_remaining

        if minutes_remaining <= 0:
            max_mined = max(max_mined, mined[3])
            continue

        # Mining
        new_inv = [inv[i] + robots[i] for i in range(NUM_MATERIALS)]
        new_mined = [mined[i] + robots[i] for i in range(NUM_MATERIALS)]

        # Not building a robot
        queue.append((minutes_remaining - 1, (robots, tuple(new_inv), tuple(new_mined))))

        # Build a new robot
        for robot_type in range(NUM_ROBOT_TYPES):
            robot_cost = building_costs[robot_type]

            if all([inv[material] >= robot_cost[material] for material in range(NUM_MATERIALS)]):
                new_robots = list(robots)
                new_robots[robot_type] += 1
                inv_after_build = [new_inv[material] - robot_cost[material] for material in range(NUM_MATERIALS)]
                queue.append((minutes_remaining - 1, (tuple(new_robots), tuple(inv_after_build), tuple(new_mined))))

    return max_mined


@solution(no=1)
def solve_one(blueprints):
    return sum((bp + 1) * bfs(costs, (1, 0, 0, 0), 24, queue_depth=200)
               for bp, costs in enumerate(blueprints))


@solution(no=2)
def solve_two(blueprints):
    return math.prod(bfs(costs, (1, 0, 0, 0), 32, queue_depth=500)
                     for costs in blueprints[:3])


def parse_input(file='input'):
    blueprints = []
    for row in Path(file).read_text().strip().split("\n"):
        bp, ore_ore, clay_ore, obs_ore, obs_clay, geo_ore, geo_obs = map(int, re.findall(r"\d+", row))
        blueprints.append([
            (ore_ore, 0, 0, 0),
            (clay_ore, 0, 0, 0),
            (obs_ore, obs_clay, 0, 0),
            (geo_ore, 0, geo_obs, 0),
        ])
    return blueprints


if __name__ == '__main__':
    blueprints = parse_input()
    solve_one(blueprints)
    solve_two(blueprints)
