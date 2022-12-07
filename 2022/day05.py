import re
from collections import defaultdict
from typing import Dict, List, Tuple


def parse_drawing(drawing: str) -> Tuple[str, str]:
    stacks, moves = drawing.split("\n\n")
    return stacks, moves


def parse_stacks(stacks: str) -> Dict[int, List[str]]:
    state = defaultdict(list)
    lines = stacks.splitlines()
    for row in reversed(lines[:-1]):
        crates = [row[i] for i in range(1, len(row), 4)]
        for stack_nr, crate_name in dict(enumerate(crates, 1)).items():
            if crate_name != " ":
                state[stack_nr].append(crate_name)
    return state


def parse_moves(moves: str):
    for line in moves.splitlines():
        m = re.findall(r"move (\d+) from (\d+) to (\d+)", line)
        yield list(map(int, m[0]))


def rearrange_old(quantity: int, from_: int, to: int, state: Dict[int, List[str]]):
    for _ in range(quantity):
        crate = state[from_].pop()
        state[to].append(crate)
    return state


def rearrange_new(quantity: int, from_: int, to: int, state: Dict[int, List[str]]):
    remaining = state[from_][:-quantity]
    to_be_moved = state[from_][-quantity:]
    state[from_] = remaining
    state[to].extend(to_be_moved)
    return state


def top_layer(state: Dict[int, List[str]]) -> str:
    return "".join(state[i][-1] for i in range(1, len(state) + 1))


def main(part: int = 1) -> str:
    with open("2022/data/day05.txt") as f:
        drawing = f.read()
    stacks, moves = parse_drawing(drawing)
    state = parse_stacks(stacks)
    for quantity, from_, to in parse_moves(moves):
        if part == 1:
            state = rearrange_old(quantity, from_, to, state)
        else:
            state = rearrange_new(quantity, from_, to, state)
    return top_layer(state)


if __name__ == "__main__":
    drawing = """    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

    stacks, moves = parse_drawing(drawing)
    assert parse_stacks(stacks) == {1: ["Z", "N"], 2: ["M", "C", "D"], 3: ["P"]}

    assert list(parse_moves(moves)) == [[1, 2, 1], [3, 1, 3], [2, 2, 1], [1, 1, 2]]

    state = rearrange_old(1, 2, 1, parse_stacks(stacks))
    assert state == {1: ["Z", "N", "D"], 2: ["M", "C"], 3: ["P"]}
    state = rearrange_old(3, 1, 3, state)
    assert state == {1: [], 2: ["M", "C"], 3: ["P", "D", "N", "Z"]}
    state = rearrange_old(2, 2, 1, state)
    assert state == {1: ["C", "M"], 2: [], 3: ["P", "D", "N", "Z"]}
    state = rearrange_old(1, 1, 2, state)
    assert state == {1: ["C"], 2: ["M"], 3: ["P", "D", "N", "Z"]}

    assert top_layer(state) == "CMZ"

    stacks, moves = parse_drawing(drawing)
    state = rearrange_new(1, 2, 1, parse_stacks(stacks))
    assert state == {1: ["Z", "N", "D"], 2: ["M", "C"], 3: ["P"]}
    state = rearrange_new(3, 1, 3, state)
    assert state == {1: [], 2: ["M", "C"], 3: ["P", "Z", "N", "D"]}
    state = rearrange_new(2, 2, 1, state)
    assert state == {1: ["M", "C"], 2: [], 3: ["P", "Z", "N", "D"]}
    state = rearrange_new(1, 1, 2, state)
    assert state == {1: ["M"], 2: ["C"], 3: ["P", "Z", "N", "D"]}

    assert top_layer(state) == "MCD"

    print(main())
    print(main(part=2))
