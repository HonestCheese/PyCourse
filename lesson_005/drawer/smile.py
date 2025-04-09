# -*- coding: utf-8 -*-


import simple_draw as sd


def smile(x, y, color):
    """
    Такой себе смайлик
    :param x:
    :param y:
    :param color:
    :return:
    """
    sd.circle(sd.Point(x,y), radius=30, width=2, color=color)
    sd.line(sd.Point(x,y), sd.Point(x+10, y-10),color=color)
    sd.line(sd.Point(x, y), sd.Point(x - 10, y-10),color=color)
    sd.line(sd.Point(x+10, y+5), sd.Point(x+10, y+20),color=color)
    sd.line(sd.Point(x - 10, y + 5), sd.Point(x - 10, y + 20),color=color)
# for _ in range(100):
#     smile(randint(0,600),randint(0,600), sd.random_color())
# sd.pause()
