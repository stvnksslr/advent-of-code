# opcode short hand
# 1 addition
# 2 multiply
# 99 break


def collect_input(file_input):
    with open(file_input) as file:
        parsed_input = list(map(lambda a: int(a), file.read().split(",")))
    return parsed_input


def parse_opcode(opcode_input):
    parsed_opcode = 0
    return parsed_opcode


def parse_program_to_opcodes(program_input):
    list_of_instructions = [
        program_input[i * 4 : (i + 1) * 4]
        for i in range((len(program_input) + 4 - 1) // 4)
    ]
    return list_of_instructions


def run_op_codes(program_input):
    input = list(map(lambda a: int(a), program_input))

    opcode, index = int(input[0]), 0
    while opcode != 99:
        if opcode == 1:
            sum = input[input[index + 1]] + input[input[index + 2]]
            input[input[index + 3]] = sum
        elif opcode == 2:
            product = input[input[index + 1]] * input[input[index + 2]]
            input[input[index + 3]] = product
        elif opcode != 99:
            break

        index += 4
        opcode = input[index]
        return input[0]
