import sys


def wallet(a, b, c, d):
    return a * 192 + b * 24 + c * 8 + d


INPUT = sys.stdin.read().strip()
xs = [[int(x) for x in line.split(",")] for line in INPUT.split("\n")]
print(sum(1 for a, b, c, d in xs if wallet(a, b, c, d) >= 1000))
