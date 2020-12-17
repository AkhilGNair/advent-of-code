from pathlib import Path


nav = ["F10", "N3", "F7", "R90", "F11"]
nav = Path("input.txt").read_text().strip().split("\n")


def parse(inst):
    cmd, *mag = inst
    return cmd, int("".join(mag))


class Ship:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.wx = 10
        self.wy = 1

    def turn(self, angle):
        direction, amount = parse(angle)
        by = int(amount / 90)

        if direction == "R":
            for _ in range(by):
                self.wx, self.wy = self.wy, -self.wx

        elif direction == "L":
            for _ in range(by):
                self.wx, self.wy = -self.wy, self.wx

        else:
            raise ValueError()

    def do(self, inst: str):

        if inst.startswith("L") or inst.startswith("R"):
            self.turn(inst)
            return

        if inst.startswith("F"):
            _, by = parse(inst)
            self.x += by * self.wx
            self.y += by * self.wy
            return

        direction, by = parse(inst)

        if direction == "E":
            self.wx += by
        elif direction == "W":
            self.wx -= by
        elif direction == "N":
            self.wy += by
        elif direction == "S":
            self.wy -= by
        else:
            raise ValueError()

    @property
    def manhattan_dist(self):
        return abs(self.x) + abs(self.y)

    def __repr__(self):
        return f"Ship(x={self.x}, y={self.y})"


ship = Ship()

for cmd in nav:
    ship.do(cmd)

print(ship.manhattan_dist)