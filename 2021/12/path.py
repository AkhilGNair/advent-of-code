from collections import deque
from typing import NamedTuple, Set, List
from itertools import chain

import aoc

START = "start"
END = "end"


class Edge(NamedTuple):
    from_: str
    to_: str

    @classmethod
    def from_str(self, s: str) -> "Edge":
        return Edge(*s.split("-"))


def visited_nodes(path: List[Edge]) -> List[str]:
    for edge in path:
        yield edge.from_


def is_small_cave(node: str) -> bool:
    return node.lower() == node and (node not in {START, END})


def get_current_node(path: List[Edge]) -> str:
    return path[-1].to_


def filter(edges: List[Edge], node: str) -> List[Edge]:
    return set(e for e in edges if e.from_ == node)


def invalid_small_cave(to_node: str, path: List[Edge], special_cave: str) -> bool:
    visited = list(visited_nodes(path))

    if to_node == special_cave and visited.count(special_cave) < 2:
        return False

    elif visited.count(to_node) < 1:
        return False

    else:
        return True


def traverse_with_special_small_cave(
    special_cave: str, stack: deque, edges: List[Edge]
):
    while stack:
        path = stack.pop()
        current_node = get_current_node(path)
        next_edges = filter(edges, current_node)

        for edge in next_edges:
            current_path = path.copy()
            to_node = edge.to_
            current_path.append(edge)

            if to_node == END:
                yield current_path

            if is_small_cave(to_node) and invalid_small_cave(
                to_node, path, special_cave
            ):
                pass
            else:
                stack.appendleft(current_path)


def traverse(edges, nodes):
    starts = deque([path] for path in filter(edges, START))
    stacks = {n: starts.copy() for n in nodes if is_small_cave(n)}

    for special_cave, stack in stacks.items():
        yield traverse_with_special_small_cave(special_cave, stack, edges)


def path_as_route(path) -> str:
    return ",".join([e.from_ for e in path] + ["end"])


data = aoc.read("input.txt", sep="\n", cast_as=str)

edges = [Edge.from_str(e) for e in data]
backward_edges = [Edge(e.to_, e.from_) for e in edges]

edges = edges + backward_edges
edges = [e for e in edges if e.to_ != START and e.from_ != END]

nodes = set(chain(*edges))
paths = chain(*traverse(edges, nodes))
routes = set(path_as_route(path) for path in paths)

print(len(routes))