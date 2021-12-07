import aoc

data = aoc.read("input.txt", sep="\n", cast_as=str).pop()

DAYS = 80
mapper = str.maketrans("876543210", "765432106")

for day in range(DAYS):
    n_new_crabs = data.count("0")
    data = data.translate(mapper) + (",8" * n_new_crabs)

print(data.count(",") + 1)

