import operator
import sys

INPUT = sys.stdin.read().strip().split("\n")
OP = {
    "LSHIFT": operator.lshift,
    "RSHIFT": operator.rshift,
    "AND": operator.and_,
    "OR": operator.or_,
}


def evaluate(instructions):
    remaining = instructions.copy()
    values = {}

    def get_value(x):
        return int(x) if x.isdigit() else values[x]

    def parse_instruction(instruction):
        src, dst = instruction.split("->")
        src = src.split()
        dst = dst.strip()

        if len(src) == 1:
            values[dst] = get_value(src[0])
        elif len(src) == 2:
            values[dst] = ~get_value(src[1]) & 0xFFFF  # 0-65535
        elif len(src) == 3:
            lhs, op, rhs = src
            lhs = get_value(lhs)
            rhs = get_value(rhs)
            values[dst] = OP.get(op)(lhs, rhs)

    while remaining:
        for instruction in remaining[:]:
            try:
                parse_instruction(instruction)
                remaining.remove(instruction)
            except KeyError:  # Value not resolved
                pass
    return values


p1 = evaluate(INPUT).get("a")
print("p1:", p1)

instructions = [f"{p1} -> b" if x.endswith("-> b") else x for x in INPUT]
p2 = evaluate(instructions).get("a")
print("p2:", p2)

assert p1 == 956
assert p2 == 40149
