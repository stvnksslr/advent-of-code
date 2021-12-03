from src.day3.day3 import split_bits, generate_segment_list, calculate_gamma, calculate_epsilon, convert_to_int

MOCK_DATA = [
    '00100',
    '11110',
    '10110',
    '10111',
    '10101',
    '01111',
    '00111',
    '11100',
    '10000',
    '11001',
    '00010',
    '01010',
]


def test_find_most_common_bit():
    list_of_bit_lists = split_bits(MOCK_DATA)
    segment_list = generate_segment_list(list_of_bit_lists)
    gamma = calculate_gamma(segment_list)
    assert gamma == '10110'
    assert convert_to_int(gamma) == 22


def test_find_least_common_bit():
    list_of_bit_lists = split_bits(MOCK_DATA)
    segment_list = generate_segment_list(list_of_bit_lists)
    epsilon = calculate_epsilon(segment_list)
    assert epsilon == '01001'
    assert convert_to_int(epsilon) == 9


def test__calculate_power_consumption():
    list_of_bit_lists = split_bits(MOCK_DATA)
    segment_list = generate_segment_list(list_of_bit_lists)
    gamma = convert_to_int(calculate_gamma(segment_list))
    epsilon = convert_to_int(calculate_epsilon(segment_list))
    power_consumption = gamma * epsilon
    assert power_consumption == 198
