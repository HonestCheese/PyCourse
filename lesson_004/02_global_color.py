# -*- coding: utf-8 -*-
import simple_draw as sd
from simple_draw import COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

def any_figure(angle, point, storon, color):
    x, y = point
    flag = 0
    angle_1=(180*(storon-2))/storon
    for i in range(storon):
        if flag == 0:
            v1 = sd.get_vector(start_point=sd.Point(x, y), angle=angle, length=100, width=3)
            v1.draw(color = color)
            flag += 1
        elif flag > 0:
            if i == storon - 1:
                sd.line(start_point = v1.end_point, end_point=sd.Point(x,y), width=3, color=color)
                break
            v1 = sd.get_vector(start_point=v1.end_point, angle=angle+(180-angle_1)*i, length=100, width=3)
            v1.draw(color = color)
colors = {
    1: COLOR_RED,
    2: COLOR_ORANGE,
    3: COLOR_YELLOW,
    4: COLOR_GREEN,
    5: COLOR_CYAN,
    6: COLOR_BLUE,
    7: COLOR_PURPLE
}
print('так хуйлуша, сперва вводишь число сторон, затем номер нужного цвета, пон?')
while True:
    storona = int(input('Кол-во сторон >>> '))
    color = int(input('''Цвета:
    1: COLOR_RED 
    2: COLOR_ORANGE
    3: COLOR_YELLOW
    4: COLOR_GREEN
    5: COLOR_CYAN
    6: COLOR_BLUE
    7: COLOR_PURPLE
    Номер цвета >>> '''))
    if color == 0 or color > 7:
        print("Нет такого, заново")
    elif 1<=color<=7:
        any_figure(color = colors[color], point = (300,300), storon= storona, angle=0)
        break
sd.pause()

