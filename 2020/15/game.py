from collections import defaultdict, deque
from functools import partial

twos = partial(deque, maxlen=2)

s = [0, 8, 15, 2, 12, 1, 4]
history = defaultdict(twos, {k: twos([i + 1]) for i, k in enumerate(s)})
turn = len(s)
spoken = s[-1]

while True:

    turn += 1
    val = history[spoken]
    spoken = 0 if len(val) < 2 else val[1] - val[0]
    history[spoken].append(turn)

    if turn == 2020:
        break

print(spoken)
