from pathlib import Path

mapper = str.maketrans("BFRL", "1010")
seats = Path("input.txt").read_text().strip().split("\n")


def search(data):
    return int(data.translate(mapper), 2)


def seat_id(case):
    y, x = search(case[:7]), search(case[7:])
    return (y * 8) + x


print(max(seat_id(case) for case in seats))

seat_ids = list(seat_id(case) for case in seats)
all_seats = set(range(min(seat_ids), max(seat_ids)))

print(all_seats.difference(seat_ids))
