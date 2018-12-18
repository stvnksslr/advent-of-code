from unittest import TestCase
from advent_of_code.day1 import day1, day1_constants


class Day1Test(TestCase):
    def setUp(self):
        self.expected_list = day1_constants.TEST_LIST
        self.new_frequency = 1
        self.current_frequency = 1
        self.expected_adjusted_frequency = self.new_frequency + self.current_frequency
        self.first_pair_match = -18

    def test__day1_parser_returns_expected_list(self):
        """
        Method: parse_csv()
        Precondition: parsed list should match expected outcome
        Result: list matches expected outcome
        """
        list_of_frequencies = []
        day1.Day1.parse_csv(list_of_frequencies)
        self.assertEqual(list_of_frequencies, self.expected_list)

    def test__day1_adjust_frequency_returns_added_value(self):
        """
        Method: adjust_frequency()
        Precondition: two integers should be properly added
        Result: 1 + 1 should return 2
        """

        summed_frequencies = day1.Day1.adjust_frequency(
            new_frequency=self.new_frequency, current_frequency=self.current_frequency
        )
        self.assertEqual(summed_frequencies, self.expected_adjusted_frequency)

    def test__day1_find_duplicates_test(self):
        """
        Method: find_duplicates()
        Precondition: input a list of numbers, first set of numbers to repeat will be returned
        Result: should return -18 as it is the first set in the list to repeat
        """
        first_pair = day1.Day1.find_duplicates(self.expected_list)
        self.assertEqual(first_pair, self.first_pair_match)

    def test__day1_challenge(self):
        """
        Method: Challenge
        Precondition: do multiple passes over the list until it finds duplicate sums
        Result: should exit the loop upon finding the first duplicate sum pair, that sum should be 7614
        """
        current_frequency = 0
        list_of_frequencies = day1_constants.TEST_LIST
        list_of_sums = []

        duplicate_checker = True

        while duplicate_checker:
            for frequency in list_of_frequencies:
                current_frequency = frequency + current_frequency
                list_of_sums.append(current_frequency)
            first_pair = day1.Day1.find_duplicates(list_of_sums)
            if first_pair:
                print(first_pair)
                duplicate_checker = False
                self.assertEqual(first_pair, 76414)
        self.assertFalse(duplicate_checker)
