import csv
from pathlib import Path

data_folder = Path("csv")
file_to_open = data_folder / "2nd_challenge.csv"


class Day2:
    @staticmethod
    def parse_csv():
        with open(file_to_open) as csv_file:
            parse_reader = csv.reader(csv_file, delimiter=",")
            list_of_ids = []
            for row in parse_reader:
                current_row = int(row[0])
                list_of_ids.append(current_row)
            return list_of_ids
