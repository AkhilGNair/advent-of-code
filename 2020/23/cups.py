from nodelist import NodeList

test = "389125467"
input = "784235916"

N_CUPS = 1000000


def destination(current, cups):
    i = 1
    d = current - i

    if d == 0:
        d += HIGH

    while d not in cups:
        i += 1
        d = (current - i) % HIGH

        if d == 0:
            d += HIGH

    return d


data = list(map(int, input))
data = data + list(range(N_CUPS + 1))[10:]

HIGH = max(data)
MOVES = 10000000

cups = NodeList(data)


def move():

    current = cups[cups.pointer]

    next1 = cups[current.next]
    cup1 = cups.pop(next1.key)
    next2 = cups[next1.next]
    cup2 = cups.pop(next2.key)
    next3 = cups[next2.next]
    cup3 = cups.pop(next3.key)

    d = destination(current.key, cups)

    cups.insert(index=d, key=cup3)
    cups.insert(index=d, key=cup2)
    cups.insert(index=d, key=cup1)

    cups.pointer = cups[cups.pointer].next


for i in range(MOVES):
    # print(cups)
    move()

print("-- final --")
# print(cups)

cup1 = cups[1]
nxt1 = cups[cup1.next]
nxt2 = cups[nxt1.next]
