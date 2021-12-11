from pathlib import Path
from typing import NamedTuple


def read(path="input.txt", cast_as=int, sep="\n"):
    l = Path(path).read_text().strip().split(sep)
    return [cast_as(i) for i in l]

def x(i, n):
    """Returns the x position of an index in a square of length n."""
    return i - ((i // n) * n)


def y(i, n):
    """Returns the y position of an index in a square of length n."""
    return i // n

class Point(NamedTuple):
    x: int
    y: int

    @classmethod
    def from_index(self, i:int , n: int) -> "Point":
        return Point(x(i, n), y(i, n))

