import re


def part_number_count(schematic):
    part_numbers = 0
    rows = schematic.splitlines()
    width = len(rows[0])
    new_rows = ["." * (width + 2)] + [f".{row}." for row in rows] + ["." * (width + 2)]
    # print('\n'.join(new_rows))
    for row_nr, line in enumerate(new_rows):
        matches = re.finditer(r"\d+", line)
        for match in matches:
            number = int(match.group())
            start = match.start()
            end = match.end()  # End position (exclusive)
            # print(f"Number: {number}, Start: {start}, End: {end}, row nr {row_nr}")

            symbols = []
            position_before = start - 1
            symbols.append(new_rows[row_nr][position_before])
            position_after = end
            symbols.append(new_rows[row_nr][position_after])
            row_nr_above = row_nr - 1
            symbols.extend(new_rows[row_nr_above][position_before : position_after + 1])
            row_nr_below = row_nr + 1
            symbols.extend(new_rows[row_nr_below][position_before : position_after + 1])
            # print(set(symbols))
            if len(set(symbols)) > 1:
                part_numbers += number
    return part_numbers


def main(part: int = 1) -> int:
    with open("2023/data/day03.txt") as f:
        schematic = f.read()
    return part_number_count(schematic)


if __name__ == "__main__":
    schematic = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

    assert part_number_count(schematic) == 4361

    print(main())
