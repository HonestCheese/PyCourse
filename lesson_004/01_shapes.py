# -*- coding: utf-8 -*-
from operator import length_hint

import simple_draw as sd
from simple_draw import COLOR_ORANGE, COLOR_GREEN, COLOR_CYAN, COLOR_PURPLE
sd.set_screen_size(1200, 600)

def square(angle, point, color):
    x, y = point
    flag = 0
    for _ in range(3):
        if flag == 0:
            v1 = sd.get_vector(start_point=sd.Point(x, y), angle=angle, length=100, width=3)
            v1.draw(color)
            angle += 90
            flag += 1
        if flag > 0:
            v1 = sd.get_vector(start_point=v1.end_point, angle=angle, length=100, width=3)
            v1.draw(color)
            angle += 90


square(point=(300, 300), angle=0, color=COLOR_ORANGE)


def triangle(angle, point, color):
    x, y = point
    v1 = sd.get_vector(start_point=sd.Point(x, y), angle=angle, length=100, width=3)
    v1.draw(color)
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle+120, length=100, width=3)
    v2.draw(color)
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle+240, length=100, width=3)
    v3.draw(color)

triangle(0, (500,300), COLOR_GREEN)

def pentagon(color, point, angle):
    x, y = point
    v1 = sd.get_vector(start_point=sd.Point(x, y), angle=angle, length=100, width=3)
    v1.draw(color)
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=100, width=3)
    v2.draw(color)
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 144, length=100, width=3)
    v3.draw(color)
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 216, length=100, width=3)
    v4.draw(color)
    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 288, length=100, width=3)
    v5.draw(color)

pentagon(color = COLOR_CYAN, point = (700,300), angle = 0)

def hexagon(angle, point, color):
    x, y = point
    flag = 0
    for _ in range(6):
        if flag == 0:
            v1 = sd.get_vector(start_point=sd.Point(x, y), angle=angle, length=100, width=3)
            v1.draw(color)
            angle += 60
            flag += 1
        if flag > 0:
            v1 = sd.get_vector(start_point=v1.end_point, angle=angle, length=100, width=3)
            v1.draw(color)
            angle += 60
hexagon(point= (900,300), color = COLOR_PURPLE, angle = 0)
# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
##
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg



# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!
def any_figure(angle, point, storon):
    x, y = point
    flag = 0
    angle_1=(180*(storon-2))/storon
    for i in range(storon):
        if flag == 0:
            v1 = sd.get_vector(start_point=sd.Point(x, y), angle=angle, length=100, width=3)
            v1.draw()
            flag += 1
        elif flag > 0:
            if i == storon - 1:
                sd.line(start_point = v1.end_point, end_point=sd.Point(x,y), width=3)
                break
            v1 = sd.get_vector(start_point=v1.end_point, angle=angle+(180-angle_1)*i, length=100, width=3)
            v1.draw()

any_figure(point= (600,100), storon = 3, angle = 0)

sd.pause()
