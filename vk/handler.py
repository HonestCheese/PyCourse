import re

re_drink = re.compile(r'\bводк\b')
re_food = re.compile(r'\bрыб\b')

def handle_drink(text):
    # re.match(r'^[/w/-/s]{3,40}$', text) Могло бы быть, но нихуя у нас бот проще
    match = re.match(re_drink, text)
    if match:
        return True
    else:
        return False


def handle_food(text):
    match = re.match(re_food, text)
    if match:
        return True
    else:
        return False

def handle_final(text):
    return True
