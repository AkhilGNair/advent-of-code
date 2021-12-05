from collections import Counter
from typing import NamedTuple

import aoc


class Point(NamedTuple):
    x: int
    y: int

    @classmethod
    def from_str(self, s: str) -> "Point":
        return Point(*(int(v.strip()) for v in s.split(",")))

    def __getitem__(self, item):
        return getattr(self, item)


def not_diagonal(p1, p2):
    return (p1.y == p2.y) or (p1.x == p2.x)


def expand_line(p1, p2):
    axis = "x" if p1.y == p2.y else "y"
    other_axis = "x" if axis == "y" else "y"
    constant = p1[other_axis]  # p1 or p2

    v_min, v_max = sorted((p1[axis], p2[axis]))
    ps = [{other_axis: constant, axis: v} for v in range(v_min, v_max + 1)]

    return [Point(**p) for p in ps]


data = aoc.read("input.txt", cast_as=str)
data = [l.split(" -> ") for l in data]
data = [tuple(Point.from_str(p) for p in ps) for ps in data]

# For part 1, only want non-diagonal lines
straights = [ps for ps in data if not_diagonal(*ps)]
points = [p for ps in straights for p in expand_line(*ps)]
point_counts = Counter(points)

# Part 1
n_intersections = len([v for v in point_counts.values() if v > 1])
print("Part 1:", n_intersections)

print("===")
