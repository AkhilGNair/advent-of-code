import aoc

data = aoc.read("input.txt", sep="\n", cast_as=str)

POINTS = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}
OPEN = {"(", "[", "{", "<"}
COMPS = {"}": "{", ")": "(", "]": "[", ">": "<"}

l = data[0]

from collections import deque


def validate(l: str):
    stack = deque()

    while l:
        head, *l = l
        if head in OPEN:
            stack.append(head)
        else:
            opener = stack.pop()
            if opener != COMPS[head]:
                return None  # return POINTS[head]

    return stack  # return None


# print(sum([points for l in data if (points := validate(l))]))

COMP_POINTS = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}


def score(remainder):
    stack = deque(remainder)
    score = 0
    while stack:
        bracket = stack.pop()
        score *= 5
        score += COMP_POINTS[bracket]
    return score


scores = [score(rem) for l in data if (rem := validate(l))]
scores.sort()
print(scores[(len(scores) - 1) // 2])
