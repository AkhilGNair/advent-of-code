from pathlib import Path
from typing import NamedTuple
from enum import Enum

NOP = "nop"
JMP = "jmp"
ACC = "acc"


class ExitCode(Enum):
    Success = 1
    Loop = 2
    Skipped = 3


class Instruction(NamedTuple):
    opr: str
    val: int


def parse(text):
    for i, instruction in enumerate(text):
        opr, val = instruction.split(" ")
        yield (i, Instruction(opr, int(val)))


def boot(instructions, hack=False):
    accumulator = 0
    offset = 0
    visited = set()

    if hack is not False:
        corrupt = instructions[hack]
        if corrupt.opr == NOP:
            instructions[hack] = Instruction(JMP, corrupt.val)
        elif corrupt.opr == JMP:
            instructions[hack] = Instruction(NOP, corrupt.val)
        else:
            return ExitCode.Skipped, accumulator

    while True:
        try:
            opr, val = instructions[offset]
        except KeyError:
            return ExitCode.Success, accumulator

        if opr == JMP:
            offset += val

        elif opr == ACC:
            accumulator += val
            offset += 1

        elif opr == NOP:
            offset += 1

        else:
            raise ValueError

        n = len(visited)
        visited.add(offset)
        if n == len(visited):
            return ExitCode.Loop, accumulator


bootcode_text = Path("input.txt").read_text().strip().split("\n")
bootcode = dict(parse(bootcode_text))

print(boot(bootcode.copy()))

for i in bootcode.keys():
    exit_code, accumulator = boot(bootcode.copy(), hack=i)
    if exit_code == ExitCode.Success:
        print((exit_code, accumulator))
