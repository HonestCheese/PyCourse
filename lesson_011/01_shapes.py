# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.
def get_polygon(n):
    if n == 4:
        def draw_square(angle, point, length):
            flag = 0
            for _ in range(3):
                if flag == 0:
                    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
                    v1.draw()
                    angle += 90
                    flag += 1
                if flag > 0:
                    v1 = sd.get_vector(start_point=v1.end_point, angle=angle, length=length, width=3)
                    v1.draw()
                    angle += 90

        return draw_square
    if n == 5:
        def pentagon(length, point, angle):
            v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
            v1.draw()
            v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=length, width=3)
            v2.draw()
            v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 144, length=length, width=3)
            v3.draw()
            v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 216, length=length, width=3)
            v4.draw()
            v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 288, length=length, width=3)
            v5.draw()

        return pentagon

    if n == 3:
        def triangle(angle, point, length):
            v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
            v1.draw()
            v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=3)
            v2.draw()
            v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length, width=3)
            v3.draw()
        return triangle
    else: raise Exception('nah im lazy')


draw_triangle = get_polygon(n=3)
draw_square = get_polygon(n=4)
draw_pentagon = get_polygon(n=5)
print(type(draw_triangle))
draw_triangle(point=sd.get_point(200, 200), angle=13, length=100)
draw_pentagon(point=sd.get_point(300, 200), angle=13, length=100)
draw_square(point=sd.get_point(200, 300), angle=13, length=100)

sd.pause()
