# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd
from random import *
# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def smile(x, y, color):
    sd.circle(sd.Point(x,y), radius=30, width=2, color=color)
    sd.line(sd.Point(x,y), sd.Point(x+10, y-10),color=color)
    sd.line(sd.Point(x, y), sd.Point(x - 10, y-10),color=color)
    sd.line(sd.Point(x+10, y+5), sd.Point(x+10, y+20),color=color)
    sd.line(sd.Point(x - 10, y + 5), sd.Point(x - 10, y + 20),color=color)
for _ in range(100):
    smile(randint(0,600),randint(0,600), sd.random_color())
sd.pause()
