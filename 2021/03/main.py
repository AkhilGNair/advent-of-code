from typing import List, Tuple

import aoc


data = aoc.read(path="input.txt", cast_as=str)

N = len(data[0])
mapper = str.maketrans("01", "10")


def dec(bin: str) -> int:
    return int(bin, 2)


def most_common_bit(l: List[str]) -> str:
    n = len(l)
    ones = len([i for i in l if i == "1"])
    return "1" if ones >= n / 2 else "0"


def gamma(data):

    bits = ""
    for i in range(N):
        bit = most_common_bit([s[i] for s in data])
        bits += bit

    return bits


def epsilon(gamma):
    return gamma.translate(mapper)


print("=== Part 1 ===")
print(dec(gamma(data)) * dec(epsilon(gamma(data))))


def filter(data, pos, system):
    bit = most_common_bit([s[pos] for s in data])
    bit = bit.translate(mapper) if system == "co2" else bit
    return [s for s in data if s[pos] == bit]


def system_rating(data, system):
    pos = 0
    while True:
        data = filter(data, pos=pos, system=system)
        if len(data) == 1:
            return data.pop()
        pos += 1


print("=== Part 2 ===")
print(dec(system_rating(data, "o2")) * dec(system_rating(data, "co2")))
