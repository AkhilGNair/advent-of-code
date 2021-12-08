import aoc


LETTERS = "abcdefg"
DISPLAY = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}
SIMPLE = {1, 4, 7, 8}

# Set because simple digits are unique length
LEN_SIMPLE = {len(DISPLAY[digit]) for digit in SIMPLE}
SIMPLE_LEN_TO_DIGIT = {len(v): k for k, v in DISPLAY.items() if k in SIMPLE}


def separate(s):
    return s.split(" | ")


def n_simple_digits(stream):
    digits = stream.split(" ")
    return len([SIMPLE_LEN_TO_DIGIT[len(d)] for d in digits if len(d) in LEN_SIMPLE])


def diff(big, small):
    return set(big).difference(small).pop()


def as_digit(*args):
    return "".join(args)


def find_map(inputs):
    digits = inputs.split(" ")
    counts = {inputs.count(l): l for l in LETTERS}

    m = {SIMPLE_LEN_TO_DIGIT.get(len(d), None): d for d in digits}
    m.pop(None)

    T = diff(m[7], m[1])
    L1 = counts[6]
    L2 = counts[4]
    R2 = counts[9]
    R1 = diff(m[1], R2)
    M = diff(m[4], {L1, R1, R2})
    B = diff(m[8], {T, L1, L2, R2, R1, M})

    map = {
        0: as_digit(T, L1, R1, L2, R2, B),
        1: as_digit(R1, R2),
        2: as_digit(T, R1, M, L2, B),
        3: as_digit(T, R1, M, R2, B),
        4: as_digit(L1, M, R1, R2),
        5: as_digit(T, L1, M, R2, B),
        6: as_digit(T, L1, M, L2, R2, B),
        7: as_digit(T, R1, R2),
        8: as_digit(T, L1, R1, M, L2, R2, B),
        9: as_digit(T, L1, R1, M, R2, B),
    }

    return map


def output_digit(signal, map):
    return [k for k, v in map.items() if set(v) == set(signal)].pop()


def decode_output(inputs, outputs):
    map = find_map(inputs)
    digits = (str(output_digit(o, map)) for o in outputs.split(" "))
    return int("".join(digits))


data = aoc.read("input.txt", cast_as=str, sep="\n")
data = [separate(s) for s in data]
print(sum(decode_output(*io) for io in data))
