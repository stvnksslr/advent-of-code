from advent_of_code.day1 import day1, day1_constants


class TestDay1Parse:
    def setup(self):
        self.expected_list = day1_constants.TEST_LIST
        self.input_frequency = 1
        self.current_frequency = 1
        self.expected_adjusted_frequency = self.input_frequency + self.current_frequency

    def test__day1_parser_returns_expected_list(self):
        """
        Method: parse_csv()
        Precondition: parsed list should match expected outcome
        Result: list matches expected outcome
        """
        self.list_of_frquencies = []
        day1.Day1.parse_csv(self.list_of_frquencies)
        assert self.list_of_frquencies == self.expected_list

    def test__day1_adjust_frequency_returns_added_value(self):
        """
        Method: adjust_frequency()
        Precondition: two integers should be properly added
        Result: 1 + 1 should return 2
        """
        summed_frequencies = day1.Day1.adjust_frequency(
            new_frequency=self.input_frequency, current_frequency=self.current_frequency
        )
        assert summed_frequencies == self.expected_adjusted_frequency

    def test__day1_find_duplicates_test(self):
        """
        Method: find_duplicates()
        Precondition: input a list of numbers, first set of numbers to repeat will be returned
        Result: should return -18 as it is the first set in the list to repeat
        """
        self.list_of_duplicates = day1.Day1.find_duplicates(self.expected_list)
        assert self.list_of_duplicates == -18
