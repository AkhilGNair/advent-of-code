from pathlib import Path
import math
from collections import defaultdict

data = Path("input.txt").read_text()

test = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""

test2 = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9"""


def parse(text):
    lines = [line for line in text.split("\n") if line]
    idx_mine = lines.index("your ticket:")
    idx_near = lines.index("nearby tickets:")
    return lines[:idx_mine], lines[idx_mine + 1 : idx_near], lines[idx_near + 1 :]


def parse_rule(rule):
    prop, vals = rule.split(": ")
    data = vals.split(" ")
    min1, max1 = map(int, data[0].split("-"))
    min2, max2 = map(int, data[2].split("-"))
    return (prop, list(range(min1, max1 + 1)) + list(range(min2, max2 + 1)))


rules, mine, near = parse(data)
mine = mine[0]
rules = dict(parse_rule(rule) for rule in rules)
valid_values = {i for l in rules.values() for i in l}


def validate(tickets):
    for ticket in tickets:
        vals = list(map(int, ticket.split(",")))
        if all(val in valid_values for val in vals):
            yield vals


valid_tickets = list(validate(near))
columns = list(map(list, zip(*valid_tickets)))

soln = defaultdict(set)
for rule_name, allowed in rules.items():
    for col_num, data in enumerate(columns):
        if all(d in allowed for d in data):
            soln[col_num].add(rule_name)

solved = dict()
while soln:
    found = {k: v.pop() for k, v in soln.items() if len(v) == 1}
    print(found)

    for col_num, prop in found.items():
        solved[col_num] = prop
        soln.pop(col_num)

    for prop in found.values():
        for remaining in soln:
            try:
                soln[remaining].remove(prop)
            except KeyError:
                pass


departs = [k for k, v in solved.items() if v.startswith("depart")]
ticket = list(map(int, mine.split(",")))


print(math.prod(ticket[i] for i in departs))
