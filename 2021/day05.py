from collections import defaultdict
from typing import Dict, List, Tuple


def get_overlap(vents: str, part: int = 1) -> int:
    positions: Dict[Tuple[int, int], int] = defaultdict(int)
    for line in vents.splitlines():
        for point in get_points(line, part):
            positions[point] += 1
    return sum(1 for value in positions.values() if value >= 2)


def get_points(line: str, part: int = 1) -> List[Tuple[int, int]]:
    start, end = line.split(" -> ")
    x1, y1 = map(int, start.split(","))
    x2, y2 = map(int, end.split(","))
    if x1 == x2:
        # vertical
        y1, y2 = min(y1, y2), max(y1, y2)
        return [(x1, y) for y in range(y1, y2 + 1)]
    elif y1 == y2:
        # horizontal
        x1, x2 = min(x1, x2), max(x1, x2)
        return [(x, y1) for x in range(x1, x2 + 1)]
    elif part == 2 and x1 != x2 and y1 != y2:
        # diagonal
        dx = int((x2 - x1) / abs(x2 - x1))
        dy = int((y2 - y1) / abs(y2 - y1))
        return [(x, y) for x, y in zip(range(x1, x2 + dx, dx), range(y1, y2 + dy, dy))]
    else:
        return []


def main(part: int = 1) -> int:
    with open("2021/data/day05.txt") as f:
        vents = f.read()
    return get_overlap(vents, part)


if __name__ == "__main__":
    vents = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

    assert get_points("1,1 -> 1,3") == [(1, 1), (1, 2), (1, 3)]
    assert get_points("9,7 -> 7,7") == [(7, 7), (8, 7), (9, 7)]
    assert get_overlap(vents) == 5

    print(main())

    assert get_points("1,1 -> 3,3", part=2) == [(1, 1), (2, 2), (3, 3)], get_points(
        "1,1 -> 3,3", part=2
    )
    assert get_points("9,7 -> 7,9", part=2) == [(9, 7), (8, 8), (7, 9)]
    assert get_points("7,9 -> 9,7", part=2) == [(7, 9), (8, 8), (9, 7)]

    print(main(part=2))
