# -*- coding: utf-8 -*-

import simple_draw as sd
import lesson_006.snowfall as s

def create2(n ,color):
    s.create_snowflakes()
    while True:
        s.draw_snowflakes(n, color)
        s.snowflakes_move(n)
create2(20, sd.COLOR_WHITE)
