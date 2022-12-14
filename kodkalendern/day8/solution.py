from aoc.util import solution


@solution(no=1)
def solve_one(data):
    return sum(b * w * h for b, w, h in
               filter(lambda haystack: 7 not in haystack, (list(map(int, row.split(", "))) for row in data)))


def parse_input(file='input'):
    return open(file).read().split("\n")


if __name__ == '__main__':
    data = parse_input()
    solve_one(data)
