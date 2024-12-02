import sys


def test_sign(d):
    return all(x > 0 for x in d) or all(x < 0 for x in d)


def test_dist(d):
    return all(1 <= abs(x) <= 3 for x in d)


def test(ll, dampener=True):
    if dampener:
        return any(test(ll[:i] + ll[i + 1:], dampener=False) for i in range(len(ll)))
    d = [a - b for a, b in zip(ll, ll[1:])]
    return test_sign(d) and test_dist(d)


lines = sys.stdin.read().strip().split("\n")
p1 = p2 = 0

for line in lines:
    ll = list(map(int, line.split()))
    p1 += test(ll, dampener=False)
    p2 += test(ll, dampener=True)

print(p1)
print(p2)
