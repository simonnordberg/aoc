from aoc.util import solution


@solution(no=1)
def solve_one(data):
    return max(data)


@solution(no=2)
def solve_two(data):
    return sum(sorted(data)[-3:])


def parse_input(file='input'):
    return [
        sum(map(int, group.split("\n")))
        for group in open(file).read().split("\n\n")
    ]


if __name__ == '__main__':
    print("1: {}, 2: {}".format(sorted(map(sum, map(lambda l: map(int, l.split()), open('input').read().split('\n\n'))))[-1], sum(sorted(map(sum, map(lambda l: map(int, l.split()), open(
        'input').read().split('\n\n'))))[-3:])))

#    data = parse_input()
#    solve_one(data)
#    solve_two(data)


