with open("07-01.txt") as f:
    data = list(map(int, f.read().strip().split(",")))

cost_map = {}
for x in range(min(data), max(data)):
    temp_list = []
    for i in data:
        absolute_difference = abs(i - x)
        temp_list.append(absolute_difference)
    cost_map[x] = sum(temp_list)

minmum_value = min([x for x in cost_map.values()])
print(f"Lowest cost: {minmum_value}")
