from __future__ import annotations

import re
from collections import defaultdict
from typing import Dict, List, Set


class Bag:
    def __init__(self, color: str) -> None:
        self.color = color
        self.parents: List[Bag] = []
        self.children: Dict[Bag, int] = defaultdict(int)
        self.all_parent_colors: Set = set()
        self.child_color_count: int = 0

    def __str__(self):
        return f"{self.color} bag"

    def add_parent(self, parent: Bag) -> None:
        self.parents.append(parent)

    def add_child(self, child: Bag, count: int) -> None:
        self.children[child] += count

    def parent_colors(self) -> Set[str]:
        for parent in self.parents:
            self.all_parent_colors.add(parent.color)
            self.all_parent_colors |= parent.parent_colors()
        return self.all_parent_colors

    def child_colors(self) -> int:
        print(f"{self} has {len(self.children)} colors of children")
        for child, count in self.children.items():
            print(f"{count} x child {child}")
            self.child_color_count += count
            print(f"self.child_color_count += count -> {self.child_color_count}")
            self.child_color_count += count * child.child_colors()
        return self.child_color_count


def shiny_gold_bag(data: str) -> Bag:
    return make_bags(data)["shiny gold"]


def make_bags(data: str) -> Dict[str, Bag]:
    all_bags: Dict[str, Bag] = {}
    for line in data.splitlines():
        m = re.match("(.*) bags contain (.*).", line)
        if m:
            parent_color, children = m.groups()
            if parent_color in all_bags:
                parent_bag = all_bags[parent_color]
            else:
                parent_bag = Bag(parent_color)
                all_bags[parent_color] = parent_bag

            if children != "no other bags":
                for child in children.split(", "):
                    m2 = re.match(r"(\d)+ (.*) bag[s]?", child)
                    if m2:
                        count, child_color = m2.groups()
                        if child_color in all_bags:
                            child_bag = all_bags[child_color]
                        else:
                            child_bag = Bag(child_color)
                            all_bags[child_color] = child_bag

                        parent_bag.add_child(child_bag, int(count))
                        child_bag.add_parent(parent_bag)

                    else:
                        raise RuntimeError(f"Could not parse child '{child}'")
        else:
            raise RuntimeError(f"could not parse line '{line}'")
    return all_bags


def main(part: int = 1):
    with open("2020/data/day07.txt") as fh:
        data = fh.read()
    shiny = shiny_gold_bag(data)
    if part == 1:
        return len(shiny.parent_colors())
    else:
        return shiny.child_colors()


if __name__ == "__main__":
    EXAMPLE = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

    # assert len(shiny_gold_bag(EXAMPLE).parent_colors()) == 4

    # print(main())

    EXAMPLE_2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""

    SMALL = """shiny gold bags contain 2 dark red bags.
dark red bags contain 1 dark orange bag.
dark orange bags contain no other bags."""

    assert shiny_gold_bag(SMALL).child_colors() == 4
    assert shiny_gold_bag(EXAMPLE).child_colors() == 32
    assert shiny_gold_bag(EXAMPLE_2).child_colors() == 126

    print(main(part=2))  # 7162, 7161 too high"
