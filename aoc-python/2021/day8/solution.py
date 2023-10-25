from __future__ import annotations

from copy import deepcopy

from aoc.util import solution, read_file


#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....
#
#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg

@solution(no=1)
def solve_one(xs):
    return sum(1 for _, ov in xs for x in ov if len(x) in [2, 3, 4, 7])


@solution(no=2)
def solve_two(xs):
    pass


def parse(line):
    return list(map(lambda x: x.split(), line.split(" | ")))


if __name__ == '__main__':
    _data = list(map(parse, read_file("input")))
    solve_one(deepcopy(_data))
    solve_two(deepcopy(_data))
