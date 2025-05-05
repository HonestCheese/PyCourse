# -*- coding: utf-8 -*-
import re

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
path = 'events.txt'


def ppp(path):
    with open(path, 'r') as file:
        count = 0
        parts = file.readline().strip().split(' ')
        start_time = parts[0] + ' ' + parts[1][:5]
        if parts[2] == 'NOK':
            count += 1
        while True:
            try:
                parts = file.readline().strip().split(' ')
                currtime = parts[0] + ' ' + parts[1][:5]
                if currtime == start_time and parts[2] == 'NOK':
                    count += 1
                elif currtime != start_time:
                    yield start_time[1:], count
                    start_time = currtime
                    count = 0
                    if parts[2] == 'NOK':
                        count +=1
            except IndexError:
                yield start_time[1:], count
                print("EOF")
                return 0

grouped_events = ppp(path)
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

# TODO здесь ваш код
