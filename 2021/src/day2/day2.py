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
        if instruction[0] == 'up':
            starting_vertical = starting_vertical - int(instruction[1])
        if instruction[0] == 'down':
            starting_vertical = starting_vertical + int(instruction[1])

    print(f'starting_horizontal: {starting_horizontal}')
    print(f'starting_vertical: {starting_vertical}')
    return starting_horizontal * starting_vertical


def calculate_instructions_with_aim(input_list):
    aim = 0
    horizontal_position = 0
    vertical_position = 0

    for instruction in input_list:
        # movement
        if instruction[0] == 'forward':
            horizontal_position = horizontal_position + int(instruction[1])
            vertical_position = vertical_position + (aim * int(instruction[1]))

        # aim adjustments
        if instruction[0] == 'up':
            aim = aim - int(instruction[1])
        if instruction[0] == 'down':
            aim = aim + int(instruction[1])

    print(f'starting_horizontal: {horizontal_position}')
    print(f'starting_vertical: {vertical_position}')
    return horizontal_position * vertical_position


def day2_1():
    print(calculate_instructions(PUZZLE_INPUT))


def day2_2():
    print(calculate_instructions_with_aim(PUZZLE_INPUT))


if __name__ == '__main__':
    day2_1()  # 2102357
    day2_2()  # 2101031224
