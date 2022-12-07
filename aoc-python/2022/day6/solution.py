from aoc.util import solution


def _solve(input, length):
    for x in range(0, len(input) - length):
        if len(set(input[x:x + length])) == length:
            return x + length


@solution(no=1)
def solve_one(input):
    return _solve(input, 4)


@solution(no=2)
def solve_two(input):
    return _solve(input, 14)


def parse_input(file='input'):
    return open(file).read()


if __name__ == '__main__':
    input = parse_input()
    solve_one(input)
    solve_two(input)
