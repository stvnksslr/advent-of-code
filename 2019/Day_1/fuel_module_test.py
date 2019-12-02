from unittest import TestCase
from pathlib import Path
from Day_1.fuel_module import (
    collect_input,
    calculate_fuel,
    calculate_fuel_sum,
    calculate_additional_fuel_mass,
    day_1_solve_answer,
    day_1_pt2_solve_answer,
)


class FuelModuleTest(TestCase):
    def setUp(self):
        self.base_path = Path.cwd() / "Day_1"
        self.modules_input_path = str(self.base_path / "modules.txt")

    def test__load_inputs(self):
        list_of_modules = collect_input(self.modules_input_path)
        self.assertEqual(len(list_of_modules), 100)

    def test__calculate_fuel(self):
        initial_module_value = calculate_fuel(12)
        self.assertEqual(initial_module_value, 2)

    def test__calculate_fuel_complicated(self):
        initial_module_value = calculate_fuel(100756)
        self.assertEqual(initial_module_value, 33583)

    def test__calculate_fuel_sum(self):
        fuel_list = [12, 15, 20]
        fuel_sum = calculate_fuel_sum(fuel_list)
        self.assertEqual(fuel_sum, 47)

    def test__calculate_additional_fuel_mass(self):
        additional_mass = calculate_additional_fuel_mass(148454)
        list_of_additional_mass = 74192
        self.assertEqual(additional_mass, list_of_additional_mass)

    def test__day_1_pt1_solve_answer(self):
        total_fuel = day_1_solve_answer(self.modules_input_path)
        self.assertEqual(total_fuel, 3367126)

    def test__day_1_pt2_solve_answer(self):
        total_fuel_pt2 = day_1_pt2_solve_answer(self.modules_input_path)
        self.assertEqual(5047796, total_fuel_pt2)
