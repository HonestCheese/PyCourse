# -*- coding: utf-8 -*-
import pygame as pg
# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.
from drawer.wall import wall
from drawer.rainbow import rainbow
import simple_draw as sd
from simple_draw import COLOR_DARK_GREEN, snowflake
from drawer.fractal import draw_branches
from drawer.smile import smile
from drawer.snowfall import sniwi, snowfall_and_sun

rainbow()
def background():
    sd.rectangle(sd.Point(0, 0), sd.Point(1200, 200), color=COLOR_DARK_GREEN)
    sd.rectangle(sd.Point(200, 200), sd.Point(700, 400), color=sd.COLOR_ORANGE)


def house():
    list = [sd.Point(150,400), sd.Point(750,400), sd.Point(450, 500)]
    wall(200, 700, 200, 400, color = sd.COLOR_DARK_ORANGE)
    sd.polygon(list, sd.COLOR_DARK_PURPLE, width = 60)
    sd.rectangle(sd.Point(299, 400), sd.Point(600, 480), color = sd.COLOR_DARK_PURPLE)
    sd.rectangle(sd.Point(250, 250), sd.Point(320, 350), color=sd.COLOR_DARK_RED)
    sniwi(60)
    smile(285, 300, sd.COLOR_GREEN)




# def sun():
#     sd.circle(sd.Point(200, 500), 30, sd.COLOR_YELLOW, width = 30)
#     for i in range(0,360, 30):
#         v = sd.get_vector(start_point = sd.Point(200, 500), angle = 0 + i, length = 50)
#         v.draw(color = sd.COLOR_YELLOW, width = 6)


background()
house()
rainbow()
# sun()
draw_branches(point=sd.Point(900,300), angle=30, lenght=100, start_angle= 90, color = sd.COLOR_DARK_ORANGE)

snowfall_and_sun(20)

sd.pause()
# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.
