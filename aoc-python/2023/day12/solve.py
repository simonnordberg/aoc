import sys
from functools import cache
from typing import Tuple

INPUT = sys.stdin.read().strip()
xs = [
    (first, [int(n) for n in rest.split(",")])
    for first, rest in (line.split(" ") for line in INPUT.split("\n"))
]


@cache
def f(symbols: str, sizes: Tuple[int, ...]):
    nsymbols = len(symbols)
    nsizes = len(sizes)

    if nsymbols == 0:
        return 1 if nsizes == 0 else 0
    match symbols[0]:
        case ".":
            return f(symbols[1:], sizes)
        case "?":
            return f("." + symbols[1:], sizes) + f("#" + symbols[1:], sizes)
        case "#":
            if nsizes == 0:
                return 0
            current_size = sizes[0]
            if current_size > nsymbols:
                return 0
            elif any(c == "." for c in symbols[0:current_size]):
                return 0
            elif nsizes > 1:
                if current_size + 1 > nsymbols or symbols[current_size] == "#":
                    return 0
                else:
                    return f(symbols[current_size + 1 :], sizes[1:])
            elif nsizes == 1:
                return f(symbols[current_size:], ())
    assert False


p1 = sum([f(symbols, tuple(sizes)) for symbols, sizes in xs])
print("p1:", p1)

p2 = sum([f("?".join([symbols] * 5), tuple(sizes * 5)) for symbols, sizes in xs])
print("p2:", p2)

assert p1 == 7173
assert p2 == 29826669191291
