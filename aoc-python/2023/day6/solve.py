import sys
from math import prod

INPUT = sys.stdin.read().strip()
parts = INPUT.split("\n")

T = [int(x) for x in parts[0].split()[1:]]
D = [int(x) for x in parts[1].split()[1:]]


p1 = [sum([1 for x in range(t + 1) if x * (t - x) > d]) for t, d in zip(T, D)]
print("p1:", prod(p1))

t = int("".join([str(x) for x in T]))
d = int("".join([str(x) for x in D]))

p2 = [1 for x in range(t + 1) if x * (t - x) > d]
print("p2:", sum(p2))
