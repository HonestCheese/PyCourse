# -*- coding: utf-8 -*-

import os, time, shutil
from time import gmtime

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg

for path, dirs, files in os.walk('/home/kililpol/PycharmProjects/pycourse/lesson_009/icons/actions/system-run.png'):
    zipped = sorted(zip(files, [gmtime(os.path.getctime(os.path.join(path, file))) for file in files]),
                    key=lambda x: x[1][1])


class Sortik:
    def __init__(self, pathdir):
        self.pathdir = pathdir
        self.sorted_files = dict()

    def sort(self, mode):
        if os.path.isdir(self.pathdir):
            if mode == 'year':
                for path, dirs, files in os.walk(self.pathdir):
                    self.sorted_files = dict(sorted(
                        zip(files, [gmtime(os.path.getctime(os.path.join(path, file))) for file in files]),
                        key=lambda x: x[1][0]))
            if mode == 'month':
                for path, dirs, files in os.walk(self.pathdir):
                    self.sorted_files = dict(sorted(
                        zip(files, [gmtime(os.path.getctime(os.path.join(path, file))) for file in files]),
                        key=lambda x: x[1][1]))

            if mode == 'day':
                for path, dirs, files in os.walk(self.pathdir):
                    self.sorted_files = dict(sorted(
                        zip(files, [gmtime(os.path.getctime(os.path.join(path, file))) for file in files]),
                        key=lambda x: x[1][2]))
        else:
            print('Thats not a directory')

    def upload_to(self, output_dir):
        for elem in self.sorted_files:
            shutil.copy2(
                os.path.join(self.pathdir,str(elem)),
                output_dir
            )
popa = Sortik('/home/kililpol/PycharmProjects/pycourse/lesson_009/icons/actions')
popa.sort('year')
popa.upload_to('/home/kililpol/PycharmProjects/pycourse/lesson_009/test')
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
