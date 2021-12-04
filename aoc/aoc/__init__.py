from pathlib import Path


def read(path="input.txt", cast_as=int, sep="\n"):
    l = Path(path).read_text().strip().split(sep)
    return [cast_as(i) for i in l]
