from pathlib import Path

cases = Path("input.txt").read_text().strip().split("\n")


def valid_for_range(case):
    policy, password = case.split(": ")
    range, letter = policy.split(" ")
    a, b = (int(s) for s in range.split("-"))

    n = password.count(letter)
    return n >= a and n <= b


def valid_for_position(case):
    policy, password = case.split(": ")
    range, letter = policy.split(" ")
    a, b = (int(s) for s in range.split("-"))

    chance1 = password[a - 1]
    chance2 = password[b - 1]

    if chance1 == letter and chance2 == letter:
        return False

    return chance1 == letter or chance2 == letter


def check_cases(cases, checker):
    for case in cases:
        if checker(case):
            yield case


print(len(list(check_cases(cases, checker=valid_for_range))))
print(len(list(check_cases(cases, checker=valid_for_position))))