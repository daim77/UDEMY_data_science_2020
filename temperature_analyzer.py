# avarage temperature from citytemp.csv
import csv
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
            temp_list = [convert_f_c(int(temp)) for temp in data_dict[city]['F']]
            for num in [int(temp) for temp in data_dict[city]['C']]:
                temp_list.append(num)
        elif 'F' in data_dict[city]:
            temp_list = [convert_f_c(int(temp)) for temp in data_dict[city]['F']]
        else:
            temp_list = [int(temp) for temp in data_dict[city]['C']]

        result_dict.update(
            {city: [
                round(statistics.mean(temp_list), 1),
                round(statistics.median(temp_list), 1)
            ]})
    return result_dict


def convert_f_c(temp):
    temp = (temp - 32) * 5/9
    return temp


def output(result_dict):
    print('\nAll temperatures in Ceslisu\n' + '=' * 94)
    print('|{:^30}|{:^30}|{:^30}|'.format('City name', 'Average temp', 'Median temp'))
    print('=' * 94)
    for city in result_dict:
        print('|{:^30}|{:^30}|{:^30}|'.format(city, result_dict[city][0], result_dict[city][1]))
    print('=' * 94)


def main():
    data_list = data_from_csv()
    data_dict = build_dict(data_list)
    result_dict = stat_oper(data_dict)
    output(result_dict)


main()
