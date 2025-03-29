# -*- coding: utf-8 -*-

import simple_draw as sd
from random import randint
from simple_draw import COLOR_YELLOW

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
'''i=0
for _ in range(3):
    sd.circle(sd.Point(100,110),50+i, COLOR_YELLOW,1 )
    i+=5'''

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
'''def Bubble(pt, rad):
    x,y = pt
    sd.circle(sd.Point(x,y), radius=rad)

Bubble((100,300), 30 )'''

# Нарисовать 10 пузырьков в ряд
'''i=0
for _ in range(10):
    Bubble((100+i,100), 30)
    i+=60'''

# Нарисовать три ряда по 10 пузырьков
'''for j in range(10):
    for k in range(3):
        Bubble((100+j*60, 100+k*60), 30)'''
# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(300):
    sd.circle(
        center_position=sd.Point(sd.random_number(0,1640), sd.random_number(0,1640)),
        radius=randint(20,100),
        color = sd.random_color()
    )
sd.pause()
