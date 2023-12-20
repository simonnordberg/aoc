import sys

INPUT = sys.stdin.read().strip()

p1 = 0
p2 = 0
for line in INPUT.split("\n"):
    l, w, h = [int(x) for x in line.split("x")]
    a1, a2, a3 = l * w, w * h, h * l
    p1 += 2 * (a1 + a2 + a3) + min(a1, a2, a3)

    p2 += 2 * sum(sorted([l, w, h])[:2]) + l * w * h
print("p1:", p1)
print("p2:", p2)

assert p1 == 1606483
assert p2 == 3842356
