from typing import List


def process(code: List[int]) -> List[int]:
    """Process Intcode."""
    for i in range(0, len(code), 4):
        try:
            opcode, input_1, input_2, output = code[i : i + 4]
        except ValueError:
            opcode = code[i]
        if opcode == 1:
            code[output] = code[input_1] + code[input_2]
        elif opcode == 2:
            code[output] = code[input_1] * code[input_2]
        elif opcode == 99:
            break
        else:
            raise AssertionError(f"Unrecognised opcode: {opcode}")

    return code


def initialize_memory(memory: str, noun: int = 12, verb: int = 2) -> List[int]:
    """Initialize the memory at addresses 1 and 2."""
    code = [int(x) for x in memory.split(",")]
    code[1] = noun
    code[2] = verb
    return code


def execute(memory: str, noun: int = 12, verb: int = 2) -> int:
    """Initialize the memory and process the code."""
    return process(initialize_memory(memory, noun, verb))[0]


def get_memory() -> str:
    """Read in the data."""
    with open("data/day02.txt") as f:
        memory = f.read()
    return memory


def main() -> int:
    """What value is left at position 0 after the program halts?"""
    memory = get_memory()
    return execute(memory)


def main2(desired: int = 19690720) -> int:
    """What pair of inputs produces the desired output?"""
    memory = get_memory()
    code = initialize_memory(memory)
    for noun in range(len(code)):
        for verb in range(len(code)):
            if execute(memory, noun, verb) == desired:
                result = (100 * noun) + verb
                break
    return result


if __name__ == "__main__":
    assert process([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
    assert process([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
    assert process([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
    assert process([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]
    assert process([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]) == [
        3500,
        9,
        10,
        70,
        2,
        3,
        11,
        0,
        99,
        30,
        40,
        50,
    ]

    print(main())
    print(main2())
