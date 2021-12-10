from typing import Dict, Tuple

Location = Tuple[int]


def neighbors(location: Location) -> Tuple[Location]:
    """The four neighbors (without diagonals)."""
    x, y = location
    return ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))


def low_points(heightmap: str):
    grid = parse(heightmap)
    return sum(
        digit + 1
        for location, digit in grid.items()
        if all(digit < grid.get(location, 9) for location in neighbors(location))
    )


def parse(heightmap: str) -> Dict[Location, int]:
    return {
        (row_nr, column_nr): int(digit)
        for row_nr, row in enumerate(heightmap.splitlines())
        for column_nr, digit in enumerate(row)
    }


def main(part: int = 1) -> int:
    with open("2021/data/day09.txt") as f:
        heightmap = f.read()
    return low_points(heightmap)


if __name__ == "__main__":
    heightmap = """2199943210
3987894921
9856789892
8767896789
9899965678"""

    assert low_points(heightmap) == 15

    print(main())
