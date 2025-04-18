import telebot
from telebot import types
import lesson_006.mastermind_engine as me
token = '7698706110:AAEDE3mIRgLr9Psvl_166I6RaXdExxEsWqs'
bot = telebot.TeleBot(token)

user_state = {}
@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button_game = types.KeyboardButton(text='жесткий вордл')
    button_nothing = types.KeyboardButton(text='Ничего')
    keyboard.add(button_game, button_nothing)
    bot.send_message(message.chat.id, "Привет! Меня пиздят палками!", reply_markup=keyboard)


# @bot.message_handler(content_types=['text'])
# def game_message(message):
#     if message.text == 'жесткий вордл':
#         bot.send_message(message.chat.id, 'Давай начнем!')
#         game = ''
#         while True:  # Подготовка к игре
#             c = 0
#             random_n = me.random_number()
#             if game == 'no':
#                 break
#             print('Игра - быки и коровы. Ничего не понятно, вводите цифры и думайте, что нужно сделать. Удачи)')
#             while True:  # Основной код игры
#                 c += 1
#                 input_n = (input('Введите число >>> '))
#                 if input_n == 'exit':
#                     break
#                 if len(input_n) != 4:  # Проверка ввода
#                     while True:
#                         input_n = (input('Введите 4 символа, пожалуйста >>> '))
#                         if input_n == 'exit':
#                             break
#                         if len(input_n) == 4:
#                             break
#                 if input_n == 'exit':
#                     break
#                 win_q = me.check_number(random_n, input_n)
#                 print(me.bulls_cows)
#                 me.bulls_cows = {
#                     'bulls': 0,
#                     'cows': 0
#                 }
#                 if win_q == 0:
#                     print(f"победил!!! Всего за.... {c} ходов!")
#                     break
#             while True:  # Проверка на вxод выход
#                 game = input('Еще игру? (yes/no) >>> ')
#                 if game == 'yes':
#                     flag = 0
#                     break
#                 elif game == 'no':
#                     print("Спасибо за игру!")
#                     break
#                 else:
#                     print('Не понял')
#     if message.text == 'Ничего':
#         bot.send_message(message.chat.id, "Ничего ничего ничего")


@bot.message_handler(content_type = ['text'])
def game(message):
    if message.text == "жесткий вордл":
        bot.send_message(message.chat.id, 'penis bobmordiro crocodildo')

@bot.message_handler(func = lambda message : True)
def recieve_text(message):
    if message.chat.id not in user_state:
        user_state[message.chat.id] = {}
    bot.send_message(message.chat.id, "ДОБРО ПОЖАЛОВАТЬ В БЫКОВ И КОРОВ")
    if message.text:
        return message.text


bot.polling(none_stop=True, interval=0)
