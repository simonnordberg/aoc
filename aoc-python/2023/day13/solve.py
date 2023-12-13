import sys

INPUT = sys.stdin.read().strip()

P = [[line for line in pattern.split("\n")] for pattern in INPUT.split("\n\n")]


def f(p, tolerance=0):
    for i in range(0, len(p) - 1):
        diff = 0

        # iterate pairs of mirrored/reversed rows and sum diffs
        for s1, s2 in zip(p[i::-1], p[i + 1 :]):
            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    diff += 1

        if diff == tolerance:
            return i + 1
    return 0


p1 = sum(100 * f(p, 0) + f(["".join(c) for c in zip(*p)], 0) for p in P)
print("p1:", p1)

p2 = sum(100 * f(p, 1) + f(["".join(c) for c in zip(*p)], 1) for p in P)
print("p2:", p2)

assert p1 == 33735
assert p2 == 38063
