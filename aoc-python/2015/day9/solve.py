import sys
from itertools import permutations

lines = sys.stdin.read().strip().split("\n")

dists = {}
for line in lines:
    v1, v2, d = line.replace(" to ", " ").replace(" = ", " ").split()
    dists[(v1, v2)] = dists[(v2, v1)] = int(d)

cities = set(v1 for v1, v2 in dists.keys())
routes = permutations(cities)

def dist(route):
    return sum(dists[(route[i], route[i + 1])] for i in range(len(route) - 1))

route_dists = list(map(dist, routes))
print(min(route_dists))
print(max(route_dists))