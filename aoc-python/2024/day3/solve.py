import re
import sys

RE_MUL = r"mul\((\d{1,3}),(\d{1,3})\)"
RE_ENABLE = r"(do\(\))"
RE_DISABLE = r"(don\'t\(\))"

INPUT = sys.stdin.read().strip()

# Part 1
print(sum([int(x) * int(y) for x, y in re.findall(RE_MUL, INPUT)]))

# Part 2
p2 = 0
enabled = True
for a, b, enable, disable in re.findall(f"{RE_MUL}|{RE_ENABLE}|{RE_DISABLE}", INPUT):
    if enable or disable:
        enabled = bool(enable)
    elif enabled:
        p2 += int(a) * int(b)

print(p2)
