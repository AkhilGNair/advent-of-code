import aoc

data = aoc.read(path="input.txt", cast_as=str)

data = [elem.split(" ") for elem in data]
data = [(k, int(v)) for k, v in data]

aim = 0
position = 0
depth = 0

for direction, amount in data:
    amount = int(amount)
    if direction == "forward":
        position += amount
        depth += (amount * aim)
    elif direction == "down":
        aim += amount
    elif direction == "up":
        aim -= amount
    
print(position * depth)


