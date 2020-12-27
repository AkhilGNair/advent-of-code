from collections import deque
from pathlib import Path

test = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
"""

test2 = """Player 1:
43
19

Player 2:
2
29
14
"""


def parse(text):
    decks = text.strip("\n").split("\n\n")
    for deck in decks:
        _, cards = deck.split(":\n")
        yield deque(map(int, cards.split("\n")))


data = Path("input.txt").read_text()
player1, player2 = parse(data)


def score(deck):
    return sum([(i + 1) * card for i, card in enumerate(reversed(deck))])


def combat(deck1, deck2):
    history = set()
    while deck1 and deck2:

        record = str(list(deck1)) + " | " + str(list(deck2))
        if record in history:
            return deck1, deck2, True

        history.add(record)

        c1 = deck1.popleft()
        c2 = deck2.popleft()

        l1 = len(deck1)
        l2 = len(deck2)

        if c1 <= l1 and c2 <= l2:
            d1 = deque(list(deck1.copy())[:c1])
            d2 = deque(list(deck2.copy())[:c2])
            r1, r2, check = combat(d1, d2)

            winner = r1 if len(r1) > len(r2) else r2
            winner = r1 if check else winner
            deck1.extend((c1, c2)) if winner == r1 else deck2.extend((c2, c1))

        else:

            winner = c1 if c1 > c2 else c2
            deck1.extend((c1, c2)) if winner == c1 else deck2.extend((c2, c1))

    return deck1, deck2, False


p1, p2, check = combat(player1, player2)

for player in (p1, p2):
    print("Final Deck:", player)
    print("Final Score:", score(player))
