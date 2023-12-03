import sys

xs = list(map(int, sys.stdin.read().split("\n")))
avg = sum(xs) // len(xs)
print(xs.count(avg))
