import collections

from src.day3.day3_puzzle_input import PUZZLE_INPUT


def split_bits(input_list):
    list_of_lists = []
    for bit in input_list:
        split_bit = list(bit)
        list_of_lists.append(split_bit)
    return list_of_lists


def calculate_gamma(input_list):
    _gamma = []
    for idx, binary_set in enumerate(input_list):
        _gamma.append(int(collections.Counter(input_list[idx]).most_common()[0][0]))

    _gamma = [str(integer) for integer in _gamma]
    _gamma = "".join(_gamma)
    return _gamma


def calculate_epsilon(input_list):
    _epsilon = []
    for idx, binary_set in enumerate(input_list):
        _epsilon.append(int(collections.Counter(input_list[idx]).most_common()[1][0]))

    _epsilon = [str(integer) for integer in _epsilon]
    _epsilon = "".join(_epsilon)
    return _epsilon


def convert_to_int(binary):
    return int(binary, 2)


def generate_segment_list(input_list):
    segment_list = []
    for idx, binary_set in enumerate(input_list[0]):
        segment_list.append(list(list(zip(*input_list))[idx]))
    return segment_list


def day3_1():
    list_of_bit_lists = split_bits(PUZZLE_INPUT)
    segment_list = generate_segment_list(list_of_bit_lists)
    gamma = convert_to_int(calculate_gamma(segment_list))
    epsilon = convert_to_int(calculate_epsilon(segment_list))

    print(gamma)
    print(epsilon)

    power_consumption = gamma * epsilon
    return print(power_consumption)


if __name__ == "__main__":
    day3_1()  # 1540244
