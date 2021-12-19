from typing import Union


class Node:
    def __init__(self, data, depth=0, parent=None):
        l, r = data
        self.depth = depth
        self.parent = parent

        self.l: Union[int, Node] = l if isinstance(l, int) else Node(l, depth + 1, self)
        self.r: Union[int, Node] = r if isinstance(r, int) else Node(r, depth + 1, self)

    def explode(self):
        if self.depth >= 4 and isinstance(self.l, int) and isinstance(self.r, int):
            l, r = self.l, self.r

            nr_node = self.next_right()
            if nr_node:
                if isinstance(nr_node.r, int):
                    nr_node.r += r
                else:
                    nr_node = nr_node.r
                    while isinstance(nr_node.l, Node):
                        nr_node = nr_node.l
                    nr_node.l += r

            nl_node = self.next_left()
            if nl_node:
                if isinstance(nl_node.l, int):
                    nl_node.l += l
                else:
                    nl_node = nl_node.l
                    while isinstance(nl_node.r, Node):
                        nl_node = nl_node.r
                    nl_node.r += l

            if self.parent.r == self:
                self.parent.r = 0
                return True

            if self.parent.l == self:
                self.parent.l = 0
                return True

            if self.parent.r != self and self.parent.l != self:
                wleknf

        return False

    def next_right(self):
        if self.parent is None:
            return None
        if self.parent.r != self:
            return self.parent
        return self.parent.next_right()

    def next_left(self):
        if self.parent is None:
            return None
        if self.parent.l != self:
            return self.parent
        return self.parent.next_left()

    def split(self):
        if isinstance(self.l, int) and self.l >= 10:
            l = self.l
            self.l = Node([l // 2, (l + 1) // 2], self.depth + 1, parent=self)
            return True

        if isinstance(self.l, Node):
            has_split = self.l.split()
            if has_split:
                return True

        if isinstance(self.r, int) and self.r >= 10:
            r = self.r
            self.r = Node([r // 2, (r + 1) // 2], self.depth + 1, parent=self)
            return True

        if isinstance(self.r, Node):
            has_split = self.r.split()
            if has_split:
                return True

        return False

    def __iter__(self):
        """Return pairs in the tree from left to right."""
        yield self

        if isinstance(self.l, Node):
            for node in self.l:
                yield node

        if isinstance(self.r, Node):
            for node in self.r:
                yield node

    def __add__(self, other):
        l = eval(str(self))
        r = eval(str(other))
        return Node([l, r])

    def __repr__(self):
        b = "[" if self.depth < 4 else "<"
        k = "]" if self.depth < 4 else ">"
        return f"{b}{self.l}, {self.r}{k}"

    def _reduce(self):
        for node in self:
            if node.explode():
                return False

        has_split = self.split()
        if has_split:
            return False

        return True

    def reduce(self):
        done = False
        while not done:
            done = self._reduce()
        return self


def check(in_, out_):
    assert eval(str(Node(in_).reduce())) == eval(out_)
    print("pass")


# check([[[[[9, 8], 1], 2], 3], 4], "[[[[0,9],2],3],4]")
# check([7, [6, [5, [4, [3, 2]]]]], "[7,[6,[5,[7,0]]]]")
# check([[6, [5, [4, [3, 2]]]], 1], "[[6,[5,[7,0]]],3]")
# check([[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]], "[[3,[2,[8,0]]],[9,[5,[7,0]]]]")

# check(
#     [[[[[4, 3], 4], 4], [7, [[8, 4], 9]]], [1, 1]], "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"
# )

import aoc

numbers = [Node(eval(n)) for n in aoc.read("input.txt", cast_as=str, sep="\n")]

acc, *numbers = numbers

for n in numbers:
    acc = acc + n
    acc.reduce()


def magnitude(node):
    while True:
        if isinstance(node.l, int) and isinstance(node.r, int):
            return (3 * node.l) + (2 * node.r)

        if isinstance(node.l, Node):
            node.l = magnitude(node.l)

        if isinstance(node.r, Node):
            node.r = magnitude(node.r)


print(magnitude(acc))

numbers = [Node(eval(n)) for n in aoc.read("input.txt", cast_as=str, sep="\n")]

max = 0

for i, n in enumerate(numbers):
    for j, m in enumerate(numbers):
        if i != j:
            new1 = magnitude((n + m).reduce())
            new2 = magnitude((m + n).reduce())

            if new1 > max:
                max = new1

            if new2 > max:
                max = new2
