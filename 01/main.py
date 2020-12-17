from pathlib import Path

expenses = [1721, 979, 366, 299, 675, 1456]
expenses = [int(s) for s in Path("input.txt").read_text().strip().split("\n")]

for item1 in expenses:
    for item2 in expenses:
        for item3 in expenses:
            if item1 + item2 + item3 == 2020:
                print(item1, item2, item3, item1 * item2 * item3)
