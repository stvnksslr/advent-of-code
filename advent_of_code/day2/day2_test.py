from unittest import TestCase
from advent_of_code.day2 import day2, day2_constants


class Day2Test(TestCase):
    def setUp(self):
        self.list_of_box_ids = day2_constants.LIST_OF_BOX_IDS
        self.dictionary_of_duplicates = {}
        self.box_id_with_no_dups = "abcdef"
        self.box_id_with_two_dups = "bababc"
        self.box_id_with_two_dups_results = {"pair_count": 2, "tripple_count": 3}

    def test__check_if_string_has_duplicates_no_dups(self):
        """
        Method: find_duplicates()
        Precondition: method should return a truthy value if pairs were found
        Result: find duplicates should return no pairs
        """
        repeated_letters = day2.Day2.find_duplicates(self.box_id_with_no_dups)
        self.assertFalse(repeated_letters)

    def test__check_if_string_has_duplicates_two_duplicates(self):
        """
        Method: find_duplicate_in_string()
        Precondition: method should return a truthy value if pairs were found
        Result: should find two sets of duplicates a:1 b:1
        """
        repeated_letters = day2.Day2.find_duplicate_in_string(self.box_id_with_two_dups)
        self.assertTrue(repeated_letters)

    def test__Challenge_day2_part1(self):
        """
        Method: TODO:
        Precondition: Method should return a has based on results
        Result: Of these box IDs, four of them contain a letter which appears exactly twice,
        and three of them contain a letter which appears exactly three times
        """
        for box_id in self.list_of_box_ids:
            day2.Day2.find_duplicates(box_id)
