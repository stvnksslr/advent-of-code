from src.day2.day2_puzzle_input import PUZZLE_INPUT

# forward 5
# down 5
# forward 8
# up 3
# down 8
# forward 2

movement_instructions = [
    ("forward", 5),
    ("down", 5),
    ("forward", 8),
    ("up", 3),
    ("down", 8),
    ("forward", 2)
]


def calculate_instructions(input_list):
    starting_horizontal = 0
    starting_vertical = 0
    for instruction in input_list:
        if instruction[0] == 'forward':
            starting_horizontal = starting_horizontal + int(instruction[1])
        if instruction[0] == 'backward':
            starting_horizontal = starting_horizontal - int(instruction[1])
        if instruction[0] == 'up':
            starting_vertical = starting_vertical - int(instruction[1])
        if instruction[0] == 'down':
            starting_vertical = starting_vertical + int(instruction[1])

    print(f'starting_horizontal: {starting_horizontal}')
    print(f'starting_vertical: {starting_vertical}')
    return starting_horizontal * starting_vertical


def day2_1():
    print(calculate_instructions(PUZZLE_INPUT))


if __name__ == '__main__':
    day2_1()  # 2102357
