import re
import turtle
from typing import List, Tuple


def navigate(instructions: str) -> int:
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


# currently gives following error (on WSL):
"""
Traceback (most recent call last):
  File "/home/jeroen/personal/adventofcode/2020/day12.py", line 50, in <module>
    print(navigate(instructions))
  File "/home/jeroen/personal/adventofcode/2020/day12.py", line 26, in navigate
    turtle.forward(value)
  File "<string>", line 6, in forward
  File "/home/jeroen/.pyenv/versions/3.10.0/lib/python3.10/turtle.py", line 3813, in __init__
    Turtle._screen = Screen()
  File "/home/jeroen/.pyenv/versions/3.10.0/lib/python3.10/turtle.py", line 3663, in Screen
    Turtle._screen = _Screen()
  File "/home/jeroen/.pyenv/versions/3.10.0/lib/python3.10/turtle.py", line 3679, in __init__
    _Screen._root = self._root = _Root()
  File "/home/jeroen/.pyenv/versions/3.10.0/lib/python3.10/turtle.py", line 435, in __init__
    TK.Tk.__init__(self)
  File "/home/jeroen/.pyenv/versions/3.10.0/lib/python3.10/tkinter/__init__.py", line 2299, in __init__
    self.tk = _tkinter.create(screenName, baseName, className, interactive, wantobjects, useTk, sync, use)
_tkinter.TclError: couldn't connect to display ":0"
"""


if __name__ == "__main__":
    instructions = """F10
N3
F7
R90
F11"""
    print(navigate(instructions))
