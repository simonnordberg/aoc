import sys
from collections import Counter

INPUT = sys.stdin.read().strip()

H = [(hand, int(bid)) for hand, bid in (line.split() for line in INPUT.split("\n"))]


def rank(hand: str):
    return sorted(Counter(hand).values(), reverse=True)


def score(hand, joker: bool):
    mapping = {
        "T": "A",
        "J": "0" if joker else "B",
        "Q": "C",
        "K": "D",
        "A": "E",
    }

    hand = "".join(mapping.get(c, c) for c in hand)
    ranked_hands = [(rank(hand.replace(r, "0")), hand) for r in "23456789ABCDE"]
    return max(ranked_hands)


H = sorted(H, key=lambda x: score(x[0], False))
p1 = [(i + 1) * b for i, (_, b) in enumerate(H)]
print("p1:", sum(p1))


H = sorted(H, key=lambda x: score(x[0], True))
p2 = [(i + 1) * b for i, (_, b) in enumerate(H)]
print("p2:", sum(p2))
