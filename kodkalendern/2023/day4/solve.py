import sys

needle = 106023
xs = list(map(int, sys.stdin.read().split("\n")))
print(min([abs(x - needle) for x in xs]))
