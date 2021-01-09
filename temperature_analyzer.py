# avarage temperature from citytemp.csv
import csv
from pprint import pprint as pp
import statistics

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
        elif item.isdigit() and data_list[index + 1].startswith('C'):
            data_list[index + 1] = data_list[index + 1][1:]
            data_list.insert(index + 1, 'C')

        while index % 3 == 0 and index != 0:
            if data_list[index - 3] not in data_dict:
                data_dict.update({data_list[index - 3]: {data_list[index - 1]: [data_list[index - 2]]}})
            elif data_list[index - 1] not in data_dict[data_list[index - 3]]:
                data_dict[data_list[index - 3]].update({data_list[index - 1]: [data_list[index - 2]]})
            else:
                temp_list = data_dict[data_list[index - 3]][data_list[index - 1]]
                temp_list.append(data_list[index - 2])
            break
    return data_dict


def stat_oper(data_dict):
    # [°C] = ([°F] − 32) × 5⁄9
    # [°F] = [°C] × 9⁄5 + 32
    result_dict = {}
    city_list = [city for city in data_dict]
    for city in city_list:
        if len(data_dict[city]) > 1:
            temp_list = [convert_f_c(int(temp)) for temp in data_dict[city]['F']]\
                            .append([int(temp) for temp in data_dict[city]['C']])
            print(temp_list)
        elif 'F' in data_dict[city]:
            temp_list = [convert_f_c(int(temp)) for temp in data_dict[city]['F']]
        else:
            temp_list = [int(temp) for temp in data_dict[city]['C']]
        print(city, temp_list)
        # avg = statistics.mean(temp_list)
        # result_dict.update({city: avg})
    return result_dict


def convert_f_c(temp):
    temp = (temp - 32) * 5/9
    return temp


def main():
    data_list = data_from_csv()
    data_dict = build_dict(data_list)
    result_dict = stat_oper(data_dict)

    # print(data_list)
    # pp(data_dict)
    # pp(result_dict)


main()
