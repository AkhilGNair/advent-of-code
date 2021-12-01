from pathlib import Path

xmas = Path("input.txt").read_text().strip().split("\n")
xmas = list(map(int, xmas))

WINDOW = 25


def find(find, summands):
    for a in summands:
        for b in summands:
            total = a + b
            if total == find and a != b:
                return True
    return False


def exploit(target):
    window = 2
    while True:
        for i in range(len(xmas) - window):
            block = xmas[i : (i + window)]
            if target == sum(block):
                return block
        window += 1


def stream():
    for i in range(len(xmas)):
        if i < WINDOW:
            continue

        summands = xmas[(i - WINDOW + 1) : (i + 1)]
        target = xmas[i + 1]

        if not find(target, summands):
            return exploit(target)


block = stream()
print(min(block) + max(block))
