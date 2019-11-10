from unittest import TestCase
from advent_of_code.day2 import day2, day2_constants
from advent_of_code.day2.box_id_tally import BoxIdTally


class Day2Test(TestCase):
    def setUp(self):
        self.list_of_box_ids = day2_constants.LIST_OF_BOX_IDS
        self.dictionary_of_duplicates = {}
        self.box_id_with_no_dups = "abcdef"
        self.box_id_with_1_double_1_triple = "bababc"
        self.box_id_with_1_double_1_triple_results = BoxIdTally(double=1, triple=1)
        self.box_id_with_no_duplicates = BoxIdTally(double=0, triple=0)
        self.box_id_with_2_double_1_triple = BoxIdTally(double=2, triple=1)
        self.list_of_3_box_ids = ["abcdef", "bababc", "abbcde"]
        self.list_of_3_box_ids_similar = ["aaa", "aab", "abc"]
        self.hamming_test_of_1_aaa = "aaa"
        self.hamming_test_of_1_aac = "aac"
        self.list_of_3_box_ids_hash = 2
        self.list_of_box_ids_hash = 6642

    def test__check_if_string_has_duplicates_no_dups(self):
        """
        Method: find_duplicates()
        Precondition: method should return a truthy value if pairs were found
        Result: find duplicates should return no pairs
        """
        repeated_letters = day2.Day2.find_duplicate_in_string(self.box_id_with_no_dups)
        self.assertEqual(repeated_letters.double, self.box_id_with_no_duplicates.double)
        self.assertEqual(repeated_letters.triple, self.box_id_with_no_duplicates.triple)

    def test__check_if_string_has_duplicates_has_dups(self):
        """
        Method: find_duplicate_in_string()
        Precondition: method should return a truthy value if pairs were found
        Result: should find two sets of duplicates double:1 tripple:1
        """
        repeated_letters = day2.Day2.find_duplicate_in_string(
            self.box_id_with_1_double_1_triple
        )
        self.assertEqual(
            self.box_id_with_1_double_1_triple_results.double, repeated_letters.double
        )
        self.assertEqual(
            self.box_id_with_1_double_1_triple_results.triple, repeated_letters.triple
        )

    def test__tally_duplicates_from_list(self):
        """
        Method: find_and_tally_duplicates_in_list()
        Precondition: method should find the duplicate counts in a list of strings
        Result: shpould find 3 sets of repeating characters  double:2 tripple:1
        """
        repeated_letters = day2.Day2.find_and_tally_duplicates_in_list(
            self.list_of_3_box_ids
        )
        self.assertEqual(
            self.box_id_with_2_double_1_triple.double, repeated_letters.double
        )
        self.assertEqual(
            self.box_id_with_2_double_1_triple.triple, repeated_letters.triple
        )

    def test__check_for_valid_hash(self):
        """
        Method: create_hash_from_duplicates()
        Precondition: Method should return a hash based on results
        Result: hash should = 2 * 1 = 2
        """
        repeated_letters = day2.Day2.find_and_tally_duplicates_in_list(
            self.list_of_3_box_ids
        )
        list_hash = day2.Day2.create_hash_from_duplicates(repeated_letters)
        self.assertEqual(list_hash, self.list_of_3_box_ids_hash)

    def test__find_similar_strings(self):
        """
        Method: find_similar_strings()
        Precondition: method should take a list of strings and 
        return ones that only differ by 1 character
        Result: [aaa, aab, abc] -> [aa, aa]
        """
        similar_strings = day2.Day2.find_similar_strings(self.list_of_3_box_ids_similar)
        self.assertEqual(len(similar_strings), 2)

    def test__hamming_distance_between_strings(self):
        """
        Method: hamming_distance()
        Precondition: two strings are entered as input they differ by 1
        Result: hamming distance method should return 1
        """
        distance_hammed = day2.Day2.distance_hammed(
            self.hamming_test_of_1_aaa, self.hamming_test_of_1_aac
        )
        self.assertEqual(1, distance_hammed)

    def test__Challenge_day2_part1(self):
        """
        Method: create_hash_from_duplicates
        Precondition: Method should return a has based on results
        Result: Of these box IDs, four of them contain a letter which appears exactly twice,
        and three of them contain a letter which appears exactly three times
        """
        repeated_letters = day2.Day2.find_and_tally_duplicates_in_list(
            self.list_of_box_ids
        )
        list_hash = day2.Day2.create_hash_from_duplicates(repeated_letters)
        self.assertEqual(list_hash, self.list_of_box_ids_hash)

    def test__Challenge_day2_part2(self):
        """
        Method: Find strings that are within 1 character of eachother
        Precondition: Entering large list and we should find the common character set
        Result: TOOD:
        """
        similar_strings = day2.Day2.find_similar_strings(self.list_of_box_ids)
        self.assertTrue(similar_strings)