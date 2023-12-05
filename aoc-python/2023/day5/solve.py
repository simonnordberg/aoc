import re
import sys


class Function:
    def __init__(self, s):
        self.tuples = [[int(x) for x in line.split()] for line in s.split("\n")[1:]]

    def apply_one(self, x):
        for dst, src, sz in self.tuples:
            if src <= x < src + sz:
                return dst + x - src
        return x

    def apply_range(self, ranges):
        mapped_ranges = []
        for dst, src, sz in self.tuples:
            src_end = src + sz
            unmapped_ranges = []
            while ranges:
                start, end = ranges.pop()
                before = (start, min(end, src))
                inter = (max(start, src), min(src_end, end))
                after = (max(src_end, start), end)

                if before[1] > before[0]:
                    unmapped_ranges.append(before)
                if inter[1] > inter[0]:
                    mapped_ranges.append((dst + inter[0] - src, dst + inter[1] - src))
                if after[1] > after[0]:
                    unmapped_ranges.append(after)
            ranges = unmapped_ranges
        return mapped_ranges + ranges


INPUT = sys.stdin.read().strip()
parts = INPUT.split("\n\n")
seeds = [int(x) for x in re.findall(r"(\d+)", parts[0])]
functions = [Function(s) for s in parts[1:]]

p1 = []
for seed in seeds:
    for f in functions:
        seed = f.apply_one(seed)
    p1.append(seed)
print("p1:", min(p1))
assert min(p1) == 309796150

p2 = []
seed_pairs = [(seeds[x], seeds[x + 1]) for x in range(0, len(seeds), 2)]
for start, size in seed_pairs:
    seed_ranges = [(start, start + size)]
    for f in functions:
        seed_ranges = f.apply_range(seed_ranges)
    p2.append(min(seed_ranges)[0])
print("p2:", min(p2))
assert min(p2) == 50716416
