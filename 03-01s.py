with open("03-01.txt") as f:
    data = [x.strip() for x in f.readlines()]

n = []
for x in range(len(data[0])):
    r0 = [i[x] for i in data]
    g = sorted(r0, key=r0.count)[::-1][0]
    n.append(g)

n = "".join(n)
n = int(n, 2)
print(n)

m = []
for x in range(len(data[0])):
    r0 = [i[x] for i in data]
    g = sorted(r0, key=r0.count)[0]
    m.append(g)

m = "".join(m)
m = int(m, 2)
print(m * n)
