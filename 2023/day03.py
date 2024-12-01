import re
from collections import namedtuple
from itertools import combinations

Point = namedtuple("Point", ["x", "y"])
BoundingBox = namedtuple("BoundingBox", ["bottom_left", "top_right"])


def intersects(bbox_a, bbox_b):
    # Adapted from https://stackoverflow.com/a/40795835
    return not (
        bbox_a.top_right.x < bbox_b.bottom_left.x
        or bbox_a.bottom_left.x > bbox_b.top_right.x
        or bbox_a.top_right.y > bbox_b.bottom_left.y
        or bbox_a.bottom_left.y < bbox_b.top_right.y
    )


def overlapping_content(bbox_a, bbox_b, rows):
    # Calculate the max bounding box
    # x_start = min(bbox_a.bottom_left.x, bbox_b.bottom_left.x)
    # x_end = max(bbox_a.top_right.x, bbox_b.top_right.x)
    # y_start = min(bbox_a.top_right.y, bbox_b.top_right.y)
    # y_end = max(bbox_a.bottom_left.y, bbox_b.bottom_left.y)
    #
    # overlapping_text = []
    # for y in range(y_start, y_end + 1):
    #     row_content = rows[y]
    #     overlapping_text.append(row_content[x_start : x_end + 1])
    # print("\n".join(overlapping_text))

    # Calculate the overlapping region
    x_start = max(bbox_a.bottom_left.x, bbox_b.bottom_left.x)
    x_end = min(bbox_a.top_right.x, bbox_b.top_right.x)
    y_start = max(bbox_a.top_right.y, bbox_b.top_right.y)
    y_end = min(bbox_a.bottom_left.y, bbox_b.bottom_left.y)

    overlapping_text = []
    for y in range(y_start, y_end + 1):
        row_content = rows[y]
        overlapping_text.append(row_content[x_start : x_end + 1])
    return "\n".join(overlapping_text)


def part_number_count(schematic, part=1):
    part_numbers = 0
    rows = schematic.splitlines()
    width = len(rows[0])
    new_rows = ["." * (width + 2)] + [f".{row}." for row in rows] + ["." * (width + 2)]

    bounding_boxes = {}
    for row_nr, line in enumerate(new_rows):
        matches = re.finditer(r"\d+", line)
        for match in matches:
            number = int(match.group())
            start = match.start()
            end = match.end()  # End position (exclusive)

            position_before = start - 1
            position_after = end
            row_nr_above = row_nr - 1
            row_nr_below = row_nr + 1

            symbols = []
            symbols.append(new_rows[row_nr][position_before])
            symbols.append(new_rows[row_nr][position_after])
            symbols.extend(new_rows[row_nr_above][position_before : position_after + 1])
            symbols.extend(new_rows[row_nr_below][position_before : position_after + 1])

            if len(set(symbols)) > 1:
                part_numbers += number

            if part == 2:
                if "*" in symbols:
                    bottom_left = Point(position_before, row_nr_below)
                    top_right = Point(position_after, row_nr_above)
                    bounding_boxes[number] = BoundingBox(bottom_left, top_right)

    if part == 1:
        return part_numbers
    else:
        gear_ratio = 0
        for part_number_a, part_number_b in combinations(
            sorted(bounding_boxes.keys()), 2
        ):
            bbox_a = bounding_boxes[part_number_a]
            bbox_b = bounding_boxes[part_number_b]
            if intersects(bbox_a, bbox_b) and "*" in overlapping_content(
                bbox_a, bbox_b, new_rows
            ):
                gear_ratio += part_number_a * part_number_b
        return gear_ratio


def main(part: int = 1) -> int:
    with open("2023/data/day03.txt") as f:
        schematic = f.read()
    return part_number_count(schematic, part)


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

    assert part_number_count(schematic, part=2) == 467835

    print(main(part=2))
