from PIL import Image, ImageFont, ImageDraw, ImageFile
from pprint import pprint
from os.path import join, abspath



# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru

def make_ticket(fio, from_, to, date):
    with Image.open(join(abspath('images'), from_)) as first_image:
        second_image = Image.new('RGBA', first_image.size, (0, 0, 0, 0))
        font = ImageFont.truetype(join(abspath('python_snippets'), 'fonts', 'fff.ttf'), 18)
        font_txt = ImageFont.truetype(join(abspath('python_snippets'), 'fonts', 'fff.ttf'), 14)
        txt = ImageDraw.Draw(second_image)
        txt.text((45, 120), text="Aboba", font=font, fill = (0,0,0,255))
        txt.text((45, 190), text="Земля", font=font, fill = (0,0,0,255))
        txt.text((45, 255), text="Луна", font=font, fill = (0,0,0,255))
        txt.text((270, 260), text=date, font=font_txt, fill = (0,0,0,255))
        out = Image.alpha_composite(first_image, second_image)
        out.save(join(abspath('images'), to))
        out.show()
make_ticket('aboba', 'ticket_template.png',' ticket_template2.png', "30.02.1969")
# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля agrparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.
