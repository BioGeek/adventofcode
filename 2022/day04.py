from itertools import chain
from typing import List


def assignments(section: str) -> List[int]:
    return list(
        chain(
            *[tuple(map(int, assigment.split("-"))) for assigment in section.split(",")]
        )
    )


def is_fully_contained(x1: int, y1: int, x2: int, y2: int) -> bool:
    return (x1 >= x2 and y1 <= y2) or (x2 >= x1 and y2 <= y1)


def do_overlap(x1: int, y1: int, x2: int, y2: int) -> bool:
    return len(set(range(x1, y1 + 1)).intersection(set(range(x2, y2 + 1)))) > 0


def main(part: int = 1) -> int:
    with open("2022/data/day04.txt") as f:
        sections = f.read().splitlines()
    if part == 1:
        return sum(is_fully_contained(*assignments(section)) for section in sections)
    return sum(do_overlap(*assignments(section)) for section in sections)


if __name__ == "__main__":
    sections = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

    assert assignments("2-4,6-8") == [2, 4, 6, 8]
    assert assignments("12-24,36-48") == [12, 24, 36, 48]

    assert not is_fully_contained(2, 4, 6, 8)
    assert not is_fully_contained(2, 3, 4, 5)
    assert not is_fully_contained(5, 7, 7, 9)
    assert is_fully_contained(2, 8, 3, 7)
    assert is_fully_contained(6, 6, 4, 6)
    assert not is_fully_contained(2, 6, 4, 8)

    assert (
        sum(
            is_fully_contained(*assignments(section))
            for section in sections.splitlines()
        )
        == 2
    )

    assert not do_overlap(2, 4, 6, 8)
    assert not do_overlap(2, 3, 4, 5)
    assert do_overlap(5, 7, 7, 9)
    assert do_overlap(2, 8, 3, 7)
    assert do_overlap(6, 6, 4, 6)
    assert do_overlap(2, 6, 4, 8)

    print(main())
    print(main(part=2))
