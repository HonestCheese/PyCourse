# -*- coding: utf-8 -*-
class Fire:
    def __init__(self):
        self.name = 'fire'

    def __add__(self, other):
        if other.name == 'water':
            new_obj = Steam()
            return new_obj.name
        if other.name == 'fire':
            new_obj = Fire()
            return new_obj.name
        if other.name == 'earth':
            new_obj = Lava()
            return new_obj.name
        if other.name == 'wind':
            new_obj = Lightning()
            return new_obj.name


class Water:
    def __init__(self):
        self.name = 'water'

    def __str__(self):
        return "sosat america"
    def __add__(self, other):
        if other.name == 'earth':
            new_obj = Mud()
        if other.name == 'water':
            new_obj = Water()
            return new_obj.name
        if other.name == 'fire':
            new_obj = Steam()
            return new_obj.name
        if other.name == 'wind':
            new_obj = Storm()
            return new_obj.name


class Earth:
    def __init__(self):
        self.name = 'earth'

    def __add__(self, other):
        if other.name == 'earth':
            new_obj = Earth()
        if other.name == 'water':
            new_obj = Mud()
            return new_obj.name
        if other.name == 'fire':
            new_obj = Lava()
            return new_obj.name
        if other.name == 'wind':
            new_obj = Dust()
            return new_obj.name

class Wind:
    def __init__(self):
        self.name = 'wind'

    def __add__(self, other):
        if other.name == 'earth':
            new_obj = Dust()
            return new_obj.name
        if other.name == 'water':
            new_obj = Storm()
            return new_obj.name
        if other.name == 'fire':
            new_obj = Lightning()
            return new_obj.name
        if other.name == 'wind':
            new_obj = Wind()
            return new_obj.name

class Storm:
    def __init__(self):
        self.name = 'steam'

    def __add__(self, other):
        pass


class Dust:
    def __init__(self):
        self.name = 'dust'

    def __add__(self, other):
        pass

class Lava:
    def __init__(self):
        self.name = 'lava'

    def __add__(self, other):
        pass


class Steam:
    def __init__(self):
        self.name = 'steam'

    def __add__(self, other):
        pass


class Mud:
    def __init__(self):
        self.name = 'mud'

    def add(self):
        pass


class Lightning:
    def __init__(self):
        self.name = 'lightning'

    def add(self):
        pass


# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())
water = Water()
fire = Fire()
earth = Earth()
wind = Wind()
# TODO здесь ваш код
print(Water())
print(water + fire)
print(water + fire)
print(earth + fire)
print(water + wind)
print(wind + fire)
print(wind + earth)
# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
