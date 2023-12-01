import re
import turtle
from typing import List, Tuple


def navigate(instructions: str) -> int:  # type: ignore
    for action, value in parse(instructions):
        match action:
            case "E":
                (x, y) = turtle.position()
                turtle.setposition(x + value, y)
            case "W":
                (x, y) = turtle.position()
                turtle.setposition(x - value, y)
            case "N":
                (x, y) = turtle.position()
                turtle.setposition(x, y + value)
            case "S":
                (x, y) = turtle.position()
                turtle.setposition(x, y - value)
            case "L":
                turtle.left(value)
            case "R":
                turtle.right(value)
            case "F":
                turtle.forward(value)
            case _:
                raise AssertionError()
        print(turtle.position())


def parse(instructions: str) -> List[Tuple[str, int]]:
    "Returns a List of (action, value) pairs fromthe instructions"
    return [
        (action, int(value))
        for action, value in re.findall(r"(N|E|S|W|L|R|F)(\d+)", instructions)
    ]


if __name__ == "__main__":
    instructions = """F10
N3
F7
R90
F11"""
    print(navigate(instructions))
