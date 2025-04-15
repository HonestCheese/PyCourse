# -*- coding: utf-8 -*-

import simple_draw as sd


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    sd.set_screen_size(1200, 600)
    sd.take_background()

    def __init__(self):
        self.size = sd.random_number(10, 50)
        self.color = sd.COLOR_WHITE
        self.startpoint_x = sd.random_number(-200, 1200)
        self.startpoint_y = 800

    def move(self):
        sd.start_drawing()
        self.startpoint_x += (2 + self.size / 6)
        self.startpoint_y -= (2 + self.size / 9)

    def clear_previous_picture(self):
        sd.finish_drawing()
        sd.draw_background()

    def draw(self):
        sd.start_drawing()
        sd.snowflake(center=sd.Point(self.startpoint_x, self.startpoint_y), length=self.size, color=self.color)

    def can_fall(self):
        if self.startpoint_y > 0 and self.startpoint_x < 1200:
            return 1
        else: return 0

flake = Snowflake()


# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.03)
#     if sd.user_want_exit():
#         break

def get_flakes(count):
    flakes = []
    for _ in range(count):
        flake = Snowflake()
        flakes.append(flake)
    return flakes


def get_fallen_flakes(flakes):
    for flake in flakes:
        if flake.startpoint_x > 1300 or flake.startpoint_y < -50:
            fallen_flakes.append(flake)
            flakes.remove(flake)


def append_flakes(fallen_flakes, where_new_flakes):
    for flake in fallen_flakes:
        if flake.startpoint_x  > 1300:
            flake.startpoint_x = -100
        if flake.startpoint_y < -50:
            flake.startpoint_y = 800
        flake.size = sd.random_number(10,50)
        where_new_flakes.append(flake)
        fallen_flakes.remove(flake)

flakes = get_flakes(count=20)  # создать список снежинок
fallen_flakes = []
while True:
    if fallen_flakes:
        append_flakes(fallen_flakes, flakes)
    for flake in flakes:
        flake.move()
        flake.draw()
    flake.clear_previous_picture()
    get_fallen_flakes(flakes)  # подчитать сколько снежинок уже упало
    if sd.user_want_exit():
        break
