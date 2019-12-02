def collect_input(file_input):
    with open(file_input, "rt") as f:
        return list(int(line) for line in f.readlines())


def calculate_fuel(module_input):
    module_fuel = module_input / 3 - 2
    return int(module_fuel)


def calculate_fuel_sum(calculated_fuel_list):
    sum_of_fuel = 0
    for value in calculated_fuel_list:
        sum_of_fuel = sum_of_fuel + value
    return sum_of_fuel


def calculate_additional_fuel_mass(fuel_input):
    additional_fuel_mass = []

    current_fuel_needed = fuel_input / 3 - 2
    additional_fuel_mass.append(int(current_fuel_needed))
    while current_fuel_needed > 0:
        current_fuel_needed = current_fuel_needed / 3 - 2
        if not current_fuel_needed <= 0:
            additional_fuel_mass.append(int(current_fuel_needed))

    return sum(additional_fuel_mass)


def day_1_solve_answer(input_file_path):
    list_of_modules = collect_input(input_file_path)
    list_of_fuel_values = []

    for module in list_of_modules:
        list_of_fuel_values.append(calculate_fuel(int(module)))
    total_fuel = calculate_fuel_sum(list_of_fuel_values)
    return total_fuel


def day_1_pt2_solve_answer(input_file_path):
    list_of_modules = collect_input(input_file_path)

    list_of_fuel_values = []

    for module in list_of_modules:
        mass_with_fuel = calculate_additional_fuel_mass(int(module))
        list_of_fuel_values.append(mass_with_fuel)
    total_fuel = sum(list_of_fuel_values)
    return total_fuel
