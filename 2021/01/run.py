from pathlib import Path


l = Path("test.txt").read_text().strip().split("\n")
l = [int(n) for n in l]

print(sum([b > a for a, b in zip(l, l[1:])]))

# Window of width 3
w = [sum(xs) for xs in zip(l, l[1:], l[2:])]

print(sum([b > a for a, b in zip(w, w[1:])]))

