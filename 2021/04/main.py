import re
from collections import namedtuple

import aoc

Point = namedtuple("Point", ["x", "y"])

numbers, *cards = aoc.read(path="input.txt", sep="\n\n", cast_as=str)
numbers = [int(n) for n in numbers.split(",")]

N = 5  # Bingo card length
PATTERN_NUM = r"[0-9]+"


def x(i, n=N):
    return i - ((i // n) * n)


def y(i, n=N):
    return i // n


class Card:

    ALL = set(range(N))

    def __init__(self, data):
        ns = re.findall(PATTERN_NUM, data)
        self.data = {int(v): Point(x(i), y(i)) for i, v in enumerate(ns)}
        self.complete = False

    def strike(self, n):
        try:
            self.data.pop(n)
        except KeyError:
            # Boards don't have all numbers
            pass

        if self.line_found("x") or self.line_found("y"):
            self.complete = True

    def line_found(self, axis):
        lines = {getattr(p, axis) for p in self.data.values()}
        return bool(self.ALL.difference(lines))

    def score(self, n):
        return n * sum(self.data)


print("===")

cards = [Card(data=data) for data in cards]
for n in numbers:
    [card.strike(n) for card in cards]

    for card in cards:
        if card.complete:
            print("BINGO!", card.score(n))

            # # Uncomment for part 1
            # import sys
            # sys.exit(0)

    cards = [card for card in cards if not card.complete]
    if not cards:
        break
