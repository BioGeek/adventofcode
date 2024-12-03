import re


def instructions(memory):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    return sum(
        int(match.group(1)) * int(match.group(2))
        for match in re.finditer(pattern, memory)
    )


def conditional_statements(memory):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"
    total = 0
    add = True
    for match in re.finditer(pattern, memory):
        if match.group() == "don't()":
            add = False
        elif match.group() == "do()":
            add = True
        elif add:
            total += int(match.group(1)) * int(match.group(2))
    return total


def main(part: int = 1) -> int:
    with open("2024/data/day03.txt") as f:
        memory = f.read()
    if part == 1:
        return instructions(memory)
    return conditional_statements(memory)


if __name__ == "__main__":
    memory = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

    assert instructions(memory) == 161

    print(main())

    memory = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

    assert conditional_statements(memory) == 48

    print(main(part=2))
