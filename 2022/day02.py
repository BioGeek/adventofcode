from typing import List

shapes = {
    "A": 1,  # Rock, opponent
    "B": 2,  # Paper, opponent
    "C": 3,  # Scissors, opponent
    "X": 1,  # Rock, you
    "Y": 2,  # Paper, you
    "Z": 3,  # Scissors, you
}

equals = {"A": "X", "B": "Y", "C": "Z"}  # Rock  # Paper  # Scissors

is_beaten_by = {
    "A": "Y",  # Rock of opponent is beaten by your Paper
    "B": "Z",  # Paper of opponent is beaten by your Scissors
    "C": "X",  # Scissors of opponent is beaten by your Rock
}

wins_against = {
    "A": "Z",  # Rock of opponent wins against your Scissors
    "B": "X",  # Paper of opponent wins against your Rock
    "C": "Y",  # Scissors of opponent wins against your Paper
}


def parse(strategy_guide: str) -> List[List[str]]:
    lines = strategy_guide.splitlines()
    rounds = [line.split() for line in lines]
    return rounds


def total_score(rounds: List[List[str]], part: int = 1) -> int:
    if part == 1:
        return sum(score_single_round(opponent, you) for (opponent, you) in rounds)
    else:
        return sum(
            score_single_round(opponent, calculate_move(opponent, you))
            for (opponent, you) in rounds
        )


def score_single_round(opponent: str, you: str) -> int:
    return shapes[you] + outcome_of_round(opponent, you)


def outcome_of_round(opponent: str, you: str):
    """Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.
    If both players choose the same shape, the round instead ends in a draw.
    """
    if shapes[opponent] == shapes[you]:
        return 3  # draw
    elif (
        (you == "X" and opponent == "C")
        or (you == "Y" and opponent == "A")
        or (you == "Z" and opponent == "B")
    ):
        return 6  # you win
    else:
        return 0  # you lose


def calculate_move(opponent, you):
    """X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win."""
    if you == "Y":
        # needs to end in a draw
        return equals[opponent]
    elif you == "Z":
        # you need to win
        return is_beaten_by[opponent]
    else:
        # you need to lose
        return wins_against[opponent]


def main(part: int = 1) -> int:
    with open("2022/data/day02.txt") as f:
        strategy_guide = f.read()
    rounds = parse(strategy_guide)
    return total_score(rounds, part)


if __name__ == "__main__":
    strategy_guide = """A Y
B X
C Z"""

    assert parse(strategy_guide) == [["A", "Y"], ["B", "X"], ["C", "Z"]]

    assert outcome_of_round("A", "Y") == 6
    assert outcome_of_round("B", "X") == 0
    assert outcome_of_round("C", "Z") == 3

    assert score_single_round("A", "Y") == 8
    assert score_single_round("B", "X") == 1
    assert score_single_round("C", "Z") == 6

    assert total_score(parse(strategy_guide)) == 15

    assert calculate_move("A", "Y") == "X"
    assert calculate_move("B", "X") == "X"
    assert calculate_move("C", "Z") == "X"

    print(main())
    print(main(part=2))
