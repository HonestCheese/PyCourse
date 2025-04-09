# -*- coding: utf-8 -*-

import simple_draw as sd
from simple_draw import finish_drawing

sd.set_screen_size(1200,600)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные
n = 10

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()
snowflakes = [sd.random_number(10,50) for _ in range(n)]
# snowflakes = [sd.random_number(10,50) for _ in range(n)]
startpoint_x = [sd.random_number(-200,1200) for _ in range(n)]
startpoint_y =[800 for _ in range(n)]
color = [sd.random_color() for _ in range(n)]

y=600
while True:
    sd.clear_screen()
    sd.start_drawing()
    for i in range(n):
        sd.snowflake(center = sd.Point(startpoint_x[i], startpoint_y[i]), length=snowflakes[i], color=color[i])
        startpoint_x[i] += (10+snowflakes[i]/2)
        startpoint_y[i] -= (10+snowflakes[i]/3)
        if startpoint_y[i] < -100:
            snowflakes[i] = sd.random_number(10,50)
            startpoint_y[i] = 700
        if startpoint_x[i] > 1300:
            snowflakes[i] = sd.random_number(10,50)
            startpoint_x[i] = -100
    finish_drawing()
    sd.sleep(0.1)
sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


