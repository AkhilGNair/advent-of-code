from collections import defaultdict

import aoc

START = "start"
END = "end"

data = aoc.read("input.txt", sep="\n", cast_as=str)

nodes = defaultdict(set)
for edge in data:
    a, b = edge.split("-")
    nodes[a].add(b) if b != START else None
    nodes[b].add(a) if a != START else None
nodes.pop(END)


def traverse():
    explore = [(p, {START, p}) for p in nodes[START]]
    paths = 0

    while explore:
        head, visited = explore.pop()
        neighbours = nodes[head]
        for node in neighbours:
            if node == END:
                paths += 1
            elif node.islower() and (node in visited):
                paths += 0
            else:
                v = visited.copy()
                v.add(node)
                explore.append((node, v))

    return paths


def traverse2():
    explore = [(p, {START, p}, False) for p in nodes[START]]
    paths = 0

    while explore:
        head, visited, flag = explore.pop()
        neighbours = nodes[head]
        for node in neighbours:
            if node == END:
                paths += 1
            elif node.islower() and (node in visited):
                if flag:
                    paths += 0
                else:
                    v = visited.copy()
                    v.add(node)
                    explore.append((node, v, True))
            else:
                v = visited.copy()
                v.add(node)
                explore.append((node, v, flag))

    return paths


print(traverse())
print(traverse2())