from pathlib import Path
from typing import NamedTuple

layout = Path("input.txt").read_text().strip().split("\n")

MAX_Y = len(layout)
MAX_X = len(layout[0])

DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
EMPTY = "L"
OCCUPIED = "#"
FLOOR = "."
WALL = "|"


def print_layout(chairs):
    print(chr(27) + "[2J")
    for i, x in enumerate(chairs.values()):
        if i % MAX_X == 0:
            print("\n", end="")
        print(x, end="")
    print("\n")


class Chair(NamedTuple):
    x: int
    y: int


def _adj(chair, chairs):
    for direction in DIRECTIONS:
        dx, dy = direction
        new_x = chair.x
        new_y = chair.y
        while True:
            new_x, new_y = new_x + dx, new_y + dy

            try:
                status = chairs[Chair(new_x, new_y)]
            except KeyError:
                yield WALL
                break

            if status != FLOOR:
                yield status
                break


def adj(chair, chairs):
    return list(_adj(chair, chairs))


def might_occupied(chair, chairs):
    """ If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied."""
    return OCCUPIED if adj(chair, chairs).count(OCCUPIED) == 0 else EMPTY


def might_empty(chair, chairs):
    """ If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty."""
    return EMPTY if adj(chair, chairs).count(OCCUPIED) >= 5 else OCCUPIED


def simulate(chairs):
    new_chairs = {}
    for chair, status in chairs.items():
        if status == FLOOR:
            new_chairs[chair] = FLOOR

        if status == EMPTY:
            new_chairs[chair] = might_occupied(chair, chairs)

        if status == OCCUPIED:
            new_chairs[chair] = might_empty(chair, chairs)

    return new_chairs


chairs = {}
for j, col in enumerate(layout):
    for i, row in enumerate(col):
        chairs[Chair(i, j)] = row

new_chairs = simulate(chairs)

while chairs != new_chairs:
    chairs = new_chairs
    new_chairs = simulate(chairs)
    # print_layout(new_chairs)

print(list(new_chairs.values()).count(OCCUPIED))
