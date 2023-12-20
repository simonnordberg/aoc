import sys
from itertools import accumulate

INPUT = sys.stdin.read().strip()


acc = [*accumulate(1 if x == "(" else -1 for x in INPUT)]
p1 = acc[-1]
p2 = acc.index(-1) + 1

print("p1:", p1)
print("p2:", p2)

assert p1 == 232
assert p2 == 1783
