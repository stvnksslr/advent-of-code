import csv
from collections import Counter
from pathlib import Path

data_folder = Path("csv")
file_to_open = data_folder / "2nd_challenge.csv"


class Day2:
    @staticmethod
    def find_duplicates(list):
        set_ = set()
        for item in list:
            if item in set_:
                return item
            set_.add(item)
        return None

    @staticmethod
    def find_duplicate_in_string(input_string):
        char_counter = Counter(input_string)
        char_tally = {"double": 0, "tripple": 0}

        for character in char_counter:
            if char_counter[character] == 2:
                char_tally["double"] = +1
            if char_counter[character] == 3:
                char_tally["tripple"] = +1
        return char_tally

    @staticmethod
    def parse_csv():
        with open(file_to_open) as csv_file:
            parse_reader = csv.reader(csv_file, delimiter=",")
            list_of_ids = []
            for row in parse_reader:
                current_row = int(row[0])
                list_of_ids.append(current_row)
            return list_of_ids

