import math
from collections import Counter, OrderedDict
from functools import reduce
from itertools import product
from pathlib import Path
from typing import NamedTuple

text = Path("input.txt").read_text().strip().split("\n\n")
WHITE = "#"


def first(x):
    return x[0]


def last(x):
    return x[-1]


def parse(data):
    for line in data:
        id, tile = line.split(":\n")
        yield id.split(" ")[1], [list(lst) for lst in tile.split("\n")]


def rotate(tile):
    return list(map(list, zip(*reversed(tile))))


def mirror(tile):
    return list(map(list, map(reversed, tile)))


def flip(tile):
    return list(reversed(mirror(tile)))


def encode(edge):
    return sum(pow(2, i) for i, p in enumerate(edge) if p == WHITE)


def get_edges(tile):
    elit = flip(tile)
    es = [first(tile), last(tile), map(first, tile), map(last, tile)]
    fs = [first(elit), last(elit), map(first, elit), map(last, elit)]
    return [encode(tile) for tile in es + fs]


tiles = dict(parse(text))
edges = {key: get_edges(tile) for key, tile in tiles.items()}
edge_occurances = Counter(e for lst in edges.values() for e in lst)

# If boundaries are unique the puzzle is simplified.
if {k for k, v in edge_occurances.items() if v > 2}:
    raise ValueError("Boundaries are not unique")

connecting_edges = {k for k, v in edge_occurances.items() if v == 2}
is_connection = lambda b: b in connecting_edges

# 4 because of mirroring
corners = {k for k, b in edges.items() if len(list(filter(is_connection, b))) == 4}
print(math.prod(map(int, corners)))


class Point(NamedTuple):
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


def p(s):
    mapper = str.maketrans(".#", "⬛⬜")
    for l in s:
        l = "".join(l)
        l = l.translate(mapper)
        print(l)


def edge(tile, side):
    if side == "north":
        boundary = first(tile)
    if side == "west":
        boundary = list(map(first, tile))
    if side == "south":
        boundary = last(tile)
    if side == "east":
        boundary = list(map(last, tile))
    return encode(boundary)


TRANSFORMATIONS = [
    tuple(),
    (rotate,),
    (rotate, rotate),
    (rotate, rotate, rotate),
    (mirror,),
    (mirror, rotate),
    (mirror, rotate, rotate, rotate),
    (mirror, rotate, rotate),
]


def transform(tile, transformations):
    for transformation in transformations:
        tile = transformation(tile)
    return tile


corner, *_ = [
    corner
    for corner in corners
    if is_connection(edge(tiles[corner], side="east"))
    and is_connection(edge(tiles[corner], side="south"))
]

puzzle = OrderedDict({Point(0, 0): tiles.pop(corner)})
x, y = 1, 0  # Next piece

# Solve the puzzle moving right. Go down at the end of the row.
while tiles:

    if x == 0:
        need = edge(puzzle[Point(x, y - 1)], side="south")
        matching_side = "north"
    else:
        need = edge(puzzle[Point(x - 1, y)], side="east")
        matching_side = "west"

    keys = list(tiles.keys())

    for key, transformations in product(keys, TRANSFORMATIONS):
        tile = tiles[key]
        orientation = transform(tile, transformations)
        found = edge(orientation, side=matching_side)

        if found == need:
            puzzle[Point(x, y)] = orientation
            x += 1
            tiles.pop(key)
            break
    else:
        x = 0
        y += 1


def dimensions(pixels):
    dim_x, dim_y = max(pixels)
    return dim_x + 1, dim_y + 1


def add_list(a, b):
    return [a[i] + b[i] for i in range(len(a))]


def assemble(pixel_map):
    pieces = list(pixel_map.values())
    dim_x, _ = dimensions(pixel_map.keys())
    rows = [pieces[x : (x + dim_x)] for x in range(0, len(pieces), dim_x)]
    for row in rows:
        yield reduce(add_list, row)


def snip(tile):
    return [r[1:-1] for r in tile[1:-1]]


picture = sum(assemble({k: snip(tile) for k, tile in puzzle.items()}), [])


TEXT_MONSTER = """
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
"""
monster = TEXT_MONSTER.split("\n")[1:-1]


def get_pixels(picture):
    for y, line in enumerate(picture):
        for x, val in enumerate(line):
            yield Point(x, y), val


monster_pixels = {p for p, v in get_pixels(monster) if v == WHITE}

monsters = 0

while not monsters:

    transformations = TRANSFORMATIONS.pop()
    orientation = transform(picture, transformations)

    picture_pixels = dict(get_pixels(orientation))
    dim_x, dim_y = dimensions(picture_pixels)

    for x in range(dim_x):
        for y in range(dim_y):
            root = Point(x, y)
            try:
                if all(picture_pixels[root + p] == WHITE for p in monster_pixels):
                    monsters += 1
                    for pixel in (root + p for p in monster_pixels):
                        picture_pixels.pop(pixel)
            except KeyError:
                pass


print(monsters)
print(list(picture_pixels.values()).count(WHITE))
