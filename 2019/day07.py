import itertools
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
        self.result = self.memory[par1]  # type: ignore

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
    with open("./data/day07.txt") as f:
        data = f.read()
    return data


def calculate(data: str, input_: Tuple = ()) -> int:
    tape = list(map(int, data.split(",")))
    computer = Computer(tape, input_=input_)
    computer.run()
    return computer.result if computer.result is not None else computer.memory[-1]


def main(data: str, part: int = 1) -> int:
    max_thruster = 0
    if part == 1:
        for (a, b, c, d, e) in itertools.permutations(range(5)):
            A = calculate(data, (a, 0))
            B = calculate(data, (b, A))
            C = calculate(data, (c, B))
            D = calculate(data, (d, C))
            thruster = calculate(data, (e, D))
            if thruster > max_thruster:
                max_thruster = thruster
    else:
        thruster = None  # type: ignore
        for (a, b, c, d, e) in itertools.permutations(range(5, 10)):
            while True:
                inp = thruster if thruster is not None else 0
                A = calculate(data, (a, inp))
                B = calculate(data, (b, A))
                C = calculate(data, (c, B))
                D = calculate(data, (d, C))
                thruster = calculate(data, (e, D))
                if thruster > max_thruster:
                    max_thruster = thruster
    return max_thruster


if __name__ == "__main__":
    assert main("3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0") == 43210
    assert (
        main(
            "3,23,3,24,1002,24,10,24,1002,23,-1,"
            "23,101,5,23,23,1,24,23,23,4,23,99,0,0"
        )
    ) == 54321

    assert (
        main(
            "3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,"
            "1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0"
        )
        == 65210
    )

    print(main(get_data()))

    assert (
        main(
            "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5",
            part=2,
        )
        == 139629729
    )
