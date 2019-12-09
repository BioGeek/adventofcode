from collections import defaultdict
import sys
from typing import List, DefaultDict

sys.setrecursionlimit(2000)


class Tree:
    def __init__(self, name: str, children: List[str]) -> None:
        self.name = name
        self.children: List[Tree] = []
        self.parent = None
        for child_name in children:
            child = Tree(child_name, planets[child_name])
            child.parent = self
            self.children.append(child)

    def __str__(self) -> str:
        result = f"{self.name}"
        if self.children:
            kids = "(" + ", ".join([str(child) for child in self.children]) + ")"
        else:
            kids = ""
        return f"{result} {kids}"


def get_data() -> List[str]:
    with open("data/day06.txt") as f:
        lines = f.read().splitlines()
    return lines


Planets = DefaultDict[str, List[str]]


def get_planets(lines: List[str]) -> Planets:
    planets = defaultdict(list)
    for line in lines:
        a, b = line.split(")")
        planets[a].append(b)
    return planets


def create_root(planets: Planets) -> Tree:
    return Tree("COM", planets["COM"])


grand_total = 0


def count(current: Tree, total: int, previous: int) -> int:
    global grand_total
    for child in current.children:
        total = 1 + previous
        grand_total += total
        count(child, total, total)

    return grand_total


def main(lines: List[str], part: int = 1) -> int:
    root = create_root(planets)
    return count(root, 0, 0)


if __name__ == "__main__":

    """
        G - H       J - K - L
        /           /
    COM - B - C - D - E - F
                \
                 I
    """

    lines = """COM)B
    B)C
    C)D
    D)E
    E)F
    B)G
    G)H
    D)I
    E)J
    J)K
    K)L""".splitlines()

    planets = get_planets(lines)
    print(main(lines))
