# -*- coding: utf-8 -*-

import simple_draw as sd


def draw_branches(point, angle, lenght, start_angle, color):
    """
    Рисует дерево. прикольное дерево. Отсчет с точки где начинаются разветвляться ветви
    :param point:
    :param angle:
    :param lenght:
    :param start_angle:
    :param color:
    :return:
    """
    sd.start_drawing()
    if lenght == 100:
        sd.get_vector(start_point = point, angle = -90, length=200).draw(sd.COLOR_DARK_ORANGE, width = 3)

    if lenght < 25:
        v1 = sd.get_vector(start_point=point, angle=start_angle + angle, length=lenght)
        v1.draw(color = sd.COLOR_GREEN, width=1)
        v2 = sd.get_vector(start_point=point, angle=start_angle - angle, length=lenght)
        v2.draw(color = sd.COLOR_GREEN, width=1)
    if lenght<10:
        sd.finish_drawing()
        return 0
    if lenght >25:
        v1 = sd.get_vector(start_point=point, angle=start_angle + angle, length=lenght)
        v1.draw(color, width = 3)
        v2 = sd.get_vector(start_point=point, angle=start_angle - angle, length=lenght)
        v2.draw(color, width = 3)
    return draw_branches(point = v1.end_point, angle = angle, lenght = lenght*0.75, start_angle= start_angle + angle, color = color), draw_branches(v2.end_point, angle = angle, lenght = lenght*0.75, start_angle = start_angle - angle, color = color)


