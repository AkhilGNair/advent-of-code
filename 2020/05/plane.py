from pathlib import Path

seats = Path("input.txt").read_text().strip().split("\n")


def search(data, hit):
    def _search(data):
        for idx, dir in enumerate(reversed(data)):
            if dir == hit:
                yield pow(2, idx)

    return sum(list(_search(data)))


def seat_id(case):
    y, x = search(case[:7], "B"), search(case[7:], "R")
    return (y * 8) + x


print(max(seat_id(case) for case in seats))

seat_ids = list(seat_id(case) for case in seats)
all_seats = set(range(min(seat_ids), max(seat_ids)))

print(all_seats.difference(seat_ids))
