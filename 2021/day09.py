from functools import reduce
from operator import mul
from typing import Dict, Tuple

Location = Tuple[int]
Grid = Dict[Location, int]


def neighbors(location: Location) -> Tuple[Location]:
    """The locations of the four neighbors (without diagonals)."""
    x, y = location
    return ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))


def low_point_locations(grid: Grid):
    return {
        location: digit
        for (location, digit) in grid.items()
        if all(digit < grid.get(adjacent, 9) for adjacent in neighbors(location))
    }


def floodfill(
    grid: Grid, location: Location, fill_value: str = ".", show_grid: bool = False
) -> None:
    orig_value = grid[location]
    stack = set((location,))
    if orig_value == fill_value:
        raise ValueError("Area already filled")

    basin_size = 0
    while stack:
        location = stack.pop()
        if grid[location] not in (9, fill_value) and grid[location] >= orig_value:
            grid[location] = fill_value
            basin_size += 1
            for adjacent in neighbors(location):
                if adjacent in grid:
                    stack.add(adjacent)
    if show_grid:
        print(visualize(grid))
        print()
    return basin_size


def visualize(grid: Grid):
    x_size, y_size = map(max, zip(*grid.keys()))
    return "\n".join(
        "".join(str(grid[(x, y)]) for y in range(y_size + 1)) for x in range(x_size + 1)
    )


def parse(heightmap: str) -> Grid:
    return {
        (row_nr, column_nr): int(digit)
        for row_nr, row in enumerate(heightmap.splitlines())
        for column_nr, digit in enumerate(row)
    }


def solve(heightmap: str, part: int = 1) -> int:
    grid = parse(heightmap)
    low_points = low_point_locations(grid)
    if part == 1:
        return sum(digit + 1 for digit in low_points.values())
    basin_sizes = [floodfill(grid, low_point) for low_point in low_points]
    return reduce(mul, sorted(basin_sizes)[-3:])


def main(part: int = 1) -> int:
    with open("2021/data/day09.txt") as f:
        heightmap = f.read()
    return solve(heightmap, part)


if __name__ == "__main__":
    heightmap = """2199943210
3987894921
9856789892
8767896789
9899965678"""

    assert solve(heightmap) == 15
    assert visualize(parse(heightmap)) == heightmap

    print(main())

    assert solve(heightmap, part=2) == 1134

    # print(main(part=2))
