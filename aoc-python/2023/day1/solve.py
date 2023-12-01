import sys

from util import *


def solve(xs):
    return sum([int(f"{x[0]}{x[-1]}") for x in xs])


@solution(no=1)
def solve_one(xs):
    return solve(xs)


@solution(no=2)
def solve_two(xs):
    return solve(xs)


def parse(line, replace=False):
    if replace:
        line = (
            line
            .replace("one", "o1e")
            .replace("two", "t2o")
            .replace("three", "t3e")
            .replace("four", "f4r")
            .replace("five", "f5e")
            .replace("six", "s6x")
            .replace("seven", "s7n")
            .replace("eight", "e8t")
            .replace("nine", "n9e")
        )

    return ints(line.strip(), single_digit=True)


if __name__ == '__main__':
    lines = sys.stdin.readlines()
    solve_one(list(map(lambda x: parse(x, False), lines)))
    solve_two(list(map(lambda x: parse(x, True), lines)))
