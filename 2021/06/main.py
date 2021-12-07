import aoc

data = aoc.read("input.txt", sep="\n", cast_as=str).pop()

DAYS = 18
mapper = str.maketrans("876543210", "765432106")

for _ in range(DAYS):
    n_new_crabs = data.count("0")
    data = data.translate(mapper) + (",8" * n_new_crabs)

print("Part 1:", data.count(",") + 1)


from collections import Counter, defaultdict


data = aoc.read("input.txt", sep=",", cast_as=str)

DAYS = 256

data = defaultdict(int, Counter(data))
for i in range(9):
    data[str(i)]

for _ in range(DAYS):
    new_crabs = data["0"]
    data = {k.translate(mapper): v for k, v in data.items()}
    data["8"] = new_crabs
    data["6"] += new_crabs


print(sum(data.values()))
