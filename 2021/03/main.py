from typing import List

import aoc

data = aoc.read(path="test.txt", cast_as=str)
N = len(data[0])

mapper = str.maketrans("01", "10")

def most_common_bit(l: List[str]) -> str:
    n = len(l)
    ones = len([i for i in l if i == "1"])
    return "1" if ones > n/2 else "0"

def to_decimal(bin: str) -> int:
    return int(bin, 2)

def gamma(data):

    bits = ""
    for i in range(N):
        bits += most_common_bit([s[i] for s in data])

    return bits

def epsilon(gamma):
    return gamma.translate(mapper)


print(to_decimal(gamma(data)) * to_decimal(epsilon(gamma(data))))





print("=====")
