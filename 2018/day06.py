from collections import defaultdict
from itertools import chain, product
from string import ascii_uppercase


def X(point):
    return point[0]


def Y(point):
    return point[1]


def letters():
    for chars in chain(*(product(ascii_uppercase, repeat=i + 1) for i in range(2))):
        yield "".join(chars)


def neighbors4(point):
    "The eight neighboring squares."
    x, y = point
    print("in neighbors 4")
    return (
        (x, y - 1),
        (x - 1, y),
        (x + 1, y),
        (x, y + 1),
    )


"""
def floodfill(coord, letter, grid, max_x, max_y):
    print('in floodfill')
    lowercase = letter.lower()
    print('coord', coord)
    current = grid[coord]
    print('current', current)
    if current.isalpha():
        if not current.isupper():
            grid[coord] = '.'
    else:
        if current != '.':
            grid[coord] = lowercase
    print('grid', grid)
    neighbors = neighbors4(coord)
    neighbors = [coord for coord in neighbors if 0 <= X(coord) <= max_x
                                             and 0 <= Y(coord) <= max_y]
    print('neighbors', neighbors)

    for neighbor in neighbors:
        grid = floodfill(neighbor, letter, grid, max_x, max_y)

    return grid
"""


def floodfill(grid, coord, letter):
    print("in floodfill")

    def floodfill(coord):
        print("in fill")
        print("coord", coord)
        current = grid[coord]
        print("current", current)
        if (
            0 <= X(coord) <= max_x
            and 0 <= Y(coord) <= max_y
            and (current == " " or current.isalpha())
        ):
            if current == " ":
                grid[coord] = letter.lower()
            elif current.islower() and current != letter.lower():
                grid[coord] = "."
            else:
                print("## ", current)
            print("grid[coord]", grid[coord])
            draw_grid(grid)
            for neighbor in neighbors4(coord):
                print("neighbor", neighbor)
                floodfill(neighbor)

    max_x = max(X(c) for c in grid.keys())
    max_y = max(Y(c) for c in grid.keys())
    print("max_x", max_x)
    print("max_y", max_y)
    floodfill(coord)
    return grid


def draw_grid(grid):
    print("drawgrid")
    max_x = max(X(c) for c in grid.keys())
    max_y = max(Y(c) for c in grid.keys())
    print(
        "\n".join(
            [
                "".join([grid[(i, j)].ljust(2) for j in range(max_y + 1)])
                for i in range(max_x + 1)
            ]
        )
    )


def main(part=1, data=None):
    if data is None:
        with open("2018/data/06.txt") as f:
            data = f.read()
    data = data.splitlines()
    coords = [tuple(map(int, line.split(", "))) for line in data]
    grid = defaultdict(lambda: " ")

    for letter, coord in zip(letters(), coords):
        grid[coord] = letter

    print(grid)
    for coord in coords:
        letter = grid[coord]
        grid = floodfill(grid, coord, letter)
        print("grid", grid)

    draw_grid(grid)

    return grid


if __name__ == "__main__":
    data = """1, 1
1, 6
8, 3
3, 4
5, 5
8, 9"""
    print(main(data=data))
