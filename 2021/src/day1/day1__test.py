from src.day1.day1 import iterate_and_check_depth, greater_depth_check, check_list_of_summed_depths

MOCK_DEPTH_RESULTS_COUNTER = 7
MOCK_DEPTHS = [
    199, 200, 208, 210, 200, 207, 240, 269, 260, 263
]

MOCK_DEPTH_RESULTS_SUM_COUNTER = 5
MOCK_DEPTHS_SUM = [
    607, 618, 618, 617, 647, 716, 769, 792
]


# 199 (N/A - no previous measurement)
# 200 (increased)
# 208 (increased)
# 210 (increased)
# 200 (decreased)
# 207 (increased)
# 240 (increased)
# 269 (increased)
# 260 (decreased)
# 263 (increased)

def test__check_list_of_depths():
    depth_counter = iterate_and_check_depth(input_list=MOCK_DEPTHS)
    assert depth_counter == 7


def test__greater_depth_check_greater():
    depth_counter = greater_depth_check(depth=200, depth_counter=0, previous_depth=199)
    assert depth_counter == 1


def test__greater_depth_check_less():
    depth_counter = greater_depth_check(depth=198, depth_counter=0, previous_depth=199)
    assert depth_counter == 0


# A: 607 (N/A - no previous sum)
# B: 618 (increased)
# C: 618 (no change)
# D: 617 (decreased)
# E: 647 (increased)
# F: 716 (increased)
# G: 769 (increased)
# H: 792 (increased)

def test__check_list_of_summed_depths():
    depth_counter = check_list_of_summed_depths(input_list=MOCK_DEPTHS_SUM)
    assert depth_counter == MOCK_DEPTH_RESULTS_SUM_COUNTER
