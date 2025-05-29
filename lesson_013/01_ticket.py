from PIL import Image, ImageFont, ImageDraw, ImageFile
from pprint import pprint
from os.path import join, abspath
import argparse


def make_ticket(fio, from_, to, date, save_to='ticket_template2.png'):
    with Image.open(join(abspath('images'), 'ticket_template.png')) as first_image:
        second_image = Image.new('RGBA', first_image.size, (0, 0, 0, 0))
        font = ImageFont.truetype(join(abspath('python_snippets'), 'fonts', 'fff.ttf'), 18)
        font_txt = ImageFont.truetype(join(abspath('python_snippets'), 'fonts', 'fff.ttf'), 14)
        txt = ImageDraw.Draw(second_image)
        txt.text((45, 120), text=fio, font=font, fill=(0, 0, 0, 255))
        txt.text((45, 190), text=from_, font=font, fill=(0, 0, 0, 255))
        txt.text((45, 255), text=to, font=font, fill=(0, 0, 0, 255))
        txt.text((270, 260), text=date, font=font_txt, fill=(0, 0, 0, 255))
        out = Image.alpha_composite(first_image, second_image)
        out.save(join(abspath('images'), save_to))
        out.show()


parser = argparse.ArgumentParser()
parser.add_argument('-f', '--from_',
                    help="Where are you")
parser.add_argument('-w', '--where',
                    help="Where would you like to fly")
parser.add_argument('-n', '--name',
                    help="Your FIO")
parser.add_argument('-d', '--date',
                    help="Date to fly")
parser.add_argument('-s', '--save_to',
                    help="file to save")

args = parser.parse_args()
try:
    make_ticket(fio=args.name, from_=args.from_, date=args.date, to=args.where, save_to=args.save_to)
except:
    print("""REQUIREMENT ARGUMENTS
-f, --from_ Where are you
-w' --where, Where would you
-n' --name, Your FIO
-d' --date, Date to fly
optional -s --save_to""")
