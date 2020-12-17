from pathlib import Path
from collections import deque

rules = Path("input.txt").read_text().strip().split("\n")


def get_parent_bag(rule):
    return " ".join(rule.split(" ")[:2])


def parse_rule(rule):
    parent = get_parent_bag(rule)
    children = []
    contents = rule.split("contain ")[1]

    if "no other bags" in contents:
        return (parent, children)

    contents = contents.strip(".")
    contents = contents.split(", ")

    for desc in contents:
        desc = desc.strip("s")
        desc = desc.replace(" bag", " ")
        desc = desc.strip(" ")
        n, *adjs = desc.split(" ")
        bag_kind = " ".join(adjs)
        children.extend([bag_kind] * int(n))

    return (parent, children)


def get_containing_bags():
    stack = deque(["shiny gold"])
    while stack:
        bag = stack.pop()
        containing_bags = {get_parent_bag(rule) for rule in rules if bag in rule}
        containing_bags.remove(bag)
        for containing_bag in containing_bags:
            print(containing_bag)
            yield containing_bag
            stack.appendleft(containing_bag)


# print(len(set(get_containing_bags())))

BAGS = dict([parse_rule(rule) for rule in rules])

# print(BAGS)


def count():
    counter = 0
    stack = deque(["shiny gold"])
    while stack:
        bag = stack.pop()
        children = BAGS[bag]
        counter += len(children)
        stack.extendleft(children)
    return counter


print(count())
