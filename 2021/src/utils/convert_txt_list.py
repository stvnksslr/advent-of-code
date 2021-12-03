def convert_txt_to_list(input_file):
    list_of_lists = []

    for line in input_file:
        stripped_line = line.strip()
        list_of_lists.append(int(stripped_line))
    return list_of_lists
