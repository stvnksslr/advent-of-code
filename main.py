import csv

print("Hello World")

with open("1st_challenge.csv") as csv_file:
    parse_reader = csv.reader(csv_file, delimiter=',')
    starting_frequency = 0
    for row in parse_reader:
        print(row[0])
        current_frequency = int(row[0])
        starting_frequency = current_frequency + starting_frequency
        print(starting_frequency)
