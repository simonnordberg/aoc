from aoc.util import solution


@solution(no=1)
def solve_one(data):
    _scoring = {
        "A X": 4,  # rock, draw
        "A Y": 8,  # paper, win
        "A Z": 3,  # scissors, loss
        "B X": 1,  # rock, loss
        "B Y": 5,  # paper, draw
        "B Z": 9,  # scissors, win
        "C X": 7,  # rock, win
        "C Y": 2,  # paper, loss
        "C Z": 6,  # scissors, draw
    }

    return sum(map(lambda x: _scoring[x], data))


@solution(no=2)
def solve_two(data):
    _scoring = {
        "A X": 3,  # rock, loss, scissors, 0+3
        "A Y": 4,  # rock, draw, rock, 3+1
        "A Z": 8,  # rock, win, paper, 6+2
        "B X": 1,  # paper, loss, rock, 0+1
        "B Y": 5,  # paper, draw, paper, 3+2
        "B Z": 9,  # paper, win, scissors, 6+3
        "C X": 2,  # scissors, loss, paper, 0+2
        "C Y": 6,  # scissors, draw, scissors, 3+3
        "C Z": 7,  # scissors, win, rock, 6+1
    }

    return sum(map(lambda x: _scoring[x], data))


def parse_input(file='input'):
    return open(file).read().split("\n")


if __name__ == '__main__':
    data = parse_input()
    solve_one(data)
    solve_two(data)
