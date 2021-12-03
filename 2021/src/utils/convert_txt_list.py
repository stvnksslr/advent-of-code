def convert_txt_to_list_int(input_file):
    list_of_lists = []

    for line in input_file:
        stripped_line = line.strip()
        list_of_lists.append(int(stripped_line))
    return list_of_lists


def convert_txt_to_list_string(input_file):
    list_of_lists = []

    for line in input_file:
        stripped_line = line.strip()
        list_of_lists.append(stripped_line)
    return list_of_lists


def convert_text_to_list_of_sets(input_file):
    txt_list = [line.strip().split(' ') for line in input_file]
    return txt_list
