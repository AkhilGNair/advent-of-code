from typing import NamedTuple
from enum import Enum
from collections import deque, Counter, defaultdict
from pathlib import Path
from functools import reduce

BLACK = 1
WHITE = 0


class Point(NamedTuple):
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


class Directions(Enum):
    e = Point(2, 0)
    se = Point(1, -1)
    sw = Point(-1, -1)
    w = Point(-2, 0)
    nw = Point(-1, 1)
    ne = Point(1, 1)


def parse(s, current=[]):
    ds = deque(list(s))
    while ds:
        d = ds.popleft()
        current.append(d)
        if d in {"e", "w"}:
            yield "".join(current)
            current = []


def move(start, dir):
    return Directions[dir].value + start


def count_black(d):
    return list(d.values()).count(BLACK)


REF = Point(0, 0)
floor = Path("input.txt").read_text().strip().split("\n")
tiles = Counter(reduce(move, route, REF) for route in (parse(route, []) for route in floor))
tiles = {k: v % 2 for k, v in tiles.items()}
n_black = count_black(tiles)
print("part1:", n_black)

# == part 2 ==

tiles = defaultdict(int, tiles)


def neighbours(p, tiles):
    return [tiles[p + d.value] for d in Directions].count(BLACK)


def simulate(tiles):
    while True:

        for tile in tiles.copy():
            for t in [tile + d.value for d in Directions]:
                tiles[t]

        new = defaultdict(int)
        for tile in tiles.copy():
            b = neighbours(tile, tiles)

            if tiles[tile] == BLACK:
                new[tile] = WHITE if ((b == 0) or (b > 2)) else BLACK

            if tiles[tile] == WHITE:
                new[tile] = BLACK if (b == 2) else WHITE

        yield count_black(new)
        tiles = new.copy()


day = simulate(tiles)

for i in range(100):
    print(f"Day {i+1}: {next(day)}")
