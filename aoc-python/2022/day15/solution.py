from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

from aoc.util import solution, Point


@dataclass
class SensorReading:
    sensor: Point
    beacon: Point
    distance: int = field(init=False)

    def __post_init__(self):
        self.distance = Point.manhattan_distance(self.beacon, self.sensor)


SENSOR = "S"
BEACON = "B"
COVERAGE = "#"


@solution(no=1)
def solve_one(readings: [SensorReading], target_row: int = 2000000):
    grid = {}
    for reading in readings:
        grid[reading.sensor] = SENSOR
        grid[reading.beacon] = BEACON

    for reading in readings:
        distance = reading.distance
        for y in range(reading.sensor.y-distance, reading.sensor.y+distance+1):
            if y != target_row:
                continue
            r = distance-abs(reading.sensor.y-y)
            for x in range(reading.sensor.x-r, reading.sensor.x+r+1):
                p = Point(x, y)
                if p not in grid:
                    grid[p] = COVERAGE

    return sum(1 for k, v in grid.items() if k.y == target_row and v == COVERAGE)


@solution(no=2)
def solve_two(readings: [SensorReading], high: int = 4000000):
    def check_position(x: int, y: int, high: int) -> Point | None:
        if x < 0 or y < 0 or x > high or y > high:
            return None

        p = Point(x, y)
        for reading in readings:
            d = Point.manhattan_distance(reading.sensor, p)
            if d <= reading.distance:
                return None

        return p

    def find_point(readings: [SensorReading], high: int) -> Point | None:
        for reading in readings:
            x = reading.sensor.x
            y = reading.sensor.y
            d = reading.distance+1

            for i in range(0, d):
                checks = [check_position(x+i, y+i-d, high),
                          check_position(x-i+d, y+i, high),
                          check_position(x-i, y+i+d, high),
                          check_position(x+i-d, y-i, high)]
                if any(checks):
                    return next(n for n in checks if n is not None)

    p = find_point(readings, high)
    return p.x*high+p.y


val_re = re.compile(r"\w+=([-\d]+)")


def parse_readings(line):
    x1, y1, x2, y2 = map(int, val_re.findall(line))
    return SensorReading(sensor=Point(x1, y1),
                         beacon=Point(x2, y2))


def parse_input(file='input'):
    return [parse_readings(line) for line in Path(file).read_text().strip().split("\n")]


if __name__ == '__main__':
    sensors = parse_input()
    solve_one(sensors)
    solve_two(sensors)
