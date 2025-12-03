import re


def parse(document):
    pattern = re.compile(r"(L|R)(\d+)")
    for line in document.splitlines():
        match = pattern.match(line)
        if match:
            direction = match.group(1)
            distance = int(match.group(2))
            yield (direction, distance)


def rotate(direction, distance, current_dial):
    if direction == "L":
        current_dial = (current_dial - distance) % 100
    else:
        current_dial = (current_dial + distance) % 100

    return current_dial


def click(direction, distance, current_dial, dials):
    for turn in range(1, distance + 1):
        if direction == "R":
            dials[(current_dial + turn) % 100] += 1
        else:
            dials[(current_dial - turn) % 100] += 1
    current_dial = rotate(direction, distance, current_dial)
    return current_dial, dials


def part1(document):
    zero_counts = 0
    current_dial = 50
    for direction, distance in parse(document):
        current_dial = rotate(direction, distance, current_dial)
        if current_dial == 0:
            zero_counts += 1
    return zero_counts


def part2(document):
    dials = {i: 0 for i in range(100)}
    current_dial = 50
    for direction, distance in parse(document):
        current_dial, dials = click(direction, distance, current_dial, dials)
    return dials[0]


def main(part: int = 1) -> int:
    with open("2025/data/day01.txt") as f:
        document = f.read()
    if part == 1:
        return part1(document)
    else:
        return part2(document)


if __name__ == "__main__":
    document = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

    assert part1(document) == 3
    print(main())

    assert part2(document) == 6
    assert (
        click(
            direction="R",
            distance=1000,
            current_dial=50,
            dials={i: 0 for i in range(100)},
        )[0]
        == 50
    )
    print(main(part=2))
