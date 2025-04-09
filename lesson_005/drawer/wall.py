# -*- coding: utf-8 -*-
import simple_draw as sd


sd.resolution = (1200, 600)


def wall(x_start, x_end, y_start, y_end, color):
    """
    стена. так вот.
    :param x_start:
    :param x_end:
    :param y_start:
    :param y_end:
    :param color:
    :return:
    """
    sd.resolution = (1200, 600)
    for x in range(x_start, x_end, 50):
        c = 0
        for y in range(y_start, y_end, 25):
            c += 1
            if c % 2 == 0:
                sd.line(sd.Point(x, y), sd.Point(x, y + 25), color=color)
            if c % 2 == 1:
                sd.line(sd.Point(x + 25, y), sd.Point(x + 25, y + 25), color=color)
    for i in range(y_start, y_end, 25):
        sd.line(sd.Point(x_start, i), sd.Point(x_end, i), color=color)
    sd.line(sd.Point(x_start, y_start), sd.Point(x_start, y_end), color=color)
    sd.line(sd.Point(x_start, y_start), sd.Point(x_end, y_start), color=color)
    sd.line(sd.Point(x_start, y_end), sd.Point(x_end, y_end), color=color)
    sd.line(sd.Point(x_end, y_start), sd.Point(x_end, y_end), color=color)
