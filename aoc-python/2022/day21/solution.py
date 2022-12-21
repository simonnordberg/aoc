from __future__ import annotations

import operator
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Any

from aoc.util import solution

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
}

operand_re = re.compile(r"(\w{4}): (\w{4}) ([+\-*/]+) (\w{4})")
scalar_re = re.compile(r"(\w{4}): (\d+)")


class Expression:
    pass


@dataclass
class ScalarExpression(Expression):
    value: int


@dataclass
class OperandExpression(Expression):
    lhs: str
    rhs: str
    op: Callable[[Any, Any], Any]


def evaluate(expr: Expression) -> int:
    if isinstance(expr, ScalarExpression):
        return expr.value
    elif isinstance(expr, OperandExpression):
        return expr.op(evaluate(vtable[expr.lhs]),
                       evaluate(vtable[expr.rhs]))


@solution(no=1)
def solve_one():
    return evaluate(vtable["root"])


@solution(no=2)
def solve_two():
    def test(x):
        self.value = x
        left = evaluate(lhs)
        right = evaluate(rhs)

        if left == right:
            return 0
        elif left > right:
            return 1
        else:
            return -1

    def bs(low, high):
        if high >= low:
            mid = (high + low) // 2
            c = test(mid)

            if c == 0:
                return mid
            elif c < 0:
                return bs(low, mid - 1)
            else:
                return bs(mid + 1, high)
        else:
            return -1

    root, self = vtable["root"], vtable["humn"]
    lhs, rhs = vtable[root.lhs], vtable[root.rhs]
    return bs(0, sys.maxsize)


def parse_input(file='input'):
    vtable = {}
    for line in Path(file).read_text().strip().split("\n"):
        operand = operand_re.match(line)
        if operand:
            vtable[operand.group(1)] = OperandExpression(lhs=operand.group(2),
                                                         rhs=operand.group(4),
                                                         op=operators[operand.group(3)])
        scalar = scalar_re.match(line)
        if scalar:
            vtable[scalar.group(1)] = ScalarExpression(value=int(scalar.group(2)))

    return vtable


if __name__ == '__main__':
    vtable = parse_input()
    solve_one()
    solve_two()
