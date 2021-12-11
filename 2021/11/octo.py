from itertools import chain, product
from typing import List

from aoc import Point, read

data = read("input.txt", sep="\n\n", cast_as=str).pop()
N = data.index("\n")
data = data.replace("\n", "")

ADJ = {-1, 0, 1}
ADJ = [v for v in product(ADJ, ADJ) if v != (0, 0)]
ENOUGH_ENERGY = 9


def print_octos(octopodes):
    Y = 1
    for p, e in octopodes.items():
        if p.y == Y:
            print("\n", end="")
            Y += 1
        print(e if e <= ENOUGH_ENERGY else "x", end="")
    print("\n")


def neighbours(p: Point) -> List[Point]:
    return [Point(p.x + dx, p.y + dy) for dx, dy in ADJ]


def count_flashes(octopodes) -> int:
    return list(octopodes.values()).count(0)


def flash(octopodes):
    # Find all octos about to flash
    while (flashing_octos := [p for p, e in octopodes.items() if e > ENOUGH_ENERGY]) :

        # Set popped octo energy to 0
        for octo in flashing_octos:
            octopodes[octo] = 0

        # All adjacent octos who gain some energy
        all_neighbours = [neighbours(p) for p in flashing_octos]

        # Increase energy of neighbours all at once
        for q in chain(*all_neighbours):
            try:
                energy = octopodes[q]
                # An octo who just popped can't pop again
                if energy:
                    octopodes[q] += 1
            except KeyError:
                # Octo might be on the edge of the map
                pass

    return octopodes, count_flashes(octopodes)


def step(octopodes):
    octopodes = {p: e + 1 for p, e in octopodes.items()}
    return flash(octopodes)


octopodes = {Point.from_index(i, N): int(e) for i, e in enumerate(data)}

total_flashes = 0
for i in range(100):
    octopodes, flashes = step(octopodes)
    total_flashes += flashes

print("Part 1:", total_flashes)

octopodes = {Point.from_index(i, N): int(e) for i, e in enumerate(data)}

n_steps = 0
while True:
    octopodes, flashes = step(octopodes)

    if len(set(octopodes.values())) == 1:
        break

    n_steps += 1

print("Part 2:", n_steps + 1)
