from typing import List


def move(positions: List[int], idx: int, part: int = 1) -> int:
    if part == 2:
        return sum(sum(range(abs(position - idx) + 1)) for position in positions)
    return sum(abs(position - idx) for position in positions)


def parse(positions: str) -> List[int]:
    return list(map(int, positions.split(",")))


def cheapest_move(positions: List[int], part: int = 1) -> int:
    return min(move(positions, idx, part) for idx in range(len(positions)))


def main(part: int = 1) -> int:
    with open("2021/data/day07.txt") as f:
        positions = f.read()
    return cheapest_move(parse(positions), part)


if __name__ == "__main__":
    positions = "16,1,2,0,4,2,7,1,2,14"

    assert move(parse(positions), idx=1) == 41
    assert move(parse(positions), idx=2) == 37
    assert move(parse(positions), idx=3) == 39
    assert cheapest_move(parse(positions)) == 37

    print(main())

    assert move(parse(positions), idx=2, part=2) == 206
    assert move(parse(positions), idx=5, part=2) == 168
    assert cheapest_move(parse(positions), part=2) == 168

    print(main(part=2))
