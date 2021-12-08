from os import times


with open("08-01.txt") as f:
    data = [x[x.index("|") + 1 :].strip() for x in f.readlines()]

times_they_appear = 0
count_map = {1: 2, 4: 4, 7: 3, 8: 7}
for x in data:
    x = x.split()
    for y in x:
        if len(y) in count_map.values():
            times_they_appear += 1
print(times_they_appear)
