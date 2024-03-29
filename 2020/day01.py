# part1: find the two entries that sum to 2020 and then multiply those two numbers together.
# part2: find three numbers in your expense report that meet the same criteria.
from itertools import combinations
from math import prod
from typing import Iterator


def sum_to_2020(expenses: Iterator[int], part: int = 1) -> int:
    for combination in combinations(expenses, part + 1):
        if sum(combination) == 2020:
            return prod(combination)
    raise AssertionError()  # To make mypy happy


def expenses(report: str) -> Iterator[int]:
    return map(int, report.splitlines())


def main(part: int = 1) -> int:
    with open("2020/data/day01.txt") as f:
        report = f.read()
    return sum_to_2020(expenses(report), part)


if __name__ == "__main__":
    report = """1721
979
366
299
675
1456"""
    assert sum_to_2020(expenses(report)) == 514579
    assert sum_to_2020(expenses(report), part=2) == 241861950

    print(main())
    print(main(part=2))
