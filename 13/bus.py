from math import ceil
from pathlib import Path

arrival, departures = Path("input.txt").read_text().strip().split("\n")
arrival = int(arrival)


def to_int(s):
    try:
        return int(s)
    except ValueError:
        return None


departures = list(map(to_int, departures.split(",")))


def find_wait(arr, dep):
    return (ceil(arr / dep) * dep) - arr


waits = {dep: find_wait(arrival, dep) for dep in departures if dep}

min_wait = min(waits.values())
next_bus = [bus for bus, wait in waits.items() if wait == min_wait]

# print(min_wait * next_bus[0])

# 17, 0, a = 201
# 13, 2, b = 263
# 19, 3, c = 180

# 17a = x
# 13b = x + 2
# 19c = x + 3

# 17a + 0 = x
# 13b - 2 = x
# 19c - 3 = x


# 17a = 13b - 2
# => 17a + 2 = 13b
# => (1/13) * (17a + 2) = b

# 19c - 3 = 17a
# => 17a + 3 = 19c
# => (1/19) * (17a + 3) = c

# a = 0
# while True:
#     b = ((17 * a) + 2) * (1 / 13)
#     c = ((17 * a) + 3) * (1 / 19)
#     if b % 1 == 0 and c % 1 == 0:
#         print(a, b, c)
#         break
#     a += 1


# # departures = [1789, 37, 47, 1889]
# _dep = [d for d in departures if d]


# longest_wait = [(o, b) for o, b in enumerate(departures) if b == max(_dep)]
# longest_offset, longest_bus_id = longest_wait[0]

# buses = [(offset - longest_offset, bus) for offset, bus in enumerate(departures) if bus]

# i = 0
# buses = [(o, b) for o, b in buses if b != longest_bus_id]


# def all_whole(buses, i):
#     for offset, bus in buses:
#         time = ((longest_bus_id * i) + offset) * (1 / bus)
#         if time % 1 > 1e-4:
#             return False
#     return True


# while True:
#     soln = all_whole(buses, i)
#     if soln:
#         print("soln:", (longest_bus_id * i) - longest_offset)
#         break
#     i += 1
#     if i % 1000000 == 0:
#         print(i)

# Chinese remainder theorem?
# x \= 0 (mod 17)
# x \= 2 (mod 13)
# x \= 3 (mod 19)


from math import prod

departures = [67, 7, "x", 59, 61]
departures = [67, "x", 7, 59, 61]
departures = [67, 7, 59, 61]
departures = [17, "x", 13, 19]
departures = [1789, 37, 47, 1889]
_, data = Path("input.txt").read_text().strip().split("\n")

departures = [s for s in data.split(",")]

x = {int(bus): offset for offset, bus in enumerate(departures) if bus != "x"}
print(x)

M = prod(x.keys())


def b(mod):
    b = 1
    while True:
        crit = (b * ((M / mod))) % mod
        if crit == 1:
            return b
        b += 1


# Because otherwise floats produce rounding errors!
solution = 0
for mod, rem in x.items():
    solution += int(rem * b(mod)) * int(M / mod)

print("prod mod", M)
print("solution", solution % M)
print("bus time", M - (solution % M))

# 958290565868129 is wrong?? => My offsets were wrong...
# 939490236001475?
# 939490236001471? => FLOAT ERRORRRRRR
