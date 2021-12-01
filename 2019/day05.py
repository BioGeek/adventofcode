# Modified from https://topaz.github.io/paste/#XQAAAQCjCwAAAAAAAAAxmwhIY/U9BVB8ketYSB/W/NutdEboIvBfWJ+1QHbig7u8l6S6tBVwkP/7L841apnc8F6zu1YfX4UYbApL02QLco5ugavURrTEtuVj6egSJHJOHl36HlzBJsJOCoHouYcjBEeoX7Jdyeo20+mqjqm2BhpIAA1OauvjkV0Y/MYcVvGukbD2ZYmDLCU/FDKQweJK1CduwTeNpxKqEr6kPpAWEXzvqTVrilDPICwHY05UytxoxEDT6HpNEY0vQ+o+qseJ2VwY3KJi9DzU+uwz9YYazsFtAZMCBwoYchHSbGSGAS8UO/E08DVxCCK90oCbj6WoOtFdUdZyYCZErlJX77ROEnXzUEODQN89D6fFmCbpOtYI8FTMW/J5vhoPVoloLP38dLWjv+5XwXI/iiKmZd4qTd4t5YPYiMAsbO/S9qrm8gFPfhEUQgQCfwzidmfiz4a5n9U2Cvkki5vqOKKtykcW8XnOtlFP9Oh8NufwRnnI+e7yZs3W2z/ns6sHcgOmjFLlvg5GPqVQJFDXWSKQDGxvB7YI5U8y1WaP68uXU/APalo2qs72Bw/NnMELtx45ddDLaYWaUTSSYibquNj0pgPahWEn3jmUq1vDhZ7RHz8V5n32XQEer5aK22ZkoJQkOd4RBl2aQIVgfZgfuuVCJNbQu0nf7Y7fJkL5BxDm2ieYt7xc92eylGZIzQUHB6+dtmWAq/pkiks27kXKv1OVFgsBH2V0UN8bpH1+EeX9TwForjUDSOehAdarqPX1PVk9GU2Vc5x9UoEBqDYE8fLBwGFZPKwWvmbnjQBu13n6jjqhWQ+jtTpAsmTWY35+THC2scmTMkNWXoQmVyaqnQdr3ck+SWlGZYby7aSHupgK/U7I4vLn+2N7NLH/cydT3y2Kx/0++jo5YOOuQ+rcbObBIuT/FKeinxvXKY9r4C11bKqhDS42G9u9aBkN3fmmPGBWt6AA8vkkKL1GfLD8ZuPByad4KEBR1C7OZemf8Km3wyNQdu1lxuUnL/p34ymqMid07SaGsPdfv1uPhEioIjCEecb8dZBM # noqa: E501

from typing import List, Tuple


class ComputationFinished(Exception):
    pass


class Computer:
    def __init__(self, memory: List[int], input_: Tuple = (), pointer: int = 0) -> None:
        self.memory = memory
        self.pointer = pointer
        self.input = iter(input_)
        self.result = None

        self.READ_MODES = {
            0: (self.point, self.point, self.point),
            1: (self.value, self.point, self.point),
            10: (self.point, self.value, self.point),
            11: (self.value, self.value, self.point),
            100: (self.point, self.point, self.value),
            101: (self.value, self.point, self.value),
            110: (self.point, self.value, self.value),
            111: (self.value, self.value, self.value),
        }

        self.OP_CODES = {
            1: (self.op_add, 3),
            2: (self.op_mul, 3),
            3: (self.op_input, 1),
            4: (self.op_print, 1),
            5: (self.op_jit, 2),
            6: (self.op_jif, 2),
            7: (self.op_lt, 3),
            8: (self.op_eq, 3),
            99: (self.op_exit, 0),
        }

    def value(self, location: int) -> int:
        return location

    def point(self, location: int) -> int:
        return self.memory[location]

    def step(self) -> None:
        op, parameters, offset = self.read_opcode(self.pointer)
        self.pointer += offset
        op(*parameters)

    def get_parameters(self, argument_functions, pointer: int) -> List[int]:
        return [
            f(ptr)
            for f, ptr in zip(argument_functions, range(pointer + 1, pointer + 4))
        ]

    def read_opcode(self, pointer: int):
        code = self.memory[pointer]
        readmodes, opcode = divmod(code, 100)
        op, nargs = self.OP_CODES[opcode]
        argument_functions = self.READ_MODES[readmodes][:nargs]
        parameters = self.get_parameters(argument_functions, pointer)
        return op, parameters, nargs + 1

    def run(self) -> None:
        try:
            while True:
                self.step()
        except ComputationFinished:
            return

    def op_add(self, par1: int, par2: int, par3: int) -> None:
        self.memory[par3] = self.memory[par1] + self.memory[par2]

    def op_mul(self, par1: int, par2: int, par3: int) -> None:
        self.memory[par3] = self.memory[par1] * self.memory[par2]

    def op_input(self, par1: int) -> None:
        self.memory[par1] = next(self.input)

    def op_print(self, par1: int) -> None:
        self.result = self.memory[par1]

    def op_exit(self) -> None:
        raise ComputationFinished

    def op_jit(self, par1: int, par2: int) -> None:
        if self.memory[par1] != 0:
            self.pointer = self.memory[par2]

    def op_jif(self, par1: int, par2: int) -> None:
        if self.memory[par1] == 0:
            self.pointer = self.memory[par2]

    def op_lt(self, par1: int, par2: int, par3: int) -> None:
        self.memory[par3] = int(self.memory[par1] < self.memory[par2])

    def op_eq(self, par1: int, par2: int, par3: int) -> None:
        self.memory[par3] = int(self.memory[par1] == self.memory[par2])


def get_data() -> str:
    with open("data/day05.txt") as f:
        data = f.read()
    return data


def main(data: str, input_: Tuple = ()) -> int:
    tape = list(map(int, data.split(",")))
    computer = Computer(tape, input_=input_)
    computer.run()
    return computer.result if computer.result is not None else computer.memory[-1]


if __name__ == "__main__":
    assert main("3,0,4,0,99", (19,)) == 19
    assert main("1002,4,3,4,33") == 99
    print(main(get_data(), (1,)))

    assert main("3,9,8,9,10,9,4,9,99,-1,8", (8,)) == 1
    assert main("3,9,8,9,10,9,4,9,99,-1,8", (7,)) == 0
    assert main("3,9,8,9,10,9,4,9,99,-1,8", (9,)) == 0

    assert main("3,9,7,9,10,9,4,9,99,-1,8", (7,)) == 1
    assert main("3,9,7,9,10,9,4,9,99,-1,8", (8,)) == 0

    assert main("3,3,1108,-1,8,3,4,3,99", (8,)) == 1
    assert main("3,3,1108,-1,8,3,4,3,99", (7,)) == 0
    assert main("3,3,1108,-1,8,3,4,3,99", (9,)) == 0

    assert main("3,3,1107,-1,8,3,4,3,99", (7,)) == 1
    assert main("3,3,1107,-1,8,3,4,3,99", (8,)) == 0

    print(main(get_data(), (5,)))
