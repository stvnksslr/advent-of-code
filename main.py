import day1
import day1_constants

current_frequency = 0
list_of_frequencies = day1_constants.TEST_LIST
list_of_sums = []

for frequency in list_of_frequencies:
    current_frequency = frequency + current_frequency
    list_of_sums.append(current_frequency)
    # list_of_sums = list_of_sums.append(current_frequency)

first_pair = day1.Day1.find_duplicates(list_of_sums)
print(first_pair)