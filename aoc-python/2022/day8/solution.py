from __future__ import annotations

from aoc.util import solution


def count_visible(values, threshold):
    return next((n + 1 for n, x in enumerate(values) if x >= threshold), len(values))


@solution(no=1)
def solve_one(rows):
    visible = 2 * len(rows) + 2 * len(rows[0]) - 4
    for y in range(1, len(rows) - 1):
        for x in range(1, len(rows[y]) - 1):
            elm = rows[y][x]
            top = max(rows[yy][x] for yy in range(0, y)) < elm
            right = max(rows[y][x + 1:]) < elm
            bottom = max(rows[yy][x] for yy in range(y + 1, len(rows))) < elm
            left = max(rows[y][:x]) < elm

            if top or right or bottom or left:
                visible += 1

    return visible


@solution(no=2)
def solve_two(rows):
    max_score = 0
    for y in range(1, len(rows) - 1):
        for x in range(1, len(rows[y]) - 1):
            elm = rows[y][x]
            top = count_visible([rows[yy][x] for yy in reversed(range(0, y))], elm)
            right = count_visible(rows[y][x + 1:], elm)
            bottom = count_visible([rows[yy][x] for yy in range(y + 1, len(rows))], elm)
            left = count_visible(list(reversed(rows[y][:x])), elm)

            score = top * right * bottom * left
            max_score = score if score > max_score else max_score

    return max_score


def parse_input(file='input'):
    rows = []
    for row in open(file).read().split("\n"):
        rows.append(list(map(int, row)))
    return rows


if __name__ == '__main__':
    rows = parse_input()
    solve_one(rows)
    solve_two(rows)
