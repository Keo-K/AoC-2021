with open("02-01.txt") as f:
    data = [x.strip().split() for x in f.readlines()]

data = [(i[0], int(i[1])) for i in data]
depth = 0
horizontal_position = 0
for value_1, value_2 in data:
    if value_1 == "up":
        depth -= value_2
    elif value_1 == "down":
        depth += value_2
    else:
        horizontal_position += value_2

print(depth)
print(horizontal_position)
print(depth * horizontal_position)
