import re
from collections import defaultdict
from pprint import pprint
from threading import Thread  # -*- coding: utf-8 -*-
import os
from time import time
from time import process_time_ns
import simple_draw as sd


# Описание предметной области:
#
# При торгах на бирже совершаются сделки - один купил, второй продал.
# Покупают и продают ценные бумаги (акции, облигации, фьючерсы, етс). Ценные бумаги - это по сути долговые расписки.
# Ценные бумаги выпускаются партиями, от десятка до несколько миллионов штук.
# Каждая такая партия (выпуск) имеет свой торговый код на бирже - тикер - https://goo.gl/MJQ5Lq
# Все бумаги из этой партии (выпуска) одинаковы в цене, поэтому говорят о цене одной бумаги.
# У разных выпусков бумаг - разные цены, которые могут отличаться в сотни и тысячи раз.
# Каждая биржевая сделка характеризуется:
#   тикер ценнной бумаги
#   время сделки
#   цена сделки
#   обьем сделки (сколько ценных бумаг было куплено)
#
# В ходе торгов цены сделок могут со временем расти и понижаться. Величина изменения цен называтея волатильностью.
# Например, если бумага №1 торговалась с ценами 11, 11, 12, 11, 12, 11, 11, 11 - то она мало волатильна.
# А если у бумаги №2 цены сделок были: 20, 15, 23, 56, 100, 50, 3, 10 - то такая бумага имеет большую волатильность.
# Волатильность можно считать разными способами, мы будем считать сильно упрощенным способом -
# отклонение в процентах от средней цены за торговую сессию:
#   средняя цена = (максимальная цена + минимальная цена) / 2
#   волатильность = ((максимальная цена - минимальная цена) / средняя цена) * 100%
# Например для бумаги №1:
#   average_price = (12 + 11) / 2 = 11.5
#   volatility = ((12 - 11) / average_price) * 100 = 8.7%
# Для бумаги №2:
#   average_price = (100 + 3) / 2 = 51.5
#   volatility = ((100 - 3) / average_price) * 100 = 188.34%
#
# В реальности волатильность рассчитывается так: https://goo.gl/VJNmmY
#
# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью.
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
# Подготовка исходных данных
# 1. Скачать файл https://drive.google.com/file/d/1l5sia-9c-t91iIPiGyBc1s9mQ8RgTNqb/view?usp=sharing
#       (обратите внимание на значок скачивания в правом верхнем углу,
#       см https://drive.google.com/file/d/1M6mW1jI2RdZhdSCEmlbFi5eoAXOR3u6G/view?usp=sharing)
# 2. Раззиповать средствами операционной системы содержимое архива
#       в папку python_base_source/lesson_012/trades
# 3. В каждом файле в папке trades содержится данные по сделакам по одному тикеру, разделенные запятыми.
#   Первая строка - название колонок:
#       SECID - тикер
#       TRADETIME - время сделки
#       PRICE - цена сделки
#       QUANTITY - количество бумаг в этой сделке
#   Все последующие строки в файле - данные о сделках
#
# Подсказка: нужно последовательно открывать каждый файл, вычитывать данные, высчитывать волатильность и запоминать.
# Вывод на консоль можно сделать только после обработки всех файлов.
#
# Для плавного перехода к мультипоточности, код оформить в обьектном стиле, используя следующий каркас


class volatility(Thread):
    def __init__(self, *args, **kwargs):
        super(volatility, self).__init__(*args, **kwargs)
        self.dict = defaultdict(list)
        self.dv = defaultdict(float)
    def run(self):
        for _, _, fn in os.walk(os.path.abspath('trades')):
            for file in fn:
                absfile = os.path.join('trades', file)
                with open(absfile, 'r') as file:
                    file.readline()
                    for line in file:
                        name, time, price_str, quantity = line.split(',')
                        price = float(price_str)
                        if not (self.dict[name]):
                            self.dict[name].append(price)
                            self.dict[name].append(price)
                        else:
                            if self.dict[name][0] > price:
                                self.dict[name][0] = price
                            if self.dict[name][1] < price:
                                self.dict[name][1] = price
        for x, y in self.dict.items():
            sred = (float(y[1]) + float(y[0])) / 2
            self.dv[x] = round(((float(y[1]) - float(y[0])) / sred) * 100)
        self.s = list(sorted(self.dv, key=lambda x: self.dv[x], reverse=True))
        print("Максимальаня витальность")
        print(self.s[0], '-', self.dv[self.s[0]])
        print(self.s[1], '-', self.dv[self.s[1]])
        print(self.s[2], '-', self.dv[self.s[2]])
        print("Минимальная витальность")
        for elem in range(len(self.s)):
            min_elem = self.dv[self.s[elem]]
            if min_elem == 0:
                print(self.s[elem - 1], '-', self.dv[self.s[elem - 1]])
                print(self.s[elem - 2], '-', self.dv[self.s[elem - 2]])
                print(self.s[elem - 3], '-', self.dv[self.s[elem - 3]])
                break
        print('Нулевая витальность')
        zero_v = []
        for elem in range(len(self.s)):
            if self.dv[self.s[elem]] == 0:
                zero_v.append(self.s[elem])
        print(' '.join(map(str,sorted(zero_v))))
        print(self.dv)

test = volatility()
start = time()
test.run()
end = time()
print(end-start)

