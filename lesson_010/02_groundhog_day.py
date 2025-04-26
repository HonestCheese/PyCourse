# -*- coding: utf-8 -*-
from random import randint
from termcolor import cprint

ENLIGHTENMENT_CARMA_LEVEL = 777


class IamGodError(Exception):
    def __init__(self):
        self.message = 'I AM GOD YOU STUPID CREATURE'
        super().__init__(self.message)


class DrunkError(Exception):
    def __init__(self):
        self.message = 'ssry to drunk to do something'
        super().__init__(self.message)


class CarCrashError(Exception):
    def __init__(self):
        self.message = 'Damn looks like your car is broken'
        super().__init__(self.message)


class GluttonyError(Exception):
    def __init__(self):
        self.message = 'I think you cant eat anymore'
        super().__init__(self.message)


class DepressionError(Exception):
    def __init__(self):
        self.message = 'Died of cringe'
        super().__init__(self.message)


class SuicideError(Exception):
    def __init__(self):
        self.message = 'WTF BRO'
        super().__init__(self.message)


class DeleteError(Exception):
    def __init__(self):
        self.message = "I DONT WANT TO SEE YOU HERE ANYMORE"
        super().__init__(self.message)


# День сурка
def oneday():
    try:
        if randint(1,13) == 13:
            dice = randint(1,6)
            if dice == 1:
                raise IamGodError
            elif dice == 2:
                raise DrunkError
            elif dice == 3:
                raise CarCrashError
            elif dice == 4:
                raise GluttonyError
            elif dice == 5:
                raise DepressionError
            else:
                raise SuicideError
        return randint(1, 7)
    except IamGodError:
        cprint('oh looks like you think that you are a god?', color = 'light_red')
        cprint("BE MORE CAREFULL NEXT TIME", color = 'red')
        return -100
    except DrunkError:
        cprint('Bad boy', color= 'light_red')
        return -30
    except GluttonyError:
        cprint('who likes thoose who eat too much?', color = 'light_red')
        return -30
    except CarCrashError:
        cprint('damn bro thats hard(', color = 'light_red')
        return -20
    except DepressionError:
        cprint('bro i believe in you', color = 'cyan')
        return -30
    except SuicideError:
        cprint('i dont think that you deserve your existance', color = 'red')
        return -100

carma = 30
while True:
    carma += oneday()
    if carma >= ENLIGHTENMENT_CARMA_LEVEL:
        cprint('hell nah buddha??', color = 'light_yellow')
        break
    elif carma < 0:
        cprint("this place is not for you anymore", color = 'red')
        cprint("hell nah bro. cya", color = 'red')
        break
    print('carma = ', carma)


# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.


# https://goo.gl/JnsDqu
