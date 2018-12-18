import csv
from pathlib import Path

data_folder = Path("csv")
file_to_open = data_folder / "1st_challenge.csv"


class Day1:
    @staticmethod
    def find_duplicates(list):
        set_ = set()
        for item in list:
            if item in set_:
                return item
            set_.add(item)
        return None

    @staticmethod
    def adjust_frequency(new_frequency, current_frequency):
        adjusted_frequency = new_frequency + current_frequency
        return adjusted_frequency

    @staticmethod
    def parse_csv(list_of_frequencies):
        with open(file_to_open) as csv_file:
            parse_reader = csv.reader(csv_file, delimiter=",")

            for row in parse_reader:
                current_row = int(row[0])
                list_of_frequencies.append(current_row)
            return list_of_frequencies
