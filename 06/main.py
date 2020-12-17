from pathlib import Path

answers = Path("input.txt").read_text().strip().split("\n\n")
print(sum(len(set(s.replace("\n", ""))) for s in answers))


def everyone(group):
    people = [set(person) for person in group.split("\n")]
    return len(set.intersection(*people))


print(sum(everyone(group) for group in answers))
