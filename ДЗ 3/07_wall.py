# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

sd.resolution = (1200, 600)
# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
for x in range(0,1200,100):
    c = 0
    for y in range(0,1200,50):
        c+=1
        if c % 2 == 0:
            sd.line(sd.Point(x,y), sd.Point(x,y+50))
        if c % 2 == 1:
            sd.line(sd.Point(x+50,y), sd.Point(x+50,y+50))
for i in range(0,601,50):
    sd.line(sd.Point(0,i), sd.Point(1200, i))

sd.pause()
