# avarage temperature from citytemp.csv
import csv
from pprint import pprint as pp

math_dict = {}


def data_from_csv():
    data_string = ''
    with open('citytemp.csv', newline='', encoding='utf-8') as csvfile:
        citytemp_file = csv.reader(csvfile, delimiter='\t')
        for row in citytemp_file:
            data_string += ''.join(row)
        data_list = data_string.split(',')
    return data_list


def build_dict(data_list):
    data_dict = {}
    for index, item in enumerate(data_list):
        if item.isdigit() and data_list[index + 1].startswith('F'):
            data_list[index + 1] = data_list[index + 1][1:]
            data_list.insert(index + 1, 'F')
            data_dict = {data_list[index - 1]: {data_list[index + 1]: []}}
        elif item.isdigit() and data_list[index + 1].startswith('C'):
            data_list[index + 1] = data_list[index + 1][1:]
            data_list.insert(index + 1, 'C')
            data_dict = {data_list[index - 1]: {data_list[index + 1]: []}}

# if index % 3 == 0 and index != 0:
# data_dict[data_list[index - 3]].get(data_list[index - 1]).append(int(data_list[index - 2]))

    return data_dict


def math_oper(data_dict):

    return math_dict


def main():
    data_list = data_from_csv()
    data_dict = build_dict(data_list)

    print(data_list)
    pp(data_dict)
    pp(math_dict)


main()
