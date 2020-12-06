from typing import List


class Group:
    def __init__(self, data: str, part: int = 1) -> None:
        self.part = part
        self.answers_per_person = [set(line) for line in data.splitlines()]

    def question_count(self) -> int:
        if self.part == 1:
            return len(set.union(*self.answers_per_person))
        else:
            return len(set.intersection(*self.answers_per_person))


def make_groups(data: str, part: int = 1) -> List[Group]:
    return [Group(lines, part) for lines in data.split("\n\n")]


def main(part: int = 1) -> int:
    with open("2020/data/day06.txt") as fh:
        data = fh.read()

    return sum(group.question_count() for group in make_groups(data, part))


if __name__ == "__main__":
    SMALL = """abcx
abcy
abcz"""

    EXAMPLE = """abc

a
b
c

ab
ac

a
a
a
a

b"""

    assert Group(SMALL).question_count() == 6

    for group, expected in zip(make_groups(EXAMPLE), (3, 3, 3, 1, 1)):
        assert group.question_count() == expected

    print(main())

    assert Group(SMALL, part=2).question_count() == 3

    for group, expected in zip(make_groups(EXAMPLE, part=2), (3, 0, 1, 1, 1)):
        assert group.question_count() == expected

    print(main(part=2))
