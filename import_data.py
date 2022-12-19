import csv
import json
import os
os.chdir(os.path.dirname(__file__))

'''
Здесь мы считываем и сохраняем, в нашу базу, записи из файла, 
который указал пользователь
'''


def copy_cont():
    path = input('Введите имя файла, откуда хотите скопировать данные   ')

    def import_csv(path_to_import_csv_file):
        data = []
        with open(f'{path_to_import_csv_file}.csv', "r", newline='', encoding='utf-8') as file:

            file_reader = csv.reader(file, delimiter=";")
            for row in file_reader:
                data.append(row)
        return data
    d = import_csv(path)
    f = input(
        'Введите имя или фамилию человека, данные которого необходимо записать в записную книжку   ')
    arr = []
    for i in range(len(d)):
        if f in d[i]:
            arr.append(d[i])
    return arr


def copy_cont_json():
    path = input('Введите имя файла, откуда хотите скопировать данные:   ')

    def import_json(path_to_import_json_file):
        data = []
        with open(f'{path_to_import_json_file}.json', "r", encoding='utf-8') as file:
            file_reader = json.load(file)
            for i in range(0, len(file_reader)):
                g = list(file_reader[i])
                data.append(g)
        return data

    d = import_json(path)
    new = input(
        'Введите имя или фаммилию человека, данные которого хотите записать:  ')
    arr = []
    for i in range(len(d)):
        if new in d[i]:
            arr.append(d[i])

    for i in range(len(arr)):
        with open('phonebook.csv', "a", encoding='utf-8') as fil:
            csv_fil = csv.writer(fil, delimiter=';')
            csv_fil.writerow(arr[i])
    print('Данные успешно записаны')


def write_csv(data):
    for i in range(len(data)):
        with open('phonebook.csv', "a", encoding='utf-8') as fil:
            csv_fil = csv.writer(fil, delimiter=';')
            csv_fil.writerow(data[i])
            print('Данные успешно записаны')
