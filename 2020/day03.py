from math import prod
from typing import Dict


class Grid:
    def __init__(self, data: str, part: int = 1) -> None:
        self.grid = [list(line) for line in data.splitlines()]
        self.width = len(self.grid[0])
        self.height = len(self.grid)
        self.x = 0
        self.y = 0
        if part == 1:
            self.slopes = [{"right": 3, "down": 1}]
        else:
            self.slopes = [
                {"right": 1, "down": 1},
                {"right": 3, "down": 1},
                {"right": 5, "down": 1},
                {"right": 7, "down": 1},
                {"right": 1, "down": 2},
            ]
        self.trees = [0] * len(self.slopes)
        self.done = [False] * len(self.slopes)

    def step(self, i: int, slope: Dict[str, int]) -> None:
        self.x += slope["down"]
        self.y = (self.y + slope["right"]) % self.width
        if self.x >= self.height:
            self.done[i] = True
            self.x = 0
            self.y = 0
        elif self.grid[self.x][self.y] == "#":
            self.trees[i] += 1

    def count_trees(self) -> int:
        for i, slope in enumerate(self.slopes):
            while not self.done[i]:
                self.step(i, slope)
        return prod(self.trees)


def main(part: int = 1) -> int:
    with open("2020/data/day03.txt") as f:
        data = f.read()
    grid = Grid(data, part)
    return grid.count_trees()


if __name__ == "__main__":
    GRID = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""
    assert Grid(GRID).count_trees() == 7
    print(main())

    assert Grid(GRID, part=2).count_trees() == 336
    print(main(part=2))
