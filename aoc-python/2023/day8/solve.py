import math
import re
import sys

INPUT = sys.stdin.read().strip()

ins, rest = INPUT.split("\n\n")
G = {}
for line in rest.split("\n"):
    a, b, c = re.findall(r"(\w+)", line.strip())
    G[a] = (b, c)

I = [int(i == "R") for i in ins]


def path_len(node, end):
    n = 0
    while not node.endswith(end):
        i = I[n % len(I)]
        node = G[node][i]
        n += 1
    return n


print("p1:", path_len("AAA", "ZZZ"))

starts = [k for k in G if k.endswith("A")]
path_lens = [path_len(s, "Z") for s in starts]
print("p2:", math.lcm(*path_lens))
