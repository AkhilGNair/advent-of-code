from typing import NamedTuple, Set
from math import prod

import aoc


data = aoc.read("input.txt", sep="\n\n", cast_as=str).pop()
N_COLS = data.index("\n")
data = data.replace("\n", "")

CEILING = 9
ADJ = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def x(i, n=N_COLS):
    return i - ((i // n) * n)


def y(i, n=N_COLS):
    return i // n


class Point(NamedTuple):
    x: int
    y: int


cave = {Point(x(i), y(i)): int(h) for i, h in enumerate(data)}


def neighbours(p: Point):
    return [Point(p.x + dx, p.y + dy) for dx, dy in ADJ]


def low_point(p: Point):
    h = cave[p]
    for q in neighbours(p=p):
        try:
            q_h = cave[q]
            if q_h <= h:
                return False
        except KeyError:
            # Could be an edge or corner
            pass
    return True


low_points = [p for p in cave if low_point(p)]
print("Part 1:", sum(cave[p] + 1 for p in low_points))


from collections import deque


def find_basin(p: Point) -> Set[Point]:
    stack = deque([p])
    basin = set()

    while stack:
        point = stack.pop()
        height = cave[point]
        basin.add(point)
        qs = neighbours(point)
        for q in qs:
            try:
                q_height = cave[q]
                if q_height > height and q_height != CEILING:
                    stack.appendleft(q)
            except KeyError:
                pass

    return basin


basin_sizes = [len(find_basin(p)) for p in low_points]
basin_sizes.sort()

print("Part 2:", prod(basin_sizes[-3:]))
