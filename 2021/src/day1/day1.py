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


if __name__ == "__main__":
    print(iterate_and_check_depth(PUZZLE_INPUT))
