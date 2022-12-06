from typing import Generator, List, Tuple


def make_instructions(data: str) -> List[Tuple[str, int]]:
    instructions = []
    for line in data.splitlines():
        operation, argument = line.split()
        instructions.append((operation, int(argument)))
    return instructions


def detect_infinite_loop(instructions: List[Tuple[str, int]]) -> Tuple[int, bool]:
    visited = [False] * len(instructions)
    accumulator = 0
    index = 0

    terminated_normally = False

    try:
        while not visited[index]:
            operation, argument = instructions[index]

            if operation == "nop":
                visited[index] = True
                index += 1
            elif operation == "acc":
                accumulator += argument
                visited[index] = True
                index += 1
            elif operation == "jmp":
                visited[index] = True
                index += argument
    except IndexError:
        terminated_normally = True

    return accumulator, terminated_normally


def fix_corruption(instructions: List[Tuple[str, int]]) -> Generator:
    for i in range(len(instructions) - 1, 0, -1):
        operation, argument = instructions[i]
        if operation in ("jmp", "nop"):
            instructions[i] = ("nop" if operation == "jmp" else "jmp", argument)
            yield instructions
            instructions[i] = (operation, argument)


def main(part: int = 1) -> int:
    with open("2020/data/day08.txt") as fh:
        data = fh.read()

    instructions = make_instructions(data)
    if part == 1:
        accumulator, terminated_normally = detect_infinite_loop(instructions)
        return accumulator
    else:
        for instructions in fix_corruption(instructions):  # noqa: B020
            accumulator, terminated_normally = detect_infinite_loop(instructions)
            if terminated_normally:
                return accumulator
        return -1


if __name__ == "__main__":
    INSTRUCTIONS = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

    assert detect_infinite_loop(make_instructions(INSTRUCTIONS)) == (5, False)

    print(main())

    FIXED = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
nop -4
acc +6"""

    assert next(fix_corruption((make_instructions(INSTRUCTIONS)))) == make_instructions(
        FIXED
    )
    assert detect_infinite_loop(make_instructions(FIXED)) == (8, True)

    print(main(part=2))
