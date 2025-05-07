# -*- coding: utf-8 -*-
from multiprocessing import Process, Queue
import os
import threading
import time
from collections import defaultdict
from os.path import abspath
from pprint import pprint


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПРОЦЕССНОМ стиле
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
class processes(Process):
    def __init__(self, files, num, q, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.q = q
        self.files = files
        self.num = num
        self.vol = defaultdict(list)

    def run(self):
        for file in files[self.num:self.num+28]:
            file = os.path.join(abspath('trades'), file)
            with open(file, 'r') as file:
                file.readline()
                for line in file:
                    name, time, price_str, quantity = line.split(',')
                    price = float(price_str)
                    if not self.vol[name]:
                        self.vol[name] = [price, price]
                    else:
                        if self.vol[name][0] > price:
                            self.vol[name][0] = price
                        if self.vol[name][1] < price:
                            self.vol[name][1] = price
        vol_f = defaultdict()
        for x, y in self.vol.items():
            sred = (float(y[1]) + float(y[0])) / 2
            vol_f[x] = round(((float(y[1]) - float(y[0])) / sred) * 100)
        self.q.put(vol_f)


#
#
# class Volatility(Thread):
#     def __init__(self, file, vol, lock, *args, **kwargs):
#         super(Volatility, self).__init__(*args, **kwargs)
#         self.lock = lock
#         self.file = os.path.abspath(os.path.join('trades', file))
#         self.vol = vol
#         self.result = []
#
#     def run(self):
#         with open(self.file, 'r') as file:
#             file.readline()
#             for line in file:
#                 name, time, price_str, quantity = line.split(',')
#                 price = float(price_str)
#                 if not (self.result):
#                     self.result.append(price)
#                     self.result.append(price)
#                 else:
#                     if self.result[0] > price:
#                         self.result[0] = price
#                     if self.result[1] < price:
#                         self.result[1] = price
#         with self.lock:
#             self.vol[name] = self.result
#
#
# vol_1 = defaultdict()
# files = []
# for _, _, fn in os.walk(os.path.abspath('trades')):
#     files = fn
# locker = threading.Lock()
# threads = [Volatility(file, vol_1, lock=locker) for file in files]
# start = time.time()
# for thread in threads:
#     thread.start()
# for thread in threads:
#     thread.join()
# end = time.time()
# for x, y in vol_1.items():
#     sred = (float(y[1]) + float(y[0])) / 2
#     vol_1[x] = round(((float(y[1]) - float(y[0])) / sred) * 100)
# s = list(sorted(vol_1, key=lambda x: vol_1[x], reverse=True))
# print("Максимальаня витальность")
# print(s[0], '-', vol_1[s[0]])
# print(s[1], '-', vol_1[s[1]])
# print(s[2], '-', vol_1[s[2]])
# print("Минимальная витальность")
# for elem in range(len(s)):
#     min_elem = vol_1[s[elem]]
#     if min_elem == 0:
#         print(s[elem - 1], '-', vol_1[s[elem - 1]])
#         print(s[elem - 2], '-', vol_1[s[elem - 2]])
#         print(s[elem - 3], '-', vol_1[s[elem - 3]])
#         break
# print('Нулевая витальность')
# zero_v = []
# for elem in range(len(s)):
#     if vol_1[s[elem]] == 0:
#         zero_v.append(s[elem])
# print(' '.join(map(str, sorted(zero_v))))
# print(end - start)
#
# # =========================================

files = []
q = Queue(maxsize=5)
for _, _, fn in os.walk('trades'):
    files = fn
proc = [processes(files, numb, q) for numb in range(0, len(files), 28)]
start = time.time()
for process in proc:
    process.start()
for process in proc:
    process.join()
vol_final = defaultdict()
while True:
    try:
        vol_final.update(q.get(timeout=0.1))
    except:
        break
s = list(sorted(vol_final, key=lambda x: vol_final[x], reverse=True))
print("Максимальаня витальность")
print(s[0], '-', vol_final[s[0]])
print(s[1], '-', vol_final[s[1]])
print(s[2], '-', vol_final[s[2]])
print("Минимальная витальность")
for elem in range(len(s)):
    min_elem = vol_final[s[elem]]
    if min_elem == 0:
        print(s[elem - 1], '-', vol_final[s[elem - 1]])
        print(s[elem - 2], '-', vol_final[s[elem - 2]])
        print(s[elem - 3], '-', vol_final[s[elem - 3]])
        break
print('Нулевая витальность')
zero_v = []
for elem in range(len(s)):
    if vol_final[s[elem]] == 0:
        zero_v.append(s[elem])
end = time.time()
print(' '.join(map(str, sorted(zero_v))))
print(end -  start)