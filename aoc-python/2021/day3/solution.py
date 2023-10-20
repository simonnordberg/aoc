from __future__ import annotations

from collections import Counter
from copy import deepcopy
from pathlib import Path

from aoc.util import solution


@solution(no=2)
def solve_one(data):
    gamma, epsilon = "", ""
    for col in range(len(data[0])):
        common = Counter(row[col] for row in data)
        gamma += "1" if common["1"] > common["0"] else "0"
        epsilon += "1" if common["0"] > common["1"] else "0"
    return int(gamma, 2) * int(epsilon, 2)


@solution(no=2)
def solve_two(data):
    oxygen_rating = ''
    oxygen = deepcopy(data)
    for col in range(len(oxygen[0])):
        common = Counter(x[col] for x in oxygen)
        if common["0"] > common["1"]:
            oxygen = [x for x in oxygen if x[col] == "0"]
        else:
            oxygen = [x for x in oxygen if x[col] == "1"]
        oxygen_rating = oxygen[0] if oxygen else oxygen_rating

    co2_rating = ''
    co2 = deepcopy(data)
    for col in range(len(co2[0])):
        common = Counter(x[col] for x in co2)
        if common["0"] > common["1"]:
            co2 = [x for x in co2 if x[col] == "1"]
        else:
            co2 = [x for x in co2 if x[col] == "0"]
        co2_rating = co2[0] if co2 else co2_rating

    return int(oxygen_rating, 2) * int(co2_rating, 2)


def parse_input(file='input'):
    return Path(file).read_text().strip().split("\n")


if __name__ == '__main__':
    data = parse_input("input")
    solve_one(deepcopy(data))
    solve_two(deepcopy(data))
