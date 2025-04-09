import simple_draw as sd

bulls_cows = {
    'bulls': 0,
    'cows': 0
}


def random_number():
    while True:
        x = sd.random_number(1000, 10000)
        if len(set(str(x))) == 4:
            return x


def check_number(random_n, inputted_n):
    for i in range(4):
        if str(random_n)[i] == str(inputted_n)[i]:
            bulls_cows['bulls'] += 1
        elif str(random_n)[i] in str(inputted_n):
            bulls_cows['cows'] += 1
    if bulls_cows['bulls'] == 4:
        return 0
