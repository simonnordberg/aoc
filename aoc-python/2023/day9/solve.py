import sys

INPUT = sys.stdin.read().strip()

H = [[int(x) for x in line.split()] for line in INPUT.split("\n")]


def f(x):
    N = [x[i + 1] - x[i] for i in range(len(x) - 1)]
    if all(y == 0 for y in N):
        return x[-1]
    else:
        return x[-1] + f(N)


p1 = sum(f(x) for x in H)
print("p1:", p1)
assert p1 == 1798691765

# extrapolating backwards by reversing the input!
p2 = sum(f(x[::-1]) for x in H)
print("p2:", p2)
assert p2 == 1104
