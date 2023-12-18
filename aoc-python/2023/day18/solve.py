import sys

INPUT = sys.stdin.read().strip()
DIRS = {"U": (0, -1), "R": (1, 0), "D": (0, 1), "L": (-1, 0)}


def p1():
    points, b = [(0, 0)], 0
    for line in INPUT.split("\n"):
        dir, dist, _ = line.split()
        dx, dy = DIRS[dir]
        dist = int(dist)
        b += dist
        x, y = points[-1]
        points.append((x + dx * dist, y + dy * dist))
    return points, b


def p2():
    points, b = [(0, 0)], 0
    for line in INPUT.split("\n"):
        _, _, ins = line.split()
        ins = ins[2:-1]
        dist = int(ins[0:-1], 16)
        dir = "RDLU"[int(ins[-1])]

        b += dist
        dx, dy = DIRS[dir]
        x, y = points[-1]
        points.append((x + dx * dist, y + dy * dist))
    return points, b


def solve(points, b):
    # https://en.wikipedia.org/wiki/Shoelace_formula
    # Use Shoelace formula to get the area, transformed to edge integer coordinates
    A = (
        abs(
            sum(
                points[i][1] * (points[i - 1][0] - points[(i + 1) % len(points)][0])
                for i in range(len(points))
            )
        )
        // 2
    )

    # https://en.wikipedia.org/wiki/Pick%27s_theorem
    # Use Pick's theorem to find the number of interior points (i)
    # A = i + b/2 - 1 -->
    #   i = A - b/2 + 1
    i = A - b // 2 + 1

    # Total area: interior points + boundary points
    return i + b


print("p1:", solve(*p1()))
print("p2:", solve(*p2()))
