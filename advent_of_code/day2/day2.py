from collections import Counter
from pathlib import Path
from advent_of_code.day2.box_id_tally import BoxIdTally

data_folder = Path("csv")
file_to_open = data_folder / "2nd_challenge.csv"


class Day2:
    @staticmethod
    def find_duplicate_in_string(input_string):
        char_counter = Counter(input_string)
        char_tally = BoxIdTally(double=0, triple=0)

        for character in char_counter:
            if char_counter[character] == 2:
                char_tally.double = +1
            if char_counter[character] == 3:
                char_tally.triple = +1
        return char_tally

    @staticmethod
    def find_and_tally_duplicates_in_list(input_list):
        char_tally = BoxIdTally(double=0, triple=0)
        for box_id in input_list:
            current_tally = Day2.find_duplicate_in_string(box_id)
            char_tally.double = char_tally.double + current_tally.double
            char_tally.triple = char_tally.triple + current_tally.triple
        return char_tally

    @staticmethod
    def create_hash_from_duplicates(BoxIdTally):
        list_hash = BoxIdTally.double * BoxIdTally.triple
        return list_hash
