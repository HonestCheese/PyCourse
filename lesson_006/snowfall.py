import simple_draw as sd

BACKGROUND = ''
snowflakes_size = []
startpoint_x = []
startpoint_y = []
sd.set_screen_size(1200, 600)




def create_snowflakes(n):
    global snowflakes_size, startpoint_x, startpoint_y
    snowflakes_size = [sd.random_number(10, 50) for _ in range(n)]
    startpoint_x = [sd.random_number(-200, 1200) for _ in range(n)]
    startpoint_y = [800 for _ in range(n)]


def draw_snowflakes(n, color):
    sd.start_drawing()
    for i in range(n):
        sd.snowflake(center=sd.Point(startpoint_x[i], startpoint_y[i]), length=snowflakes_size[i], color = color)
    for i in range(n, len(snowflakes_size)):
        sd.snowflake(center=sd.Point(startpoint_x[i], startpoint_y[i]), length=snowflakes_size[i], color = color)
    sd.finish_drawing()
    sd.sleep(0.01)
    sd.draw_background()

num_to_rem = []
def snowflakes_move(n):
    for i in range(n):
        startpoint_x[i] += (2 + snowflakes_size[i] / 6)
        startpoint_y[i] -= (2 + snowflakes_size[i] / 9)
        if len(snowflakes_size)>40:
            for i in range(len(snowflakes_size)-40):
                snowflakes_size[i+n]-=0.3
                if snowflakes_size[i+n]<3:
                    snowflakes_size.pop(i+n)
                    startpoint_x.pop(i+n)
                    startpoint_y.pop(i+n)
        if startpoint_y[i] < 10:
            startpoint_x.append(startpoint_x[i])
            startpoint_y.append(startpoint_y[i])
            snowflakes_size.append(snowflakes_size[i])
        if startpoint_y[i] < 10:
            snowflakes_size[i] = sd.random_number(10, 50)
            startpoint_y[i] = 700
        if startpoint_x[i] > 1300:
            snowflakes_size[i] = sd.random_number(10, 50)
            startpoint_x[i] = -60
def snowfall_2(n):
    create_snowflakes(n)
    sd.take_background()
    while True:
        draw_snowflakes(n, color = sd.COLOR_WHITE)
        snowflakes_move(n)
snowfall_2(20)