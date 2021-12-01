import aoc


l = aoc.read()

def count(l):
    return sum(b > a for a, b in zip(l, l[1:]))

print(count(l))

# Window of width 3
w = [sum(xs) for xs in zip(l, l[1:], l[2:])]

print(count(w))

