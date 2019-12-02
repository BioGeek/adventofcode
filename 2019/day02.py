from typing import List, Callable

def process(code: List[int]) -> List[int]:
    """
    Process Intcode.
    """
    for i in range(0, len(code), 4):
        try:
            opcode, input_1, input_2, output = code[i:i+4]
        except ValueError:
            opcode = code[i]
        if opcode == 1:
            code[output] = code[input_1] + code[input_2]
        elif opcode == 2:
            code[output] = code[input_1] * code[input_2]
        elif opcode == 99:
            return code
        else:
            raise RuntimeError("Shouldn't get here!")

def restore(raw: str) -> List[int]:
    """
    restore the gravity assist program to the "1202 program alarm" state.
    """
    code = [int(x) for x in  raw.split(',')]
    code[1] = 12
    code[2] = 2
    return code


def main(func: Callable) -> int:
    """
    What value is left at position 0 after the program halts?
    """
    with open('data/day02.txt') as f:
        code = f.read()

    return func(restore(code))[0]

if __name__ ==  '__main__':
    assert process([1,0,0,0,99]) == [2,0,0,0,99]
    assert process([2,3,0,3,99]) == [2,3,0,6,99]
    assert process([2,4,4,5,99,0]) == [2,4,4,5,99,9801]
    assert process([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99]
    assert process([1,9,10,3,2,3,11,0,99,30,40,50]) == [3500,9,10,70,2,3,11,0,99,30,40,50]

    print(main(process))