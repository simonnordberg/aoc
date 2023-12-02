import sys

n = sum(2000 <= int(line) * 28 <= 3000 for line in sys.stdin.read().split("\n"))
print(n)
