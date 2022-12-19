from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import List

from aoc.util import solution, Point


class Shape(Enum):
    Minus = [Point(0, 0), Point(1, 0), Point(2, 0), Point(3, 0)]
    Plus = [Point(1, 0), Point(0, 1), Point(1, 1), Point(2, 1), Point(1, 2)]
    L = [Point(0, 0), Point(1, 0), Point(2, 0), Point(2, 1), Point(2, 2)]
    I = [Point(0, 0), Point(0, 1), Point(0, 2), Point(0, 3)]
    Hash = [Point(0, 0), Point(1, 0), Point(0, 1), Point(1, 1)]


ROCKS = [
    Shape.Minus,
    Shape.Plus,
    Shape.L,
    Shape.I,
    Shape.Hash
]


@dataclass
class Rock:
    position: Point
    shape: Shape

    def move_to(self, point: Point):
        self.position = point

    def highest_point(self) -> int:
        return max(p.y for p in self.coverage())

    def coverage(self, position: Point = None) -> [Point]:
        return [(position or self.position) + p for p in self.shape.value]


FALL_START_X = 2
FALL_HEIGHT = 3
CHAMBER_WIDTH = 7


@dataclass
class World:
    jets: List[str]
    _chamber = {}  # bottom is at (x, 0)
    _highest = 0

    def __post_init__(self):
        for x in range(CHAMBER_WIDTH):
            self._chamber[Point(x, 0)] = "#"

    def simulate(self, iterations):
        time = 0

        for i in range(iterations):
            rock = self.spawn_rock(shape=ROCKS[i % len(ROCKS)])

            #if i % 100_000 == 0:
            #    print(f"Progress: {(i / iterations) * 100}%")

            while True:
                self.push_rock(rock, time)
                rested = self.fall_rock(rock)
                time += 1

                if rested:
                    break

    def spawn_rock(self, shape: Shape) -> Rock:
        return Rock(position=Point(FALL_START_X, self._highest + FALL_HEIGHT + 1),
                    shape=shape)

    def push_rock(self, rock: Rock, time: int):
        jet = self.jets[time % len(self.jets)]
        pos = Point(-1, 0) if jet == '<' else Point(1, 0)
        next_pos = rock.position + pos

        if self.is_free_position(rock, next_pos):
            # print(f"push ({jet}) {rock} -> {next_pos}")
            rock.move_to(next_pos)
        else:
            # print(f"Pushed ({jet}) but nothing happened!")
            pass

    def fall_rock(self, rock: Rock) -> bool:
        next_pos = rock.position + Point(0, -1)
        if self.is_free_position(rock, next_pos):
            rock.move_to(next_pos)
            # print(f"fall {rock} -> {next_pos}")
            return False
        else:
            self.rest_rock(rock)
            return True

    def is_free_position(self, rock: Rock, next_pos: Point):
        if any(p in self._chamber or p.x < 0 or p.x >= CHAMBER_WIDTH for p in rock.coverage(next_pos)):
            return False
        return True

    def rest_rock(self, rock: Rock):
        for pos in rock.coverage():
            self._chamber[pos] = "#"
        self._highest = max(self._highest, rock.highest_point())

        # print(f"rested {rock}, highest: {self._highest}")
        # print("-----------------")
        # self.debug()
        # print("-----------------")

    def debug(self):
        for y in range(self._highest):
            print(''.join('#' if Point(x, self._highest - y) in self._chamber else '.' for x in range(7)))
        print()

    @property
    def height(self):
        return self._highest


@solution(no=1)
def solve_one(jets):
    w = World(jets=jets)
    w.simulate(iterations=2022)
    return w.height


@solution(no=2)
def solve_two(jets):
    w = World(jets=jets)
    w.simulate(iterations=1_000_000_000_000)
    return w.height


def parse_input(file='input'):
    return list(Path(file).read_text().strip())


if __name__ == '__main__':
    jets = parse_input()
    solve_one(jets)
    # solve_two(jets)
