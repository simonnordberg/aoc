import string

from aoc.util import solution

HAYSTACK = list(string.ascii_lowercase + string.ascii_uppercase)


def prio(needle):
    return HAYSTACK.index(needle) + 1


@solution(no=1)
def solve_one(data):
    return sum(prio(needle.pop())
               for needle in ({*l} & {*r}
                              for l, r in ((line[:len(line) // 2], line[len(line) // 2:])
                                           for line in data)))


@solution(no=2)
def solve_two(data):
    return sum(prio(needle.pop())
               for needle in ({*data[x]} & {*data[x + 1]} & {*data[x + 2]}
                              for x in range(0, len(data), 3)))


def parse_input(file='input'):
    return open(file).read().split("\n")


if __name__ == '__main__':
    data = parse_input()
    solve_one(data)
    solve_two(data)
