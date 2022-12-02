from typing import List


def calories_per_elf(inventory: str) -> List[int]:
    supplies_per_elf = inventory.split("\n\n")
    return [sum(map(int, supplies.splitlines())) for supplies in supplies_per_elf]


def most_calories(inventory: str) -> int:
    return max(calories_per_elf(inventory))


def top_three_calories(inventory: str) -> int:
    top_three = sorted(calories_per_elf(inventory), reverse=True)[:3]
    return sum(top_three)


def main(part: int = 1):
    with open("2022/data/day01.txt") as f:
        inventory = f.read()
    if part == 1:
        return most_calories(inventory)
    else:
        return top_three_calories(inventory)


if __name__ == "__main__":
    inventory = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

    assert calories_per_elf(inventory) == [6000, 4000, 11000, 24000, 10000]
    assert most_calories(inventory) == 24000
    assert top_three_calories(inventory) == 45000

    print(main())
    print(main(part=2))
