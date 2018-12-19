from collections import Counter
from advent_of_code.day2.box_id_tally import BoxIdTally


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
    def find_similar_strings(input_list):
        ids_within_1 = []
        for box_id in input_list:
            for box_id_to_match in input_list:
                if box_id != box_id_to_match:
                    hammed_distance = Day2.distance_hammed(box_id, box_id_to_match)
                    if hammed_distance <= 1:
                        box_id_within_1_ham = box_id
                        ids_within_1.append(box_id_within_1_ham)
        return ids_within_1

    @staticmethod
    def create_hash_from_duplicates(BoxIdTally):
        list_hash = BoxIdTally.double * BoxIdTally.triple
        return list_hash

    @staticmethod
    def distance_hammed(input_string1, input_string2):
        assert len(input_string1) == len(input_string2)
        return sum(c1 != c2 for c1, c2 in zip(input_string1, input_string2))
