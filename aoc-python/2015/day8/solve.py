import sys

lines = sys.stdin.read().strip().split("\n")

part1 = sum(len(line) - len(eval(line)) for line in lines)
print(part1)

part2 = sum(2 + line.count('\\') + line.count('"') for line in lines)
print(part2)
