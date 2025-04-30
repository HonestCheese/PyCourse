def log_errors(func):
    def okie(param):
        try:
            func(param)  # Выполняем функцию
            return True  # Возвращаем True при успехе
        except (ZeroDivisionError, ValueError) as arg:
            print(f"Ошибка: {arg}")  # Печатаем ошибку
            return False  # Возвращаем False при ошибке
    return okie

@log_errors
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
    if check_line(line):  # Если проверка прошла успешно (True)
        with open('function_errors.log', 'a+') as file:
            file.write(line + '\n')  # Записываем строку в файл
    else:
        print(f"Строка не прошла проверку: {line}")  # Выводим информацию об ошибке