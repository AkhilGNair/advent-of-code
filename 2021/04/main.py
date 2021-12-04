import re
from collections import namedtuple

import aoc

Point = namedtuple("Point", ["x", "y"])

numbers, *cards = aoc.read(path="input.txt", sep="\n\n", cast_as=str)
numbers = numbers.split(",")


def get_x(i, n):
    return i - ((i // n) * n)


def get_y(i, n):
    return i // n


class Card:

    EXPECTED = {0, 1, 2, 3, 4}

    def __init__(self, data):
        ns = re.findall(r"[0-9]+", data)
        self.data = {v: Point(get_x(k, 5), get_y(k, 5)) for k, v in enumerate(ns)}
        self.complete = False

    def strike(self, n):
        try:
            self.data.pop(n)
        except KeyError:
            # Boards don't have all numbers
            pass

        if self.h_line_found() or self.v_line_found():
            self.complete = True

    def h_line_found(self):
        return not (self.EXPECTED == {p.y for p in self.data.values()})

    def v_line_found(self):
        return not (self.EXPECTED == {p.x for p in self.data.values()})

    def score(self, n):
        return int(n) * sum(int(i) for i in self.data.keys())


print("===")

cards = [Card(data=data) for data in cards]
for n in numbers:
    [card.strike(n) for card in cards]

    for card in cards:
        if card.complete:
            print("BINGO!", card.score(n))

            # Uncomment for part 1
            # import sys
            # sys.exit(0)

    cards = [card for card in cards if not card.complete]
    if not cards:
        break
