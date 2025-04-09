# -*- coding: utf-8 -*-

import simple_draw as sd
from simple_draw import finish_drawing

sd.set_screen_size(1200,600)


def snowfall(n):
    """
    Cнегопад из n снежинок (1200х600)
    :param n:
    :return:
    """
    snowflakes = [sd.random_number(10,50) for _ in range(n)]
    startpoint_x = [sd.random_number(-200,1200) for _ in range(n)]
    startpoint_y =[800 for _ in range(n)]
    y=600
    sd.take_background()
    while True:
        sd.start_drawing()
        for i in range(n):
            sd.snowflake(center = sd.Point(startpoint_x[i], startpoint_y[i]), length=snowflakes[i], color=sd.COLOR_WHITE)
            startpoint_x[i] += (10+snowflakes[i]/2)
            startpoint_y[i] -= (10+snowflakes[i]/3)
            if startpoint_y[i] < -100:
                snowflakes[i] = sd.random_number(10,50)
                startpoint_y[i] = 700
            if startpoint_x[i] > 1300:
                snowflakes[i] = sd.random_number(10,50)
                startpoint_x[i] = -100

        finish_drawing()
        sd.draw_background()
        sd.sleep(0.1)


def snowfall_and_sun(n):
    """
    Cнегопад из n снежинок (1200х600)
    :param n:
    :return:
    """
    snowflakes = [sd.random_number(10, 50) for _ in range(n)]
    startpoint_x = [sd.random_number(-200, 1200) for _ in range(n)]
    startpoint_y = [800 for _ in range(n)]
    y = 600
    angle = 0
    sd.circle(sd.Point(200, 500), 30, sd.COLOR_YELLOW, width=30)
    sd.take_background()
    while True:
        sd.start_drawing()
        for i in range(n):
            sd.snowflake(center=sd.Point(startpoint_x[i], startpoint_y[i]), length=snowflakes[i], color=sd.COLOR_WHITE)
            startpoint_x[i] += (10 + snowflakes[i] / 2)
            startpoint_y[i] -= (10 + snowflakes[i] / 3)
            if startpoint_y[i] < -100:
                snowflakes[i] = sd.random_number(10, 50)
                startpoint_y[i] = 700
            if startpoint_x[i] > 1300:
                snowflakes[i] = sd.random_number(10, 50)
                startpoint_x[i] = -100

        for i in range(0, 360, 30):
            v = sd.get_vector(start_point=sd.Point(200, 500), angle=angle + i, length=50)
            v.draw(color=sd.COLOR_YELLOW, width=6)
        angle+=3
        finish_drawing()
        sd.draw_background()
        sd.sleep(0.1)


def sniwi(pipipi):
    """
    сколько то снежинок в квадратике. Сугроб короче.
    :param pipipi:
    :return:
    """
    for _ in range(pipipi):
        sd.snowflake(sd.Point(sd.random_number(150, 250), sd.random_number(150,220)), length=sd.random_number(10,20), color = sd.COLOR_WHITE)




