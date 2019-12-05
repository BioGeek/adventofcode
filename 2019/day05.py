# memory = '3,0,4,0,99'
memory = '1002,4,3,4,33'

code = [int(x) for x in memory.split(",")]

i = 0

while i < len(code):
    full_opcode = str(code[i]).zfill(5)

    opcode = int(full_opcode[-2:])
    parameter_modes = list(reversed([int(x) for x in full_opcode[:3]]))
    print(f"parameter_modes: {parameter_modes}")

    if parameter_modes[0] == 0: # position_mode
        param_1 = code[code[i+1]]
    else:
        param_1 = code[i+1]
    print(f"param_1: {param_1}")

    if parameter_modes[1] == 0: # position_mode
        param_2 = code[code[i+2]]
    else:
        param_2 = code[i+2]
    print(f"param_2: {param_2}")

    if parameter_modes[2] == 0: # position_mode
        param_3 = code[code[i+3]]
    else:
        param_3 = code[i+3]
    print(f"param_3: {param_3}")


    print(f"opcode: {opcode}")

    if opcode in (3, 4):
        instruction_length = 2
    else:
        instruction_length = 4

    print(f"instruction_length: {instruction_length}")

    instruction = code[i:i+instruction_length]

    print(f"instruction: {instruction}")

    if opcode == 3:
        output_pos = code[i+1]
        code[output_pos] = int(input('> '))
    elif opcode == 4:
        output_pos = param_1
        print(code[output_pos])
    elif opcode == 1:
        code[i+3] = param_1 + param_2
    elif opcode == 2:
        code[i+3] = param_1 * param_2
    elif opcode == 99:
        break

    print(f"code: {code}")

    i += instruction_length





