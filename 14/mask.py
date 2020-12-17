from collections import defaultdict, deque
import re
from pathlib import Path

data = Path("input.txt").read_text()

test = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
"""

test2 = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
"""

PTN_NUM = r"[0-9]+"
MASK_LEN = 36
MEMORY = defaultdict(str)


def binary(dec):
    return list(format(dec, f"0{MASK_LEN}b"))


def get_mask(mask):
    return {i: b for i, b in enumerate(mask)}


def apply_mask(dec, mask):
    val = binary(dec)
    for i, m in mask.items():
        val[i] = val[i] if m == "0" else m
    return "".join(val)


def get_addresses(address):
    addesses = deque([address])
    address = "X"
    while "X" in address:
        address = addesses.pop()
        addesses.appendleft(address.replace("X", "1", 1))
        addesses.appendleft(address.replace("X", "0", 1))
    return addesses


def read(inst):
    data = inst.strip().split("\n")
    for line in data:
        key, val = line.split(" = ")
        if key == "mask":
            mask = get_mask(val)
        elif key.startswith("mem"):
            address_dec = int(re.search(PTN_NUM, key)[0])
            address = apply_mask(address_dec, mask)

            addresses = get_addresses(address)

            for a in addresses:
                MEMORY[a] = int(val)
        else:
            raise ValueError()


read(data)
print(sum(MEMORY.values()))