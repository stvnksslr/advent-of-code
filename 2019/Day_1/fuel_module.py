def collect_input(file_input):
    with open(file_input) as fp:
        file_input_list = []
        line = fp.readline()
        while line:
            line = fp.readline()
            if not line == "":
                file_input_list.append(line)

    return file_input_list


def calculate_fuel(module_input):
    module_fuel = module_input / 3 - 2
    return int(module_fuel)


def calculate_fuel_sum(calculated_fuel_list):
    sum_of_fuel = 0
    for value in calculated_fuel_list:
        sum_of_fuel = sum_of_fuel + value
    return sum_of_fuel


def day_1_solve_answer(input_file_path):
    list_of_modules = collect_input(input_file_path)
    list_of_fuel_values = []

    for module in list_of_modules:
        cleaned_module_value = module.rstrip("\n")
        list_of_fuel_values.append(calculate_fuel(int(cleaned_module_value)))
    total_fuel = calculate_fuel_sum(list_of_fuel_values)
    return total_fuel
