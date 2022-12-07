from aoc.util import solution


@solution(no=1)
def solve_one(data):
    def outcome(a, b):
        return 3 * ((b - a + 1) % 3)

    return sum(r for r in (1 + b + outcome(a, b) for (a, b) in data))


@solution(no=2)
def solve_two(data):
    def outcome(a, b):
        return (a + b + 2) % 3 + (3 * b)

    return sum(r for r in (1 + outcome(a, b) for (a, b) in data))


def decode(s, base):
    return ord(s) - ord(base)


def parse_input(file='input'):
    return [
        (decode(a, 'A'), decode(b, 'X'))
        for a, b in (row.split()
                     for row in open(file).read().split("\n"))
    ]


if __name__ == '__main__':
    data = parse_input()
    solve_one(data)
    solve_two(data)
