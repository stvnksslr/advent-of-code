from pathlib import Path
from src.utils.convert_txt_list import convert_txt_to_list_int

input_file_path = Path.cwd() / "src" / "day1" / "puzzle_input.txt.txt"

if __name__ == '__main__':
    """
    This returns the text input as a python list
    """
    with open(input_file_path, mode='r') as file:
        input_list = convert_txt_to_list_int(file)
        print(input_list)
