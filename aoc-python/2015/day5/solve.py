import sys

INPUT = sys.stdin.read().strip()
VOWELS = "aeiou"


def is_nice(s):
    has_vowels = sum(c in "aeiou" for c in s) >= 3
    has_double = any(s[i] == s[i + 1] for i in range(len(s) - 1))
    has_disallowed = any(ss in s for ss in ["ab", "cd", "pq", "xy"])

    return has_vowels and has_double and not has_disallowed


def is_nicer(s):
    has_pair = any(s[i : i + 2] in s[i + 2 :] for i in range(len(s) - 2))
    has_repeat = any(s[i] == s[i + 2] for i in range(len(s) - 2))
    return has_pair and has_repeat


p1 = sum(is_nice(s) for s in INPUT.split("\n"))
print("p1:", p1)
p2 = sum(is_nicer(s) for s in INPUT.split("\n"))
print("p2:", p2)

assert p1 == 236
assert p2 == 51
