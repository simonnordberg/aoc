"""
Description:
    Vanilla Python implementation using only stdlib.
"""

import sys

part1 = 0
part2 = 0

for line in sys.stdin.read().strip().split("\n"):
    part1_digits = []
    part2_digits = []

    for i, c in enumerate(line):
        if c.isdigit():
            part1_digits.append(c)
            part2_digits.append(c)

        # Translate wordy numbers
        for idx, value in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            if line[i:].startswith(value):
                part2_digits.append(str(idx + 1))

    part1 += int(part1_digits[0] + part1_digits[-1])
    part2 += int(part2_digits[0] + part2_digits[-1])

print(part1)
print(part2)
