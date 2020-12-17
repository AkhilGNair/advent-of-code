from pathlib import Path
from typing import NamedTuple

RAD = {-1, 0, 1}
ACTIVE = "#"
INACTIVE = "."

test = """.#.
..#
###"""

data = Path("input.txt").read_text()


class Point(NamedTuple):
    x: int
    y: int
    z: int
    w: int


def neighbours(p):
    def _neighbours():
        for x in RAD:
            for y in RAD:
                for z in RAD:
                    for w in RAD:
                        if abs(x) + abs(y) + abs(z) + abs(w) > 0:
                            yield Point(p.x + x, p.y + y, p.z + z, p.w + w)

    return list(_neighbours())


def read(text):
    for y, row in enumerate(text.split("\n")):
        for x, val in enumerate(row):
            yield Point(x=x - 1, y=y - 1, z=0, w=0), val


def expand_space(points):
    s = set()
    for p in points:
        s.update(neighbours(p))
    return {n: points.get(n, INACTIVE) for n in s}


def cycle(times, starting, new_space={}):
    space = starting
    for _ in range(times):
        grid = expand_space(space)
        for point, state in grid.items():

            neighbour_states = [grid.get(p, INACTIVE) for p in neighbours(point)]

            if state == ACTIVE:
                new_space[point] = ACTIVE if neighbour_states.count(ACTIVE) in {2, 3} else INACTIVE

            if state == INACTIVE:
                new_space[point] = ACTIVE if neighbour_states.count(ACTIVE) == 3 else INACTIVE

        space = new_space
        new_space = {}

    return space


print(list(cycle(6, dict(read(data))).values()).count(ACTIVE))