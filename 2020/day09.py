from typing import Dict, Generator, List, Tuple
from itertools import combinations


def create_numbers(data: str) -> List[int]:
    return [int(line) for line in data.splitlines()]


def get_slice(
    numbers: List[int], n: int
) -> Generator[Tuple[List[int], int], None, None]:
    for i in range(len(numbers) - n):
        yield numbers[i : i + n], numbers[i + n]


def is_valid(number: int, memory: Dict[Tuple[int, int], int]) -> bool:
    return number in memory.values()


def make_key(a: int, b: int) -> Tuple[int, int]:
    # contrived way because of https://github.com/python/mypy/issues/2628
    assert a != b
    if a < b:
        return (a, b)
    return (b, a)


def xmas(numbers: List[int], n: int) -> int:
    memory = {}
    for preamble, number in get_slice(numbers, n):
        for a, b in combinations(preamble, 2):
            if a != b:
                memory[make_key(a, b)] = a + b
        if not is_valid(number, memory):
            return number
        else:
            first, *rest = preamble
            for key in list(memory):
                if first in key:
                    del memory[key]
            for r in rest:
                if make_key(r, number) not in memory:
                    memory[make_key(r, number)] = r + number
    return -1


def encryption_weakness(numbers: List[int], invalid_number: int) -> int:
    stack = numbers[:2]
    index = 2
    while sum(stack) != invalid_number:
        if sum(stack) < invalid_number:
            stack += [numbers[index]]
            index += 1
        else:
            stack = stack[1:]
    return min(stack) + max(stack)


def main(part: int = 1) -> int:
    with open("2020/data/day09.txt") as fh:
        data = fh.read()

    numbers = create_numbers(data)
    invalid_number = xmas(numbers, n=25)

    if part == 1:
        return invalid_number
    else:
        return encryption_weakness(numbers, invalid_number)


if __name__ == "__main__":
    EXAMPLE = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""

    assert xmas(create_numbers(EXAMPLE), 5) == 127

    print(main())

    assert encryption_weakness(create_numbers(EXAMPLE), 127) == 62

    print(main(part=2))
