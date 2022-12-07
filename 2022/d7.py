from pathlib import Path

LIMIT = 100000
PROMPT = "$"

cmds = Path("t7.txt").read_text().strip().split("\n")

path = []
du = {}

for cmd in cmds:
    if cmd.startswith(PROMPT):
        cmd = cmd[2:]
        if cmd.startswith("cd"):
            dir = cmd[3:].strip()
            if dir == "..":
                path.pop()
                print(f"{path=}")
            else:
                path.append(dir)
                print(f"Initialising {dir=}")
                du[dir] = 0
                print(f"{path=}")
    elif cmd.startswith("dir"):
        dir = cmd[4:].strip()
        print(f"Listed {dir=}")
    else:
        size, filename = cmd.split(" ")
        for p in path:
            du[p] += int(size)

print(du)

print(sum(s for s in du.values() if s <= LIMIT))
