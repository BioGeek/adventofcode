# type: ignore
from dataclasses import dataclass
from typing import Iterable


@dataclass
class Location:
    horizontal: int = 0
    depth: int = 0
    aim: int = 0


def parse(line: str, location: Location, part: int) -> Location:
    match line.split():
        case ["forward", distance]:
            location.horizontal += int(distance)
            if part == 2:
                location.depth += location.aim * int(distance)
        case ["down", distance]:
            if part == 1:
                location.depth += int(distance)
            else:
                location.aim += int(distance)
        case ["up", distance]:
            if part == 1:
                location.depth -= int(distance)
            else:
                location.aim -= int(distance)
        case _:
            print(line)
    return location


def commands(course: str, part: int = 1) -> Iterable[int]:
    location = Location()
    for line in course.splitlines():
        location = parse(line, location, part)
    return location.horizontal * location.depth


def main(part: int = 1) -> int:
    with open("2021/data/day02.txt") as f:
        course = f.read()
    return commands(course, part)


if __name__ == "__main__":
    course = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""
    assert commands(course) == 150
    assert commands(course, part=2) == 900

    print(main())
    print(main(part=2))
