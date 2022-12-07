import string

from aoc.util import solution


def _range(input):
    return list(range(int(input.split('-')[0]), int(input.split('-')[1]) + 1))


@solution(no=1)
def solve_one(data):
    return sum([1 if ar.issubset(br) or br.issubset(ar) else 0
                for ar, br in (({*_range(a)}, {*_range(b)})
                               for a, b in (row.split(',') for row in data))])


@solution(no=2)
def solve_two(data):
    return sum([1 if len(ar & br) > 0 else 0
                for ar, br in (({*_range(a)}, {*_range(b)})
                               for a, b in (row.split(',') for row in data))])


def parse_input(file='input'):
    return open(file).read().split("\n")


if __name__ == '__main__':
    data = parse_input()
    solve_one(data)
    solve_two(data)
