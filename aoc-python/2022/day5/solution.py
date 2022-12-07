import copy
import re
from collections import namedtuple

from aoc.util import solution

Instruction = namedtuple("Instruction", ["qty", "src", "dest"])
instruction_re = re.compile(r'move (\d+) from (\d+) to (\d+)')
crate_re = re.compile(r'[A-Z]')
col_re = re.compile(r'.(.)..')


class Input(object):
    def __init__(self):
        self.stacks = list()
        self.instructions = list()

    def move9000(self, instruction):
        for x in range(0, instruction.qty):
            self.stacks[instruction.dest - 1].insert(0, self.stacks[instruction.src - 1].pop(0))

    def move9001(self, instruction):
        self.stacks[instruction.dest - 1][0:0] = [self.stacks[instruction.src - 1].pop(0) for _ in
                                                  range(0, instruction.qty)]

    def top_of_stack(self):
        return "".join([stack[0] for stack in self.stacks])


@solution(no=1)
def solve_one(input):
    for instruction in input.instructions:
        input.move9000(instruction)
    return input.top_of_stack()


@solution(no=2)
def solve_two(input):
    for instruction in input.instructions:
        input.move9001(instruction)

    return input.top_of_stack()


def parse_input(file='input'):
    """
    Example input:

        [D]
    [N] [C]
    [Z] [M] [P]
     1   2   3

    move 1 from 2 to 1
    move 3 from 1 to 3
    move 2 from 2 to 1
    move 1 from 1 to 2
    """

    stacks, instructions = open(file).read().split("\n\n")
    input = Input()

    for row in stacks.split("\n"):
        # Pad to divisible length of 4 and find all columns of equal width
        for idx, col in enumerate(col_re.findall(row.ljust(len(row) + 3 & -4, ' '))):
            if len(input.stacks) <= idx:
                input.stacks.append(list())

            if crate_re.match(col):
                input.stacks[idx].append(col)

    for row in instructions.split("\n"):
        for match in instruction_re.finditer(row):
            input.instructions.append(Instruction(qty=int(match.group(1)),
                                                  src=int(match.group(2)),
                                                  dest=int(match.group(3))))

    return input


if __name__ == '__main__':
    input = parse_input()
    solve_one(copy.deepcopy(input))
    solve_two(copy.deepcopy(input))
