from itertools import pairwise, tee
from typing import Iterable, TypeVar

_T_co = TypeVar("_T_co", covariant=True)


def tripletwise(iterable: Iterable[_T_co]):
    """tripletwise('ABCDEFG') --> ABC BCD CDE DEF EFG"""
    a, b, c = tee(iterable, 3)
    next(b, None)
    next(c, None)
    next(c, None)
    return zip(a, b, c)


def sonar_sweep(sea_floor_depths: Iterable[int], part: int = 1) -> int:
    if part == 1:
        return sum(b > a for a, b in pairwise(sea_floor_depths))
    return sonar_sweep((a + b + c for a, b, c in tripletwise(sea_floor_depths)), part=1)


def sea_floor_depths(report: str) -> Iterable[int]:
    return map(int, report.splitlines())


def main(part: int = 1) -> int:
    with open("2021/data/day01.txt") as f:
        report = f.read()
    return sonar_sweep(sea_floor_depths(report), part)


if __name__ == "__main__":
    report = """199
200
208
210
200
207
240
269
260
263"""
    assert sonar_sweep(sea_floor_depths(report), part=1) == 7
    assert sonar_sweep(sea_floor_depths(report), part=2) == 5
    assert list(tripletwise("ABCDEFG")) == [
        ("A", "B", "C"),
        ("B", "C", "D"),
        ("C", "D", "E"),
        ("D", "E", "F"),
        ("E", "F", "G"),
    ]
    assert list(tripletwise(sea_floor_depths(report))) == [
        (199, 200, 208),
        (200, 208, 210),
        (208, 210, 200),
        (210, 200, 207),
        (200, 207, 240),
        (207, 240, 269),
        (240, 269, 260),
        (269, 260, 263),
    ]

    print(main())
    print(main(part=2))
