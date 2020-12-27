MOD = 20201227

subject_number = 7

PUB_DOOR = 7573546
PUB_CARD = 17786549

RAINBOW = {0: 1}


def naive_handshake(subject, loop):
    val = 1
    for _ in range(loop):
        val *= subject
        val = val % MOD
    return val


def handshake(subject, loop):
    val = (RAINBOW[loop - 1] * subject) % MOD
    RAINBOW[loop] = val
    return val


def search(target, subject):
    i = 0
    while True:
        i += 1

        if i % 10000 == 0:
            print(i)

        key = handshake(subject, i)
        if key == target:
            return i


loop_card = search(PUB_CARD, subject=7)

# 10985209  # door loop
# 925199  # card loop

print(naive_handshake(PUB_DOOR, loop_card))