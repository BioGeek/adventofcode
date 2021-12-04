from typing import List, Tuple

Board = List[List[str]]


def score(drawing: str, board: Board) -> int:
    board_sum = sum(int(item) for row in board for item in row if item != "X")
    print(f"score: {drawing}, {board_sum}")
    return board_sum * int(drawing)


def win(board: Board) -> bool:
    complete = ["X"] * 5
    for row in board:
        if row == complete:
            return True
    for column in zip(*board):
        if list(column) == complete:
            return True
    return False


def play(drawings: List[str], boards: List[Board], part: int) -> int:
    print(f"{drawings = }")
    nr_boards = len(boards)
    print(f"{nr_boards = }")
    for drawing_nr, drawing in enumerate(drawings):
        print(f"{drawing = }")
        for board_nr, board in enumerate(boards):
            print(f"{board_nr = }")
            for row in board:
                try:
                    idx = row.index(drawing)
                    row[idx] = "X"
                except ValueError:
                    pass
                print("".join([f"{item:>3}" for item in row]))
            if win(board):
                print("WIN")
                print(f"{len(boards) = }")
                if part == 1:
                    return score(drawing, board)
                else:
                    del boards[board_nr]

                    if len(boards) == 1:

                        return score(drawing, board)
                    else:
                        drawings = drawings[drawing_nr + 1 :]
                        return play(drawings, boards, part)


def parse(bingo: str) -> Tuple[List[str], List[Board]]:
    drawings, *boards = bingo.split("\n\n")
    drawings = drawings.split(",")
    boards = [[line.split() for line in board.split("\n")] for board in boards]
    return drawings, boards


def main(part: int = 1) -> int:
    with open("2021/data/day04.txt") as f:
        bingo = f.read()
    return play(*parse(bingo))


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

    # assert play(*parse(bingo)) == 4512
    print(play(*parse(bingo), part=2))

    # print(main())
