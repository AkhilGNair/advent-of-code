from pathlib import Path
from collections import defaultdict, deque
import math


adapters = [int(s) for s in Path("test.txt").read_text().strip().split("\n")]
adapters.append(0)
adapters.sort()

BUILT_IN_JUMP = 3


def find_jumps(adapters):
    next_adapters = adapters.copy()
    next_adapters = next_adapters[1:]
    next_adapters.append(max(adapters) + BUILT_IN_JUMP)

    for adapter, next_adapter in zip(adapters, next_adapters):
        yield next_adapter - adapter


jumps = list(find_jumps(adapters.copy()))
print(jumps.count(1), jumps.count(3), jumps.count(1) * jumps.count(3))
print(jumps)


def find_connections(adapters):
    connections = defaultdict(list)

    for adapter in adapters:
        for next_adapters in adapters:
            if 0 < next_adapters - adapter <= 3:
                connections[adapter].append(next_adapters)

    return connections


conns = find_connections(adapters)


def find_cliques(conns):
    clique = set()
    for choices in conns.values():
        if len(choices) > 1:
            clique.update(choices)
        else:
            if clique:
                yield clique
            clique = set()


cliques = list(find_cliques(conns))


def map_clique(clique):
    start = min(clique) - 1
    end = max(clique)
    paths = deque([[start]])

    while paths:

        path = paths.pop()
        current_node = path[-1]
        nodes = conns[current_node]

        for node in nodes:
            route = path + [node]
            if node == end:
                yield route
            else:
                paths.appendleft(route)


print(math.prod(len(list(map_clique(clique))) for clique in cliques))


# def combn(adapters):
#     """ Works, but is too slow!"""
#     paths = deque([[max(adapters)]])

#     while paths:
#         path = paths.pop()
#         current_node = path[0]
#         nodes = [node for node in adapters if 0 < current_node - node <= 3]

#         if not nodes:
#             yield path

#         for node in nodes:
#             paths.appendleft([node] + path)


# print(len(list(combn(adapters))))


paths = defaultdict(int)
paths[0] = 1

for adapter in adapters[1:]:
    paths[adapter] = sum(paths[adapter - (i + 1)] for i in range(3))

paths