with open("01-01.txt") as f:
    data = [int(x.strip()) for x in f.readlines()]

increased_count = 0
for index, number in enumerate(data):
    try:
        next_number = data[index + 1]
    except IndexError:
        print("Reached end of list")
    if next_number > number:
        increased_count += 1

print(increased_count)
