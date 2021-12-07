from statistics import median

import aoc


data = aoc.read(sep=",", cast_as=int)
m = median(data)
fuel = sum(abs(x - m) for x in data)
