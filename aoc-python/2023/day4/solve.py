import re
import sys
from collections import defaultdict

p1 = 0
N = defaultdict(int)

for i, line in enumerate(sys.stdin.read().split("\n")):
    first, rest = line.split("|")
    a = [int(x) for x in re.findall(r"\d+", first)][1:]
    b = [int(x) for x in re.findall(r"\d+", rest)]
    ab = len(set(a) & set(b))
    p1 += 2 ** (ab - 1) if ab > 0 else 0

    N[i] += 1
    for j in range(ab):
        N[i + 1 + j] += N[i]

print("p1:", p1)
print("p2:", sum(N.values()))
