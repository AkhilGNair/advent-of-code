from aoc import Point, read


data = read("input.txt", cast_as=str, sep="\n")

OTHER_AXIS = {"x": "y", "y": "x"}

DELIM = data.index("")

points = data[:DELIM]
points = [Point(*map(int, p.split(","))) for p in points]
DIMX, DIMY = max(p.x for p in points), max(p.y for p in points)

folds = data[(DELIM + 1) :]
folds = [f.replace("fold along ", "") for f in folds]


def make_fold(fold, points):
    axis, pos = fold.split("=")
    other = OTHER_AXIS[axis]
    pos = int(pos)

    for p in points:
        if p[axis] > pos:
            data = {axis: 2 * pos - p[axis], other: p[other]}
            yield Point(**data)
        else:
            yield p


for fold in folds:
    points = set(make_fold(fold, points))


def printer(points):
    for y in range(10):
        print("\n", end="")
        for x in range(60):
            symbol = "#" if Point(x, y) in points else "."
            print(symbol, end="")


printer(points)