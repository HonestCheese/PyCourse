# -*- coding: utf-8 -*-
import simple_draw as sd


rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)


def rainbow():
    """Тупо радуга по краю экрана"""
    x, y = 0,-800
    for color in rainbow_colors:
        sd.circle(center_position=sd.Point(x, y), color=color, width=6, radius=1600)
        x+=5
        y+=3
rainbow()


