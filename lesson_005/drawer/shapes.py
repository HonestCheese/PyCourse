# -*- coding: utf-8 -*-
import simple_draw as sd
import pygame as p


sd.set_screen_size(1200, 600)


def point_triangle(x1,y1,x2,y2,x3,y3):
    sd.line(sd.Point(x1, y1), sd.Point(x2, y2))
    sd.line(sd.Point(x1,y1), sd.Point(x3, y3))
    sd.line(sd.Point(x2,y2), sd.Point(x3, y3))



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




def triangle(angle, point, color):
    x, y = point
    v1 = sd.get_vector(start_point=sd.Point(x, y), angle=angle, length=100, width=3)
    v1.draw(color)
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle+120, length=100, width=3)
    v2.draw(color)
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle+240, length=100, width=3)
    v3.draw(color)


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

