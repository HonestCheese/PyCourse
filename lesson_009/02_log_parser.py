# -*- coding: utf-8 -*-
import re
class LogParser:
    def __init__(self, input):
        self.lib = dict()
        with open(f'{input}', 'r') as events:
            for line in events:
                parts = re.split(r"[ \[\].:\n]+", line)
                if parts[6] == 'NOK':
                    if (parts[1] + ' ' + parts[2] + ':' + parts[3]) not in self.lib:
                        self.lib[parts[1] + ' ' + parts[2] + ':' + parts[3]] = 0
                    if (parts[1] + ' ' + parts[2] + ':' + parts[3]) in self.lib:
                        self.lib[parts[1] + ' ' + parts[2] + ':' + parts[3]] += int(parts[5])


    def write_to(self, output):
        with open(f'{output}', 'w') as file:
            for elem in self.lib:
                line = f"{elem} NOK - {self.lib[elem]}\n"
                file.write(line)

    def sortby(self, mode):
        if mode == 'year':
            self.lib = dict(sorted(self.lib.items(), key = lambda x: re.split(r'[- :]', x[0])[0]))
        if mode == 'month':
            self.lib = dict(sorted(self.lib.items(), key = lambda x: re.split(r'[- :]', x[0])[1]))
        if mode == 'day':
            self.lib = dict(sorted(self.lib.items(), key = lambda x: re.split(r'[- :]', x[0])[2]))
        if mode == 'hour':
            self.lib = dict(sorted(self.lib.items(), key = lambda x: re.split(r'[- :]', x[0])[3]))
        if mode == 'minute':
            self.lib = dict(sorted(self.lib.items(), key = lambda x: re.split(r'[- :]', x[0])[1]))






aboba = LogParser('events.txt')
aboba.sortby('year')
aboba.write_to('output.txt')
