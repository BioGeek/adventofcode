# inspired by https://stackoverflow.com/a/36961645/50065
# and https://github.com/norvig/pytudes/blob/master/ipynb/Advent%20of%20Code.ipynb

from collections import defaultdict
from itertools import count, cycle


def spiral_distances():
    """
    Yields 1, 1, 2, 2, 3, 3, ...
    """
    for distance in count(1):
        for _ in (0, 1):
            yield distance


def clockwise_directions():
    """
    Yields right, down, left, up, right, down, left, up, right, ...
    """
    left = (-1, 0)
    right = (1, 0)
    up = (0, 1)
    down = (0, -1)
    return cycle((right, up, left, down))


def spiral_movements():
    """
    Yields each individual movement to make a spiral:
    right, down, left, left, up, up, right, right, right, down, down, down, ...
    """
    for distance, direction in zip(spiral_distances(), clockwise_directions()):
        for _ in range(distance):
            yield direction


# 2-D points implemented using (x, y) tuples
def X(point):
    return point[0]


def Y(point):
    return point[1]


def add(p, q):
    return (X(p) + X(q), Y(p) + Y(q))


def cityblock_distance(p, q=(0, 0)):
    "City block distance between two points."
    return abs(X(p) - X(q)) + abs(Y(p) - Y(q))


def neighbors8(point):
    "The eight neighbors (with diagonals)."
    x, y = point
    return (
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
        (x + 1, y + 1),
        (x - 1, y - 1),
        (x + 1, y - 1),
        (x - 1, y + 1),
    )


def solve(n: int, part: int = 1) -> int:
    current_position = (0, 0)
    if part == 1:
        s = spiral_movements()
        for _ in range(2, n + 1):
            change = next(s)
            current_position = add(current_position, change)
        return cityblock_distance(current_position)
    else:
        current_value = 1
        values = defaultdict(int)
        values[current_position] = current_value
        s = spiral_movements()
        while current_value < n:
            change = next(s)
            current_position = add(current_position, change)
            neighbors = neighbors8(current_position)
            current_value = sum([values[n] for n in neighbors])
            values[current_position] = current_value
            # print(current_value, current_position, {(k, v) for (k, v) in values.items() if v})
        return current_value


def main(part: int = 1) -> int:
    n = 361527
    return solve(n, part)


if __name__ == "__main__":
    assert solve(12) == 3
    assert solve(23) == 2
    assert solve(1024) == 31

    print(main())

    assert solve(12, part=2) == 23
    assert solve(800, part=2) == 806

    print(main(part=2))
