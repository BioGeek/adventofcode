from collections import defaultdict
from typing import List, Tuple


def get_overlap(vents: str, part: int = 1) -> int:
    positions = defaultdict(int)
    for line in vents.splitlines():
        for point in get_points(line, part):
            positions[point] += 1
    return sum(1 for value in positions.values() if value >= 2)


def get_points(line: str, part: int = 1) -> List[Tuple[int]]:
    start, end = line.split(" -> ")
    x1, y1 = map(int, start.split(","))
    x2, y2 = map(int, end.split(","))
    if x1 == x2:
        ys = sorted([y1, y2])
        ys = range(ys[0], ys[1] + 1)
        xs = [x1] * len(ys)
    elif y1 == y2:
        xs = sorted([x1, x2])
        xs = range(xs[0], xs[1] + 1)
        ys = [y2] * len(xs)
    elif part == 2 and (x2 - x1) == (y2 - y1):
        xs = sorted([x1, x2])
        ys = sorted([y1, y2])
        xs = range(xs[0], xs[1] + 1)
        ys = range(ys[0], ys[1] + 1)
    elif part == 2 and abs(x2 - x1) == abs(y2 - y1):
        if x1 > x2:
            xs = range(x1, x2 - 1, -1)
            ys = range(y1, y2 + 1)
        else:
            xs = range(x1, x2 + 1)
            ys = range(y1, y2 - 1, -1)
    else:
        return []
    return list(zip(xs, ys))


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

    assert get_points("1,1 -> 3,3", part=2) == [(1, 1), (2, 2), (3, 3)]
    assert get_points("9,7 -> 7,9", part=2) == [(9, 7), (8, 8), (7, 9)]
    assert get_points("7,9 -> 9,7", part=2) == [(7, 9), (8, 8), (9, 7)]

    print(main(part=2))
