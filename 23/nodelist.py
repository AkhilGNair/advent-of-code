def rotate(lst, n):
    return lst[n:] + lst[:n]


class Node:
    def __init__(self, key, prev, next):
        self.key = key
        self.prev = prev
        self.next = next

    def __iter__(self):
        for prop in (self.key, self.prev, self.next):
            yield prop

    def __repr__(self):
        return f"Node(key={self.key}, prev={self.prev}, next={self.next})"


class NodeList:
    def __init__(self, lst):
        self.map = {k: Node(k, p, n) for k, p, n in zip(lst, rotate(lst, -1), rotate(lst, 1))}
        self.pointer = self.__first = lst[0]

    def pop(self, key):
        k, p, n = self.map.pop(key)
        self.map[p].next = n
        self.map[n].prev = p
        return k

    def insert(self, index, key):
        tmp = self.map[index]
        nxt = self.map[tmp.next]
        self.map[index] = Node(tmp.key, tmp.prev, key)
        self.map[key] = Node(key, index, tmp.next)
        self.map[tmp.next] = Node(tmp.next, key, nxt.next)

    def __getitem__(self, key):
        return self.map[key]

    def __contains__(self, key):
        return key in self.map.keys()

    def traverse(self, key=None):
        node = self.__first if not key else key
        for _ in range(len(self.map)):
            yield self.map[node].key
            node = self.map[node].next

    def __repr__(self):
        return f"NodeList({list(self.traverse())})"
