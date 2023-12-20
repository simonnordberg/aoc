import hashlib
import sys

INPUT = sys.stdin.read().strip()


def solve(input_prefix: str, result_prefix: str):
    n = 1
    while True:
        md5 = hashlib.md5((input_prefix + str(n)).encode())
        if md5.hexdigest().startswith(result_prefix):
            return n
        n += 1


p1 = solve(INPUT, "00000")
print("p1:", p1)

p2 = solve(INPUT, "000000")
print("p2:", p2)


assert p1 == 282749
assert p2 == 9962624
