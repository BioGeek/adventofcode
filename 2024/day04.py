import numpy as np


def xmas_count(lol):
    return sum("".join(lst).count("XMAS") for lst in lol) + sum(
        "".join(lst)[::-1].count("XMAS") for lst in lol
    )


def search_xmas(grid):
    # Adapted from https://stackoverflow.com/a/43311126/50065
    lines = grid.splitlines()
    max_col = len(lines[0])
    max_row = len(lines)
    cols = [[] for _ in range(max_col)]
    rows = [[] for _ in range(max_row)]
    fdiag = [[] for _ in range(max_row + max_col - 1)]
    bdiag = [[] for _ in range(len(fdiag))]
    min_bdiag = -max_row + 1

    for x in range(max_col):
        for y in range(max_row):
            cols[x].append(lines[y][x])
            rows[y].append(lines[y][x])
            fdiag[x + y].append(lines[y][x])
            bdiag[x - y - min_bdiag].append(lines[y][x])

    return xmas_count(cols) + xmas_count(rows) + xmas_count(fdiag) + xmas_count(bdiag)


def rolling_window(a, shape):
    # Rolling window for 2D arrays in NumPy
    # https://stackoverflow.com/a/46237736
    s = (a.shape[0] - shape[0] + 1,) + (a.shape[1] - shape[1] + 1,) + shape
    strides = a.strides + a.strides
    return np.lib.stride_tricks.as_strided(a, shape=s, strides=strides)


def search_x_mas(grid):
    lines = grid.splitlines()
    array = np.array([[letter for letter in line] for line in lines])
    x_mas_shape = (3, 3)
    mas_count = 0
    for subgrid in rolling_window(array, x_mas_shape).tolist():
        for square in subgrid:
            fdiag = square[0][0] + square[1][1] + square[2][2]
            bdiag = square[0][2] + square[1][1] + square[2][0]
            fmas = "MAS" in (fdiag, fdiag[::-1])
            bmas = "MAS" in (bdiag, bdiag[::-1])
            if fmas and bmas:
                mas_count += 1
            # print('\n'.join(''.join(s) for s in square), fdiag, bdiag, fmas, bmas)
    return mas_count


def main(part: int = 1) -> int:
    with open("2024/data/day04.txt") as f:
        grid = f.read()
    if part == 1:
        return search_xmas(grid)
    return search_x_mas(grid)


if __name__ == "__main__":
    small = """..X...
.SAMX.
.A..A.
XMAS.S
.X...."""

    medium = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

    assert search_xmas(small) == 4
    assert search_xmas(medium) == 18

    print(main())

    assert search_x_mas(medium) == 9

    print(main(part=2))
