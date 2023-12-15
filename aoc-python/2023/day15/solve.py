import re
import sys
from collections import defaultdict

INPUT = sys.stdin.read().strip()
CMDS = INPUT.split(",")


def f(s):
    h = 0
    for c in s:
        h += ord(c)
        h *= 17
        h = h % 256
    return h


p1 = sum(f(cmd) for cmd in CMDS)
print("p1:", p1)


BOXES = defaultdict(list)
CMD_RE = re.compile(r"([A-Za-z]+)([=-])(\d?)")

for cmd in CMDS:
    label, op, length = CMD_RE.match(cmd).groups()
    length = int(length) if len(length) > 0 else 0
    box = f(label)

    match op:
        case "-":
            BOXES[box] = [(k, v) for k, v in BOXES[box] if k != label]
        case "=":
            if label in [k for k, v in BOXES[box]]:
                BOXES[box] = [
                    (k, length) if k == label else (k, v) for k, v in BOXES[box]
                ]
            else:
                BOXES[box].append((label, length))

p2 = sum(
    (k + 1) * (j + 1) * BOXES[k][j][1]
    for k in BOXES.keys()
    for j in range(len(BOXES[k]))
)
print("p2:", p2)

assert p1 == 495972
assert p2 == 245223
