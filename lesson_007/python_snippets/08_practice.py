from random import randint


class Man:
    def __init__(self, name, house):
        self.name = name
        self.hunger = 0
        self.house = house
        self.status = 'alive'

    def clean(self):
        self.house.cleanliness = 100
        self.hunger += 10

    def shop(self):
        if self.house.money >= 50:
            self.house.money -= 50
            self.house.food += 100
            print('{} купил еду. Еда = {}, деньги = {}'.format(self.name, self.house.food, self.house.money))
        else:
            print("не было денег. Пошел на работу")
            self.work("Пришлось")

    def shop_cat(self):
        self.house.money -= 30
        self.house.cat_food += 50
        print('{} купил еду гниде. Еда гниды = {}'.format(self.name, self.house.cat_food))

    def pickup_cat(self, cat):
        cat.house = self.house

    def work(self, text):
        self.house.money += 50
        self.hunger += 15
        print('Человек {} работал, {}. Денег = {}, голод = {}'.format(self.name, text, self.house.money, self.hunger))

    def eat(self):
        if self.house.food >= 20:
            self.house.food -= 20
            self.hunger -= 20
            print('{} поел. Голод = {}, еда = {}'.format(self.name, self.hunger, self.house.food))
        else:
            print('Еды не было. Пошел в магаз')
            self.shop()

    def watch_mtv(self):
        self.hunger += 10
        print('{} смотрел мультики. Голод = {}'.format(self.name, self.hunger))

    def sleep(self):
        self.hunger += 10

    def act(self):
        dice = randint(1, 2)
        if self.status == 'dead':
            print("он мертв")
        elif self.hunger >= 100:
            self.status = 'dead'
            print('{} УМЕР'.format(self.name, color='red'))
        elif self.hunger >= 80:
            self.eat()
        elif self.house.food <= 10:
            self.shop()
        elif self.house.cat_food <= 10:
            self.shop_cat()
        if self.hunger > 50:
            self.eat()
        elif self.house.cleanliness < 30:
            self.clean()
        elif dice == 1:
            self.work('Захотел')
        elif dice == 2:
            self.eat()


class House:
    def __init__(self):
        self.money = 0
        self.cleanliness = 90
        self.cat_food = 50
        self.food = 50


class Cat:
    def __init__(self, name):
        self.name = name
        self.house = None
        self.hunger = 0
        self.status = 'alive'

    def sleep(self):
        self.hunger += 10

    def eat(self):
        if self.house.cat_food >= 10:
            self.hunger -= 20
            self.house.cat_food -= 10
            print('Кот {} поел. Голод = {}, еда кота = {}'.format(self.name, self.hunger, self.house.cat_food))
        else:
            print(f"Котик плачет, голод = {self.hunger}")

    def FUN(self):
        self.house.cleanliness -= 10
        self.hunger += 10
        print('Кот {} веселится. Порядок = {}, голод = {}'.format(self.name, self.house.cleanliness, self.hunger))

    def act(self):
        dice = randint(1, 3)
        if self.house == None and self.hunger < 100:
            self.hunger +=10
        elif self.status == 'dead':
            print("он мертв")
        elif self.hunger >= 80:
            self.eat()
        elif self.hunger >= 100:
            print('{} УМЕР'.format(self.name, color='red'))
            self.status = 'dead'
        elif dice == 1:
            self.sleep()
            print("Спит в доме король")
        else:
            self.FUN()


def life(n):
    global cat, man
    for i in range(n):
        print(f'============DAY {i}============')
        man.act()
        cat.act()
        man.sleep()
        cat.sleep()
        if cat.status == 'dead' and man.status == 'dead':
            break


# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.
cats = [
    Cat(name="Barsssik"),Cat(name="slave"), Cat(name="poop"),
]
house = House()

citizens = [
    Man(name='Бивис', house=house),
    Man(name='Батхед', house=house),
    Man(name='Кенни', house=house),
]
for cat in cats:
    citizens[0].pickup_cat(cat)
# my_sweet_home = House()
# for citisen in citizens:
#     citisen.go_to_the_house(house=my_sweet_home)

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    for citisen in citizens:
        citisen.act()
        citisen.sleep()
    for cat in cats:
        cat.act()
        cat.sleep()
# Создадим двух людей, живущих в одном доме - Бивиса и Батхеда
# Нужен класс Дом, в нем должн быть холодильник с едой и тумбочка с деньгами
# Еда пусть хранится в холодильнике в доме, а деньги - в тумбочке.
