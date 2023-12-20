import re
import sys
from collections import defaultdict

INPUT = sys.stdin.read().strip()
LINE_RE = re.compile(r"(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)")


def solve(actions):
    G = defaultdict(int)
    for line in INPUT.split("\n"):
        action, x1, y1, x2, y2 = LINE_RE.match(line).groups()
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                G[(x, y)] = actions[action](G[(x, y)])
    return sum(v for v in G.values())


p1 = solve(
    {
        "toggle": lambda x: not x,
        "turn on": lambda x: 1,
        "turn off": lambda x: 0,
    }
)
print("p1:", p1)
p2 = solve(
    {
        "toggle": lambda x: x + 2,
        "turn on": lambda x: x + 1,
        "turn off": lambda x: x - 1 if x > 0 else 0,
    }
)
print("p2:", p2)

assert p1 == 569999
assert p2 == 17836115
