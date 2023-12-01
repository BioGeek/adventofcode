DIGITS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def find_offsets(haystack, needle):
    """
    Find the start of all (possibly-overlapping) instances of needle in haystack
    Credit: https://stackoverflow.com/a/11122388/50065
    """
    offs = -1
    while True:
        offs = haystack.find(needle, offs + 1)
        if offs == -1:
            break
        else:
            yield offs


def get_calibartion_value(line: str, part: int = 1) -> int:
    digits = list(map(str, range(10)))
    if part == 2:
        digits = digits + list(DIGITS.keys())
    locations = {}
    for digit in digits:
        offsets = find_offsets(line, digit)
        for offset in offsets:
            locations[offset] = digit

    first = locations[min(locations.keys())]
    last = locations[max(locations.keys())]
    # print(line, locations, first, last, DIGITS.get(first, first), DIGITS.get(last, last))
    return int(DIGITS.get(first, first) + DIGITS.get(last, last))


def main(part: int = 1) -> int:
    with open("2023/data/day01.txt") as f:
        document = f.read()
    return sum(get_calibartion_value(line, part) for line in document.splitlines())


if __name__ == "__main__":
    assert get_calibartion_value("1abc2") == 12
    assert get_calibartion_value("pqr3stu8vwx") == 38
    assert get_calibartion_value("a1b2c3d4e5f") == 15
    assert get_calibartion_value("treb7uchet") == 77

    assert get_calibartion_value("3fourrbvvlrsrbb2858") == 38

    document = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

    assert sum(get_calibartion_value(line) for line in document.splitlines()) == 142

    print(main())

    assert get_calibartion_value("two1nine", part=2) == 29
    assert get_calibartion_value("eightwothree", part=2) == 83
    assert get_calibartion_value("abcone2threexyz", part=2) == 13
    assert get_calibartion_value("xtwone3four", part=2) == 24
    assert get_calibartion_value("4nineeightseven2", part=2) == 42
    assert get_calibartion_value("zoneight234", part=2) == 14
    assert get_calibartion_value("7pqrstsixteen", part=2) == 76

    document = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

    print(main(part=2))
