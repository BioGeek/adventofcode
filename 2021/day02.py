from dataclasses import dataclass

@dataclass
class Location:
    horizontal: int = 0
    depth: int = 0

def parse(line: str, location: Location) -> Location:
    match line.split():
        case ["forward", distance]:
            location.horizontal += int(distance)
        case ["down", distance]:
            location.depth += int(distance)
        case ["up", distance]:
            location.depth -= int(distance)
        case _:
            print(line)
    return location

def main(part: int = 1) -> int:
    with open("2021/data/day02.txt") as f:
        course = f.read()

    location = Location()
    for line in course.splitlines():
        location = parse(line, location)
        # print(location)
    return location.horizontal * location.depth





if __name__ == '__main__':
    course = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""
    print(main(course))
