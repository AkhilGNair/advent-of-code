from collections import Counter, defaultdict

import aoc


def pairwise(s):
    """Not on python 3.10."""
    while True:
        try:
            a, b, *tail = s
        except ValueError:
            return
        yield a + b
        s = [b] + tail


polymer, _, *rules = aoc.read("input.txt", cast_as=str, sep="\n")
final = polymer[-1]  # To add the last letter into the counts at the end
rules = dict(pair.split(" -> ") for pair in rules)

# Initialise
poly = Counter(pairwise(polymer))

# Iterate simultaneously
for _ in range(40):
    new = defaultdict(int)
    for pair in list(poly):
        n = poly[pair]
        insertion = rules[pair]
        new[pair[0] + insertion] += n
        new[insertion + pair[1]] += n
    poly = new

# Total up the first letter of each pair
counts = Counter()
for pair, n in poly.items():
    counts[pair[0]] += n

# Add the final letter back in
counts[final] += 1

freq = counts.most_common()
_, high = freq[0]
_, low = freq[-1]

print(high - low)
