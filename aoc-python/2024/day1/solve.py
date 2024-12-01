import sys

lines = sys.stdin.read().strip().split("\n")

c1, c2 = zip(*(map(int, line.split()) for line in lines))
c1, c2 = sorted(c1), sorted(c2)

p1 = sum(abs(a - b) for a, b in zip(c1, c2))
print(p1)

p2 = sum(a * c2.count(a) for a in c1)
print(p2)
