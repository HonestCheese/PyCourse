# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


class Human:
    def __init__(self):
        self.home = None
        self.fullness = 30
        self.happiness = 100
        self.status = 'alive'


class House:

    def __init__(self):
        self.money = 100
        self.food = 0
        self.cat_food = 0
        # Another shit
        self.mud = 0
        self.ate = 0
        self.used_money = 0

    def __str__(self):
        return f"Деньги - {self.money},  еда - {self.food}, еда котов - {self.cat_food} грязь - {self.mud}"

    def used(self):
        print(f"Съедено - {self.ate}, потрачено - {self.used_money}")

    def act(self):
        self.mud += 10


class Husband(Human):

    def __init__(self, name, home):
        super().__init__()
        self.name = name
        self.home = home

    def __str__(self):
        return f"{self.name}, cчасьте - {self.happiness},  насыщенность - {self.fullness}" + (
            ', мертв' if self.status == 'dead' else '')

    def act(self):
        start = self.fullness
        if self.status == 'dead':
            cprint("Слегло", color='red')
            return 0
        if self.happiness < 10:
            cprint(f"{self.name} 1000-7", color='red')
            self.status = 'dead'
            return 0
        if self.fullness < 10:
            cprint(f"{self.name} не нашел нямку", color='red')
            self.status = 'dead'
            return 0
        if self.home.mud > 90:  # ТУТ УЖЕ БЫТОВУХА
            self.happiness -= 10
        if self.fullness < 30:
            if self.home.food >= 30:
                self.eat()
            elif self.home.money < 120:
                self.work()
        elif self.home.money < 120:
            self.work()
        elif self.happiness < 50:
            self.gaming()
        else:
            dice = randint(1, 3)
            if dice == 1 or 2:
                self.work()
            if dice == 2:
                if self.happiness < 100:
                    self.gaming()
        if self.fullness == start:
            self.fullness -= 10
            cprint(f'{self.name} ничего не делал', color='cyan')
            self.happiness -= 10

    def eat(self):
        self.home.food -= 30
        self.fullness += 30
        self.home.ate += 30
        cprint(f'{self.name} ест')

    def work(self):
        self.home.money += 150
        self.fullness -= 10
        cprint(f'{self.name} работает')

    def gaming(self):
        self.fullness -= 10
        self.happiness += 10
        cprint(f'{self.name} катает')


class Wife(Human):

    def __init__(self, name, home):
        super().__init__()
        self.name = name
        self.home = home

    def __str__(self):
        return f"{self.name}, cчасьте - {self.happiness},  насыщенность - {self.fullness} " + (
            ', мертв' if self.status == 'dead' else '')

    def act(self):
        start = self.fullness
        if self.status == 'dead':
            cprint("Слегло", color='red')
            return 0
        if self.happiness < 10:
            cprint(f"{self.name} 1000-7", color='red')
            self.status = 'dead'
            return 0
        if self.fullness < 10:
            cprint(f"{self.name} не нашел нямку", color='red')
            self.status = 'dead'
            return 0
        elif self.fullness < 30:  # FOOD
            if self.home.food < 30 and self.home.money >= 120:
                self.shopping()
            elif self.home.food >= 30:
                self.eat()
            else:
                pass
        elif self.home.food < 30 and self.home.money >= 120:
            self.shopping()
        elif self.happiness < 20:  # SHUBA
            if self.home.money < 350:
                pass
            else:
                self.buy_fur_coat()
        elif self.home.cat_food < 40 and self.home.money >= 40:
            self.cat_shopping()
        elif self.home.mud > 80:  # CLEAN
            self.clean_house()
        else:  # FREE_TO_DO
            if self.fullness < 60 and self.home.food >= 30:
                self.eat()
            else:
                pass
        if self.fullness == start:
            self.fullness -= 10
            self.happiness -= 10
            cprint(f'{self.name} ничего не делалa', color='purple')

    def eat(self):
        self.home.food -= 30
        self.fullness += 30
        self.home.ate += 30
        cprint(f"{self.name} поела")

    def shopping(self):
        self.home.money -= 120
        self.home.food += 120
        self.fullness -= 10
        self.home.used_money += 120
        cprint(f"{self.name} купила еду")

    def cat_shopping(self):
        self.home.money -= 80
        self.home.cat_food += 80
        print(f'{self.name} купила еду котам')

    def buy_fur_coat(self):
        self.home.money -= 350
        self.happiness += 60
        self.fullness -= 10
        self.home.used_money += 350
        cprint("жена  шуба)())))")

    def clean_house(self):
        self.fullness -= 10
        self.home.mud = 0
        cprint(f"{self.name} убираца")


class Cat:

    def __init__(self, name, home):
        self.name = name
        self.fullness = 40
        self.status = 'alive'
        self.home = home

    def __str__(self):
        if self.status == "alive":
            return f"{self.name}, насыщенность - {self.fullness} "
        else:
            return f"{self.name} умер"

    def act(self):
        if self.fullness <= 0:
            self.status = 'dead'
        if self.status == "dead":
            print(f'{self.name} откис')
            return 0
        if self.fullness < 20 and self.home.cat_food >= 10:
            self.eat()
        else:
            dice = randint(1, 2)
            if dice == 1:
                self.sleep()
            if dice == 2:
                self.soil()

    def eat(self):
        self.fullness += 20
        self.home.cat_food -= 10
        print(f'{self.name} поел, насыщенность - {self.fullness}')

    def sleep(self):
        self.fullness -= 10
        print(f'{self.name} спал ')

    def soil(self):
        self.home.mud += 10
        self.fullness -= 10
        print(f'{self.name} драл обои)')



class Child(Human):

    def __init__(self, name, home):
        super().__init__()
        self.name = name
        self.home = home

    def __str__(self):
        return f"{self.name}, cчасьте - {self.happiness},  насыщенность - {self.fullness} " + (
            ', мертв' if self.status == 'dead' else '')

    def act(self):
        if self.fullness <= 0:
            self.status = 'dead'
        if self.status == 'dead':
            print(f'{self.name} умер')
            return 0
        if self.fullness < 20 and self.home.food >= 10:
            self.eat()
        else:
            dice = randint(1, 2)
            if dice == 1:
                self.sleep()
            elif dice == 2 and self.fullness < 100 and self.home.food >= 10:
                self.eat()
            else:
                self.sleep()

    def eat(self):
        self.fullness += 10
        self.home.food -= 10
        print(f'{self.name} ел, насыщенность - {self.fullness}')

    def sleep(self):
        self.fullness -= 10
        print(f'{self.name} спал')


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.

#
home = House()
serge = Husband(name='Сережа', home=home)
masha = Wife(name='Маша', home=home)
kolya = Child(name='Коля', home=home)
cats = [
    Cat(name='Мурзик', home=home),
    Cat(name='Барсик', home=home),
    Cat(name='Лолик', home=home),
    Cat(name='Сима', home=home)
]

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    kolya.act()
    for cat in cats:
        cat.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    for cat in cats:
        cprint(cat, color='cyan')
    print(home)

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
