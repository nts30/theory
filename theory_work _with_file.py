"""Работа с файлами

r - только для чтение
r+ - для записи и чтения
w - только для записи (Создаст новый файл, если файл с таким именем не найден)
w+ -  для чтения и записи (Создаст новый файл, если файл с таким именем не найден)
rb - чтение бинарного файла
wb - только для записи в .bin файл
a - откроет файл для добавления новой информации (Создаст новый файл, если файл с таким именем не найден)

"""
import os.path

import pysnooper


@pysnooper.snoop()
def writer(name: str, param: str):
    if not os.path.exists('files'):
        os.mkdir('files')

    with open(r'files/some_file.txt', f'{param}', encoding='utf-8') as file:
        file.write(f'Привет меня зовут {name.title()}\n')


def reader():
    with open(r'files/some_file.txt', 'r', encoding='utf-8') as file:
        #text = file.read()
        text = file.readlines()
        print(text)


writer('Aleksey', 'a')

reader()
