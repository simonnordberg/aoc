import functools
import unittest
from dataclasses import dataclass
from re import findall


@dataclass
class Point:
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __abs__(self):
        return Point(abs(self.x), abs(self.y))

    def __eq__(self, other):
        return other and self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(repr(self))

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    @staticmethod
    def manhattan_distance(p1, p2):
        return abs(p1.x - p2.x) + abs(p1.y - p2.y)


NORTH = Point(0, -1)
NORTH_EAST = Point(1, -1)
EAST = Point(1, 0)
SOUTH_EAST = Point(1, 1)
SOUTH = Point(0, 1)
SOUTH_WEST = Point(-1, 1)
WEST = Point(-1, 0)
NORTH_WEST = Point(-1, -1)


def sign(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0


def transpose(xs):
    return list(map(list, zip(*xs)))


def flatten(xs):
    return [x for xx in xs for x in xx]


def ints(s, single_digit=False, negatives=False):
    pattern = (f"{'-?' if negatives else ''}\\d"
               f"{'' if single_digit else '+'}")
    return list(map(int, findall(pattern, s)))


def read_file(file):
    with open(file, "r") as file:
        return file.read().splitlines()


def solution(no=1):
    def decorator_solution(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(f"{no}: {result}")
            return result

        return wrapper

    return decorator_solution


class TestInts(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(ints("123 abc -456"), [123, 456])

    def test_single_digit(self):
        self.assertEqual(ints("123 abc -456", single_digit=True), [1, 2, 3, 4, 5, 6])

    def test_negatives(self):
        self.assertEqual(ints("123 abc -456", negatives=True), [123, -456])

    def test_single_digit_negatives(self):
        self.assertEqual(ints("123 abc -456", single_digit=True, negatives=True), [1, 2, 3, -4, 5, 6])

    def test_no_numbers(self):
        self.assertEqual(ints("abc def"), [])


if __name__ == '__main__':
    unittest.main()
