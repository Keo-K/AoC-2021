with open("08-01.txt") as f:
    data = [
        {
            "Input": x.strip().split("|")[0].split(),
            "Output": x.strip().split("|")[1].split(),
        }
        for x in f.readlines()
    ]

total = 0
for line in data:
    input_values = ["".join(x) for x in line["Input"]]
    output_values = ["".join(x) for x in line["Output"]]
    number_map_unique = {
        1: [i for i in input_values if len(i) == 2][0],
        4: [i for i in input_values if len(i) == 4][0],
        7: [i for i in input_values if len(i) == 3][0],
        8: [i for i in input_values if len(i) == 7][0],
    }
    # print(input_values)
    number_map_non_unique = {
        2: [
            i for i in input_values if len(i) == 5 and number_map_unique[1][1] not in i
        ][0],
        3: [
            i
            for i in input_values
            if len(i) == 5
            and number_map_unique[1][0] in i
            and number_map_unique[1][1] in i
        ][0],
        5: [
            i for i in input_values if len(i) == 5 and number_map_unique[1][0] not in i
        ][0],
        6: [
            i
            for i in input_values
            if len(i) == 6
            and (number_map_unique[1][1] not in i or number_map_unique[1][0] not in i)
        ][0],
        9: [
            i
            for i in input_values
            if len(i) == 6 and all([n in i for n in number_map_unique[4]])
        ][0],
        0: [
            i
            for i in input_values
            if len(i) == 6
            and not all([n in i for n in number_map_unique[4]])
            and all([n in i for n in number_map_unique[1]])
        ][0],
    }
    combined_map = number_map_unique | number_map_non_unique
    sorting_map = sorted([x for x in combined_map.keys()])
    combined_map = {x: "".join(sorted(combined_map[x])) for x in sorting_map}
    output_values = ["".join(sorted(x)) for x in output_values]
    n = ""
    for x in output_values:
        for index, value in combined_map.items():
            if value == x:
                n += str(index)
    print(n)
    total += int(n)

print(f"Total: {total}")
