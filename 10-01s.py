with open("10-01.txt") as f:
    data = [x.strip() for x in f.readlines()]


error_score = {
    ')':    3,
    ']':    57,
    '}':    1197,
    '>':    25137,
}

completion_score = {
    ')':    1,
    ']':    2,
    '}':    3,
    '>':    4,
}

matching = dict(zip('([{<>}])', ')]}><{[('))

def process(line):
    stack = []
    for i, char in enumerate(line): # match case is new in python 3.10 :3
        match char:
            case '(' | '[' | '{' | '<':
                stack.append(char)
            case _: # this is a fun use of it
                if not stack or stack.pop() != matching[char]:
                    return i
    return ''.join(matching[char] for char in reversed(stack))

total = 0
for line in data:
    i = process(line)
    if isinstance(i, int):
        total += error_score[line[i]]
print(total)