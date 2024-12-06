from collections import namedtuple

# Taken from Norvig
# https://github.com/norvig/pytudes/blob/main/ipynb/Advent-2017.ipynb

#           (x, y-1)
#  (x-1, y) (x, y  )  (x+1, y)
#           (x, y+1)

HEADINGS = UP, LEFT, DOWN, RIGHT = (0, -1), (-1, 0), (0, 1), (1, 0)


def turn_right(heading):
    return HEADINGS[HEADINGS.index(heading) - 1]


Grid = namedtuple("Grid", ["current", "heading", "obstacles", "visited"])


def parse(lines):
    current = next(
        (x, y)
        for y, row in enumerate(lines)
        for x, content in enumerate(row)
        if content == "^"
    )
    heading = UP
    obstacles = [
        (x, y)
        for y, row in enumerate(lines)
        for x, content in enumerate(row)
        if content == "#"
    ]
    visited = set()
    return Grid(current, heading, obstacles, visited)


def next_step(current, heading):
    return tuple(c + h for c, h in zip(current, heading))


def visualize(obstacles, nxt, heading):
    arrows = "^<v>"
    rows = []
    for y in range(11):
        row = []
        for x in range(11):
            if (x, y) == nxt:
                row.append(arrows[HEADINGS.index(heading)])
            else:
                row.append("#" if (x, y) in obstacles else ".")
        rows.append("".join(row))
    print("\n".join(rows))


def walk(grid):
    """Walk one step and simulate the new state of the grid"""
    current, heading, obstacles, visited = grid
    visited.add(current)
    # visualize(obstacles, current, heading)
    if next_step(current, heading) in obstacles:
        print("turning")
        heading = turn_right(heading)
    nxt = next_step(current, heading)
    # print(current, nxt, heading, visited)
    # print()
    return Grid(nxt, heading, obstacles, visited)


def visit(map):
    lines = [list(line) for line in map.strip().splitlines()]
    max_y = len(lines)
    max_x = len(lines[0])
    grid = parse(lines)
    while (0 <= grid.current[0] <= max_x) and (0 <= grid.current[1] <= max_y):
        grid = walk(grid)
    return len(grid.visited) - 1


def main(part: int = 1) -> int:
    with open("2024/data/day05.txt") as f:
        map = f.read()
    return visit(map)


if __name__ == "__main__":
    map = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

    assert visit(map) == 41

    print(main())
