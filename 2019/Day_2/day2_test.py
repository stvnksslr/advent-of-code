from unittest import TestCase
from pathlib import Path
from Day_2.day2_pt1 import parse_program_to_opcodes, collect_input, run_op_codes


class TestDay2(TestCase):
    def setUp(self):
        self.base_path = Path.cwd() / "Day_2"
        self.modules_input_path = str(self.base_path / "input.txt")
        self.test_program_1 = [1, 0, 0, 0, 99]
        self.test_program_1_solution = [2, 4, 4, 5, 99, 9801]

    def test__day2_pt1_solution(self):
        program_input = collect_input(self.modules_input_path)
        op_codes = run_op_codes(program_input)
        self.assertEqual(op_codes, 1)

    def test__parse_program_to_opcodes(self):
        solution = [[1, 0, 0, 0], [99]]
        parsed_program = parse_program_to_opcodes(self.test_program_1)
        self.assertEqual(parsed_program, solution)
