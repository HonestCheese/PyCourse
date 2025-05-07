# -*- coding: utf-8 -*-
import threading
from collections import defaultdict
from pprint import pprint
from threading import Thread
import os
import time
import queue

import simple_draw


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
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

class Volatility(Thread):
    def __init__(self, file, vol, lock, *args, **kwargs):
        super(Volatility, self).__init__(*args, **kwargs)
        self.lock = lock
        self.file = os.path.abspath(os.path.join('trades', file))
        self.vol = vol
        self.result = []

    def run(self):
        with open(self.file, 'r') as file:
            file.readline()
            for line in file:
                name, time, price_str, quantity = line.split(',')
                price = float(price_str)
                if not (self.result):
                    self.result.append(price)
                    self.result.append(price)
                else:
                    if self.result[0] > price:
                        self.result[0] = price
                    if self.result[1] < price:
                        self.result[1] = price
        with self.lock:
            self.vol[name] = self.result


vol_1 = defaultdict()
files = []
for _, _, fn in os.walk(os.path.abspath('trades')):
    files = fn
locker = threading.Lock()
threads = [Volatility(file, vol_1, lock=locker) for file in files]
start = time.time()
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
end = time.time()
pprint(vol_1)
for x, y in vol_1.items():
    sred = (float(y[1]) + float(y[0])) / 2
    vol_1[x] = round(((float(y[1]) - float(y[0])) / sred) * 100)
s = list(sorted(vol_1, key=lambda x: vol_1[x], reverse=True))
print("Максимальаня витальность")
print(s[0], '-', vol_1[s[0]])
print(s[1], '-', vol_1[s[1]])
print(s[2], '-', vol_1[s[2]])
print("Минимальная витальность")
for elem in range(len(s)):
    min_elem =vol_1[s[elem]]
    if min_elem == 0:
        print(s[elem - 1], '-', vol_1[s[elem - 1]])
        print(s[elem - 2], '-', vol_1[s[elem - 2]])
        print(s[elem - 3], '-', vol_1[s[elem - 3]])
        break
print('Нулевая витальность')
zero_v = []
for elem in range(len(s)):
    if vol_1[s[elem]] == 0:
        zero_v.append(s[elem])
print(' '.join(map(str, sorted(zero_v))))
print(end - start)
