from typing import List

BOARD_SIZE = 5
boards = []
with open("04-01.txt") as fin:
    bingo_numbers = fin.readline().rstrip("\n").split(",")
    for line in fin:
        board = [next(fin).split() for row in range(BOARD_SIZE)]
        boards.append(board)


def is_bingo_row(row: List) -> bool:
    return all([isinstance(value, int) for value in row])


def is_bingo_col(board: List[List], column: int) -> bool:
    return all([isinstance(row[column], int) for row in board])


def is_bingo(board: List[List]) -> bool:
    # check rows
    for row in board:
        if is_bingo_row(row):
            return True
    for column in range(BOARD_SIZE):
        if is_bingo_col(board, column):
            return True
    return False


def set_number(board: List[List], number: str):
    for row in board:
        try:
            row[row.index(number)] = int(number)
        except ValueError:
            pass


def sum_unmarked_numbers(board: List[List]):
    return sum(
        [int(number) for row in board for number in row if not isinstance(number, int)]
    )


# play bingo
for index, number in enumerate(bingo_numbers):
    # set number
    boards_to_remove = []
    for board_index, board in enumerate(boards):
        set_number(board, number)
        if index >= 4 and is_bingo(board):
            boards_to_remove.append(board_index)
    print(boards_to_remove)
    if len(boards_to_remove) == 1 and len(boards) == 1:
        summation = sum_unmarked_numbers(boards[0])
        print(summation * int(number))
        break
    for board_remove in reversed(boards_to_remove):
        boards.pop(board_remove)
