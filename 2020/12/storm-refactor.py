from pathlib import Path


# nav = ["F10", "N3", "F7", "R90", "F11"]
nav = Path("input.txt").read_text().strip().split("\n")


def parse(inst):
    return inst[:1], int(inst[1:])


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rotate(self, direction, by):
        by = int(by / 90)

        if direction == "R":
            for _ in range(by):
                self.x, self.y = self.y, -self.x

        elif direction == "L":
            for _ in range(by):
                self.x, self.y = -self.y, self.x

    def move(self, direction, by):
        if direction == "E":
            self.x += by
        elif direction == "W":
            self.x -= by
        elif direction == "N":
            self.y += by
        elif direction == "S":
            self.y -= by
        else:
            raise ValueError()

    @property
    def manhattan_dist(self):
        return abs(self.x) + abs(self.y)

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"


waypoint = Point(x=10, y=1)
ship = Point(x=0, y=0)

for cmd in nav:
    direction, by = parse(cmd)

    if direction in {"L", "R"}:
        waypoint.rotate(direction=direction, by=by)

    elif direction == "F":
        ship.x += by * waypoint.x
        ship.y += by * waypoint.y

    else:
        waypoint.move(direction=direction, by=by)

    print(ship, waypoint)


print(ship.manhattan_dist)
