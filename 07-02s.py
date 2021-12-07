with open("07-01.txt") as f:
    data = list(map(int, f.read().strip().split(",")))

print(
    min(
        sum(sum(range(1, abs(t - i) + 1)) for i in data)
        for t in range(min(data), max(data))
    )
)
