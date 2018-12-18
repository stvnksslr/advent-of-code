import day1


current_frequency = 0
list_of_frequencies = []
day1.parse_csv()
print(list_of_frequencies)
for frequency in list_of_frequencies:
    adjusted_frequency = day1.adjust_frequency(frequency, current_frequency)
    current_frequency = adjusted_frequency + current_frequency
print(current_frequency)
