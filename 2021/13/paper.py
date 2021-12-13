from aoc import Point, read

from functools import reduce


data = read("input.txt", cast_as=str, sep="\n")
DELIM = data.index("")

points = [Point(*map(int, p.split(","))) for p in data[:DELIM]]
folds = [f.replace("fold along ", "") for f in data[(DELIM + 1) :]]


def make_fold(points, fold):
    axis, pos = fold.split("=")
    pos = int(pos)

    for p in points:
        px = (2 * pos - p.x) if (axis == "x") and (p.x > pos) else p.x
        py = (2 * pos - p.y) if (axis == "y") and (p.y > pos) else p.y
        yield Point(px, py)


def printer(points):
    for y in range(10):
        ans = ""
        for x in range(60):
            ans += "#" if Point(x, y) in points else "."
        print(ans)


printer(set(reduce(make_fold, folds, points)))
