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


def visited_nodes(path: List[Edge]) -> Set[str]:
    return set(chain(*path))


def is_small_cave(node):
    return node.lower() == node


def filter(edges, node):
    return set(e for e in edges if e.from_ == node)


def traverse(edges):
    stack = deque([path] for path in filter(edges, START))

    while stack:
        path = stack.pop()
        current_node = path[-1].to_  # CHECK THIS
        next_edges = filter(edges, current_node)

        for edge in next_edges:
            current_path = path.copy()
            to_node = edge.to_
            current_path.append(edge)

            if to_node == END:
                yield current_path

            if is_small_cave(to_node) and (to_node in visited_nodes(path)):
                pass
            else:
                stack.appendleft(current_path)


data = aoc.read("input.txt", sep="\n", cast_as=str)

edges = [Edge.from_str(e) for e in data]
backward_edges = [Edge(e.to_, e.from_) for e in edges]

edges = edges + backward_edges
edges = [e for e in edges if e.to_ != START and e.from_ != END]

nodes = visited_nodes(edges)

paths = list(traverse(edges))
