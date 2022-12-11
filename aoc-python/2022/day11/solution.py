from __future__ import annotations

import math
import operator
import re
from dataclasses import dataclass
from pathlib import Path

from aoc.util import solution

monkey_re = re.compile(r"Monkey (\d+):\n"
                       r"\s\sStarting items: (.*)\n"
                       r"\s\sOperation: (.*)\n"
                       r"\s\sTest: divisible by (\d+)\n"
                       r"\s\s\s\sIf true: throw to monkey (\d+)\n"
                       r"\s\s\s\sIf false: throw to monkey (\d+)")
expr_re = re.compile(r"(\w+) ([+*]+) (\w+)")

Operator = {
    "+": operator.add,
    "*": operator.mul
}


@dataclass
class Monkey:
    no: int
    items: []
    worry_op: str
    divisor: int
    monkey_true: int
    monkey_false: int
    inspect_count: int = 0

    def catch_item(self, item: int):
        self.items.append(item)


def parse_monkey(chunk):
    match = monkey_re.match(chunk)
    return Monkey(
        no=int(match.group(1)),
        items=list(map(int, match.group(2).split(", "))),
        worry_op=match.group(3).split("=")[1].strip(),
        divisor=int(match.group(4)),
        monkey_true=int(match.group(5)),
        monkey_false=int(match.group(6))
    ) if match else None


@dataclass
class World:
    monkeys: [Monkey]
    relief: bool = True
    lcm: int = 0

    def tick(self):
        for monkey in self.monkeys:
            self.inspect_items(monkey)

    def inspect_items(self, monkey):
        monkey.inspect_count += len(monkey.items)
        while len(monkey.items) > 0:
            item = monkey.items.pop(0)
            worry_op = monkey.worry_op.replace("old", str(item))
            lhs, op, rhs = expr_re.match(worry_op).groups()
            worry_level = Operator[op](int(lhs), int(rhs))

            if self.relief:
                worry_level //= 3

            if self.lcm:
                worry_level %= self.lcm

            if worry_level % monkey.divisor == 0:
                self.throw_item(monkey.monkey_true, worry_level)
            else:
                self.throw_item(monkey.monkey_false, worry_level)

    def throw_item(self, target: int, item: int):
        self.monkeys[target].catch_item(item)

    def monkey_business(self):
        return math.prod(sorted(map(lambda x: x.inspect_count, self.monkeys))[-2:])


@solution(no=1)
def solve_one(monkeys):
    world = World(monkeys, relief=True)
    for _ in range(20):
        world.tick()

    return world.monkey_business()


@solution(no=2)
def solve_two(monkeys):
    world = World(monkeys,
                  relief=False,
                  lcm=math.lcm(*[m.divisor for m in monkeys]))
    for _ in range(10000):
        world.tick()

    return world.monkey_business()


def parse_input(file='input'):
    return [parse_monkey(chunk) for chunk in Path(file).read_text().strip().split("\n\n")]


if __name__ == '__main__':
    solve_one(parse_input())
    solve_two(parse_input())
