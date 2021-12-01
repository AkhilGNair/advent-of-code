from pathlib import Path
import math

hill = Path("input.txt").read_text().strip().split("\n")

TREE = "#"
height = len(hill)


def slide(right, down):
    width = len(hill[0])
    x = 0
    y = 0
    trees = 0
    while y < height - 1:
        x += right
        x = x % width
        y += down
        if hill[y][x] == TREE:
            trees += 1

    return trees


print(slide(3, 1))

rights = [1, 3, 5, 7, 1]
downs = [1, 1, 1, 1, 2]

print(math.prod(map(slide, rights, downs)))
