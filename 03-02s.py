with open("03-01.txt") as f:
    data = [x.strip() for x in f.readlines()]


# print(most_common)

data_copy = data.copy()

for i in range(12):
    columns = [[x[i] for x in data_copy] for i in range(12)]
    most_common = ["0" if x.count("0") > x.count("1") else "1" for x in columns]
    print(most_common)
    data_copy = [x for x in data_copy if x[i] == most_common[i]]
    print(data_copy)
print(int("001100111001", 2))  # 825


data_copy = data.copy()

for i in range(12):
    columns = [[x[i] for x in data_copy] for i in range(12)]
    most_common = ["1" if x.count("1") < x.count("0") else "0" for x in columns]
    print(most_common)
    data_copy = [x for x in data_copy if x[i] == most_common[i]]
    print(data_copy)
print(int("110100101111", 2))  # 3375

print(3375 * 825)
