# -*- coding: utf-8 -*-
from os import write


# Написать декоратор, который будет логировать (записывать в лог файл)
# ошибки из декорируемой функции и выбрасывать их дальше.
#
# Имя файла лога - function_errors.log
# Формат лога: <имя функции> <параметры вызова> <тип ошибки> <текст ошибки>
# Лог файл открывать каждый раз при ошибке в режиме 'a'
def dec_w(name):
    def log_errors(func):
        def okie(param):
            try:
                func(param)
                with open(name, 'a') as file:
                    file.write(line + '\n')
            except (ValueError, ZeroDivisionError) as arg:
                print(f'Error: {arg} - {param}')
        return okie
    return log_errors


# Проверить работу на следующих функциях
@dec_w(None)
def perky(param):
    return param / 0


@dec_w(name = 'function_errors.log')
def check_line(line):
    name, email, age = line.split(' ')
    if not name.isalpha():
        raise ValueError("it's not a name")
    if '@' not in email or '.' not in email:
        raise ValueError("it's not a email")
    if not 10 <= int(age) <= 99:
        raise ValueError('Age not in 10..99 range')


lines = [
    'Ярослав bxh@ya.ru 600',
    'Земфира tslzp@mail.ru 52',
    'Тролль nsocnzas.mail.ru 82',
    'Джигурда wqxq@gmail.com 29',
    'Земфира 86',
    'Равшан wmsuuzsxi@mail.ru 35',
]
for line in lines:
    check_line(line)
perky(param=42)


# Усложненное задание (делать по желанию).
# Написать декоратор с параметром - именем файла
#
# @log_errors('function_errors.log')
# def func():
#     pass

