from typing import List, Tuple

Board = List[List[str]]


def score(number: str, board: Board) -> int:
    board_sum = sum(int(item) for row in board for item in row if item != "X")
    return board_sum * int(number)


def has_won(board: Board) -> bool:
    complete = ["X"] * 5
    return any(row == complete for row in board) or any(
        list(column) == complete for column in zip(*board)
    )


def play(numbers: List[str], boards: List[Board], part: int = 1) -> int:
    nr_boards = len(boards)
    winning_boards = set()
    for number in numbers:
        for board_nr, board in enumerate(boards):
            for row in board:
                try:
                    idx = row.index(number)
                    row[idx] = "X"
                except ValueError:
                    pass
            if has_won(board):
                if part == 1:
                    return score(number, board)
                else:
                    winning_boards.add(board_nr)
                    if len(winning_boards) == nr_boards:
                        return score(number, board)
    raise AssertionError()


def parse(bingo: str) -> Tuple[List[str], List[Board]]:
    first_line, *rest = bingo.split("\n\n")
    numbers = first_line.split(",")
    boards = [[line.strip().split() for line in board.split("\n")] for board in rest]
    return numbers, boards


def main(part: int = 1) -> int:
    with open("2021/data/day04.txt") as f:
        bingo = f.read()
    return play(*parse(bingo), part)


if __name__ == "__main__":
    bingo = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

    assert play(*parse(bingo)) == 4512
    assert play(*parse(bingo), part=2)

    print(main())
    print(main(part=2))
