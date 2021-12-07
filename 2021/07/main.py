from statistics import median, mean

import aoc


data = aoc.read("input.txt", sep=",", cast_as=int)
m = median(data)
fuel = sum(abs(x - m) for x in data)

print(f"Part 1 - total fuel:", int(fuel))


def triangle_fuel(x, m):
    t = -1 if x < m else 1
    return 0.5 * ((x - m) * (x - m + t))

min = None
for i in range(len(data)):
    fuel = sum(triangle_fuel(x, i) for x in data)
    if min is None or min > fuel:
        min = fuel

print(f"Part 2 - total fuel:", int(min))
