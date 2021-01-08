# avarage temperature from citytemp.csv
import csv

data_string = ''

with open('citytemp.csv', newline='', encoding='utf-8') as csvfile:
    citytemp_file = csv.reader(csvfile, delimiter='\t')
    for row in citytemp_file:
        data_string += ''.join(row)

    data_string = data_string.split(',')
    print(data_string)

    for index, item in enumerate(data_string):
        if item.isdigit() and data_string[index + 1].startswith('F'):
            data_string[index + 1] = data_string[index + 1][1:]
            data_string.insert(index + 1, 'F')
            status = 1
        elif item.isdigit() and data_string[index + 1].startswith('C'):
            data_string[index + 1] = data_string[index + 1][1:]
            data_string.insert(index + 1, 'C')
            status = 1

print(data_string)
