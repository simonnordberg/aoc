import sys
from collections import Counter

lines = sys.stdin.read().strip().split("\n")
G = [list(line) for line in lines]
DIRS = [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]


def find_word(G, word):
    matches = []
    for y in range(len(G)):
        for x in range(len(G[y])):
            for dx, dy in DIRS:
                if all(0 <= x + dx * i < len(G[0]) and 0 <= y + dy * i < len(G) and G[y + dy * i][x + dx * i] == word[i]
                       for i in range(len(word))):
                    matches.append((x, y, dx, dy))
    return matches


print(len(find_word(G, "XMAS")))

diagonals = [(x + dx, y + dy) for x, y, dx, dy in find_word(G, "MAS") if dx != 0 and dy != 0]
print(sum(1 for count in Counter(diagonals).values() if count >= 2))
