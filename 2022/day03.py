from string import ascii_lowercase, ascii_uppercase
from typing import List

LOWERCASE = {v: k for k, v in (enumerate(ascii_lowercase, 1))}
UPPERCASE = {v: k for k, v in (enumerate(ascii_uppercase, 27))}
PRIORITIES = dict(LOWERCASE, **UPPERCASE)


def find_common_item(content: str) -> str:
    half = len(content) // 2
    left = content[:half]
    right = content[half:]
    return (set(left) & set(right)).pop()


def find_badge(contents: List[str]) -> str:
    return set.intersection(*map(set, contents)).pop()  # type: ignore


def to_priority(item: str) -> int:
    return PRIORITIES[item]


def groups(contents: List[str]):
    return [contents[i : i + 3] for i in range(0, len(contents), 3)]


def main(part: int = 1) -> int:
    with open("2022/data/day03.txt") as f:
        contents = f.read().splitlines()
    if part == 1:
        return sum(to_priority(find_common_item(content)) for content in contents)
    else:
        return sum(to_priority(find_badge(group)) for group in groups(contents))


if __name__ == "__main__":
    contents = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

    assert find_common_item("vJrwpWtwJgWrhcsFMMfFFhFp") == "p"
    assert find_common_item("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL") == "L"
    assert find_common_item("PmmdzqPrVvPwwTWBwg") == "P"
    assert find_common_item("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn") == "v"
    assert find_common_item("ttgJtRGJQctTZtZT") == "t"
    assert find_common_item("CrZsJsPPZsGzwwsLwLmpwMDw") == "s"

    assert to_priority("a") == 1
    assert to_priority("z") == 26
    assert to_priority("A") == 27
    assert to_priority("Z") == 52

    assert to_priority(find_common_item("vJrwpWtwJgWrhcsFMMfFFhFp")) == 16
    assert to_priority(find_common_item("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL")) == 38
    assert to_priority(find_common_item("PmmdzqPrVvPwwTWBwg")) == 42
    assert to_priority(find_common_item("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn")) == 22
    assert to_priority(find_common_item("ttgJtRGJQctTZtZT")) == 20
    assert to_priority(find_common_item("CrZsJsPPZsGzwwsLwLmpwMDw")) == 19

    assert groups(contents.splitlines()) == [
        [
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
        ],
        [
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "ttgJtRGJQctTZtZT",
            "CrZsJsPPZsGzwwsLwLmpwMDw",
        ],
    ]

    assert (
        find_badge(
            [
                "vJrwpWtwJgWrhcsFMMfFFhFp",
                "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
                "PmmdzqPrVvPwwTWBwg",
            ]
        )
        == "r"
    )
    assert (
        find_badge(
            [
                "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
                "ttgJtRGJQctTZtZT",
                "CrZsJsPPZsGzwwsLwLmpwMDw",
            ]
        )
        == "Z"
    )

    print(main())
    print(main(part=2))
