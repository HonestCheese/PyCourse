# -*- coding: utf-8 -*-
#
import simple_draw as sd


# def tree(point, angle, lenght_br):
#     angle = 30
#     x,y = point
#     if lenght_br<10:
#         exit()
#     vec1 = sd.get_vector(start_point=sd.Point(x,y), angle = 90+angle/2, length=lenght_br)
#     vec1.draw()
#     vec2 = sd.get_vector(start_point=sd.Point(x, y), angle=90 - angle/2, length=lenght_br)
#     vec2.draw()
#     vec1_1 = sd.get_vector(start_point=vec1.end_point, angle = 90+angle/2, length=lenght_br*0.75)
#     vec1_2 = sd.get_vector(start_point=vec1.end_point, angle = 90-angle/2, length=lenght_br*0.75)
#     vec1_2.draw()
#     vec1_1.draw()
# tree(point = (300,10), angle = 0, lenght_br = 100)

def draw_branches(point, angle, lenght):
    if lenght < 10:
        return 0
    v1 = sd.get_vector(start_point=point, angle=90 + angle, length=lenght)
    v1.draw()
    v2 = sd.get_vector(start_point=point, angle=90 - angle, length=lenght)
    v2.draw()
    return draw_branches(point = v1.end_point, angle = angle*1.5, lenght = lenght*0.75), draw_branches(v2.end_point, angle*1.5, lenght*0.75)

draw_branches(point=sd.Point(300,10), angle=30, lenght=100)
# 2) делать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
#root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения


# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()
