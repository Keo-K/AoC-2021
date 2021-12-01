with open("01-01.txt") as f:
    data = [int(x.strip()) for x in f.readlines()]

increased_count = 0
for index, number in enumerate(data):
    try:
        _ = data[index + 2]
    except IndexError:
        break
    sum_number_old = sum(data[index : index + 3])
    sum_number_new = (
        sum(data[index + 1 : index + 4])
        if len(data[index + 1 : index + 4]) > 2
        else None
    )
    if sum_number_new and sum_number_new > sum_number_old:
        increased_count += 1

print(increased_count)
