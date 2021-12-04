def solve():
    with open("04-01.txt") as f:
        d = f.read()
        inp, *board = d.split("\n")
        data = []
        t = []
        board.append("")
        for item in board[1:]:
            if item != "":
                t.append(item)
            else:
                data.append(t.copy())
                t.clear()

        classes = []
        for i in data:
            classes.append(matrix(i))
        for val in map(int, inp.split(",")):
            for i in classes:
                for j in i.inner:
                    for k in j:
                        if k.value == val:
                            k.marked = True
            for i in classes:
                if i.check():
                    return val * sum(
                        [j.value for j in sum(i.inner, start=[]) if not j.marked]
                    )


class num:
    def __init__(self, value, marked=False):
        self.value = value
        self.marked = marked


class matrix:
    def __init__(self, data):
        self.data = [list(map(int, i.split())) for i in data]
        self.inner = [[num(i) for i in j] for j in self.data]
        self.pos = ()

    def check(self):
        for i in self.inner:
            if all(j.marked for j in i):
                return True
        for i in zip(*self.inner):
            if all(j.marked for j in i):
                return True


print(solve())
