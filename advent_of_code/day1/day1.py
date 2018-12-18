import csv


class Day1:
    def find_duplicates(list):
        set_ = set()
        for item in list:
            if item in set_:
                return item
            set_.add(item)
        return None

    def adjust_frequency(new_frequency, current_frequency):
        adjusted_frequency = new_frequency + current_frequency
        return adjusted_frequency

    def parse_csv(list_of_frequencies):
        with open("advent_of_code/day1/1st_challenge.csv") as csv_file:
            parse_reader = csv.reader(csv_file, delimiter=",")

            for row in parse_reader:
                current_row = int(row[0])
                list_of_frequencies.append(current_row)
            return list_of_frequencies
