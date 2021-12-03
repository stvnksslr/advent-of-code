from day1_puzzle_input import PUZZLE_INPUT


def iterate_and_check_depth(input_list):
    previous_depth = 0
    depth_counter = 0
    for idx, depth in enumerate(input_list):
        if idx == 1:
            previous_depth = depth
            pass
        else:
            depth_counter = greater_depth_check(depth, depth_counter, previous_depth)
            previous_depth = depth
    return depth_counter


def greater_depth_check(depth, depth_counter, previous_depth):
    if depth > previous_depth:
        depth_counter += 1
    return depth_counter


def check_list_of_summed_depths(input_list):
    previous_depth_sum = 0
    depth_counter = 0
    for idx, depth in enumerate(input_list):
        current_depth = idx
        second_index = current_depth + 1
        third_index = second_index + 1

        if current_depth < len(input_list) \
                and second_index < len(input_list) \
                and third_index < len(input_list):
            current_sum = input_list[current_depth] + \
                          input_list[second_index] + \
                          input_list[third_index]

            if previous_depth_sum == 0:
                previous_depth_sum = current_sum
                pass
            else:
                if current_sum > previous_depth_sum:
                    depth_counter += 1
                previous_depth_sum = current_sum
    return depth_counter


def part1_1():
    return print(iterate_and_check_depth(PUZZLE_INPUT))


def part1_2():
    return print(check_list_of_summed_depths(PUZZLE_INPUT))


if __name__ == "__main__":
    part1_1()  # 1502
    part1_2()  # 1538
