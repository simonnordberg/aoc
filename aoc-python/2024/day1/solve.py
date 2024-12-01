import sys
from collections import Counter

lines = sys.stdin.read().strip().split("\n")

c1, c2 = zip(*(map(int, line.split()) for line in lines))
c1, c2 = sorted(c1), sorted(c2)

p1 = sum(abs(a - b) for a, b in zip(c1, c2))
print(p1)

c2c = Counter(c2)
p2 = sum(a * c2c[a] for a in c1)
print(p2)
