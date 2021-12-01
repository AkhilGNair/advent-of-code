from pathlib import Path


def read(path="input.txt", cast_as=int):
    l = Path(path).read_text().strip().split("\n")
    return [cast_as(i) for i in l]
