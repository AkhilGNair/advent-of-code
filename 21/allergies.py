from pathlib import Path
import json
from itertools import groupby

test = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)"""


# Note: this is a generator function
def parse(text):
    for line in text.strip().split("\n"):
        ingredients, allergens = line.strip(")").split(" (contains ")
        allergens = allergens.split(", ")
        ingredients = ingredients.split(" ")

        for allergen in allergens:
            yield (allergen, ingredients)


def first(x):
    return x[0]


text = Path("input.txt").read_text()

data = list(parse(text))
ingredients = sum([line.split(" (")[0].split(" ") for line in text.split("\n")], [])

allergens = {k: list(set(t[1]) for t in v) for k, v in groupby(sorted(data), first)}
allergens = {k: set.intersection(*v) for k, v in allergens.items()}

words = {}

while allergens:

    found = {k for k, v in allergens.items() if len(v) == 1}

    for allergen in found:
        words[allergen] = allergens.pop(allergen).pop()

    allergens = {k: v.difference(words.values()) for k, v in allergens.items()}

print(len([i for i in ingredients if i not in words.values()]))
print(json.dumps(words, indent=2))

# for food in $(python allergies.py | grep '"' | sort | cut -d'"' -f4); do echo -n $food","; done
