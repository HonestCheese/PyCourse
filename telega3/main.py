from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
import asyncio
from aiogram import F
from aiogram.fsm.state import StatesGroup, State
import config
import casic
import money
import datetime
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Конфигурация
token = config.token
bot_username = "gandonica_bot"

# Инициализация бота и диспетчера
bot = Bot(token=token)
dp = Dispatcher(storage=MemoryStorage())

# Клавиатуры
menu_kb = [
    [KeyboardButton(text="Профиль")],[KeyboardButton(text="Купить вип")],
    [KeyboardButton(text="Игры🎰🚀"), KeyboardButton(text="Промокод🎫")]
]
menu = ReplyKeyboardMarkup(keyboard=menu_kb, resize_keyboard=True, one_time_keyboard=True)

m_list = [
    [KeyboardButton(text="Crash🚀"), KeyboardButton(text="Слоты🎰")],
    [KeyboardButton(text="Рандомайзер🎲")],
    [KeyboardButton(text="Меню")]
]
mkeyboard = ReplyKeyboardMarkup(keyboard=m_list, resize_keyboard=True, one_time_keyboard=True)

# База данных и игры
db = money.PlayerDatabase()
crash = casic.Crash()
slots = casic.Slotsgame()
r = casic.Randomgame()
# Состояния FSM
class Slotfsm(StatesGroup):
    pet = State()
    next = State()

class Randfsm(StatesGroup):
    pet = State()
    stavka = State()
    next = State()

class Crashfsm(StatesGroup):
    pet = State()
    x = State()
    next = State()

class Reg(StatesGroup):
    name = State()

# Генерация реферальной ссылки
def generate_referral_link(bot_username, user_id):
    return f"https://t.me/{bot_username}?start={user_id}"

# Обработчики команд
@dp.message(Command("start"))
async def start_command_handler(message: Message, state: FSMContext):
    args = message.text.split()[1:]
    referrer_id = None

    if args:
        try:
            referrer_id = int(args[0])
        except ValueError:
            await message.answer("Некорректный ID реферера.")
            return

    user_info = db.get_player_info(message.from_user.id)
    if user_info:
        await message.answer("Здравствуйте🤝, на казино BestWin | Симулятор Казино и Ставок 🎰", reply_markup=menu)
    else:
        await state.update_data(referrer_id=referrer_id)
        await message.answer('Здравствуйте🤝, введите свой игровой ник🎰: ')
        await state.set_state(Reg.name)

@dp.message(Reg.name)
async def process_name(message: Message, state: FSMContext):
    player_name = message.text
    user_id = message.from_user.id

    data = await state.get_data()
    referrer_id = data.get('referrer_id')
    registration_result = db.register_player(user_id, player_name, referrer_id)

    if "успешно зарегистрировались" in registration_result:
        db.add_balance(user_id, 100)
        await message.answer(
            f"{registration_result}\nВам начислено 100 монет.",
            reply_markup=menu
        )

        if referrer_id:
            if db.get_player_info(referrer_id)['vip_status'] == "Premium 🎰":
                db.add_referral(referrer_id, user_id)
                db.add_balance(referrer_id, 300)
            else:
                db.add_referral(referrer_id, user_id)
                db.add_balance(referrer_id, 100)
    else:
        await message.answer(registration_result)

    await state.clear()

@dp.message(F.text == "Купить")
async def buy_command(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Неделя - 100₽")],
            [KeyboardButton(text="Месяц - 150₽")],
            [KeyboardButton(text="Всегда - 200₽")],
            [KeyboardButton(text="Выйти")]
        ],
        resize_keyboard=True
    )
    await message.reply("Выберите подписку:", reply_markup=keyboard)

async def give_money():
    while True:
        await asyncio.sleep(3600)
        db.give_vipmoney()

async def send_message_to_all():
    while True:
        await asyncio.sleep(3600)
        db.check_vip_time()

@dp.message(lambda message: message.text in ["Выйти"])
async def pon(message: types.Message):
    await message.answer("Вы вышли в меню", reply_markup=menu)
@dp.message(lambda message: message.text in ["Неделя - 100₽", "Месяц - 150₽", "Всегда - 200₽"])
async def process_subscription_choice(message: types.Message):
    choice = message.text
    prices = {
        'Неделя - 100₽': types.LabeledPrice(label='Неделя - 100₽', amount=10000),
        'Месяц - 150₽': types.LabeledPrice(label='Месяц - 150₽', amount=15000),
        'Всегда - 200₽': types.LabeledPrice(label='Всегда - 200₽', amount=20000)
    }
    await bot.send_invoice(
        message.chat.id,
        title="Подписка",
        description=f"Вы выбрали {choice}.",
        provider_token=config.YOOTOKEN,
        currency='RUB',
        prices=[prices[choice]],
        start_parameter='subscription-purchase',
        payload=choice
    )

@dp.pre_checkout_query()
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

@dp.message(lambda message: message.content_type == types.ContentType.SUCCESSFUL_PAYMENT)
async def process_successful_payment(message: types.Message):
    subscription_type = message.successful_payment.invoice_payload
    purchase_time = datetime.datetime.now()
    your_function(subscription_type, purchase_time)
    await message.reply(f"{db.give_vip(message.from_user.id, subscription_type)}")

def your_function(subscription_type, purchase_time):
    logging.info(f"Подписка: {subscription_type}, Время оформления: {purchase_time}")

@dp.message(F.text == "Меню")
async def menus(message: types.Message):
    if not db.get_player_info(message.from_user.id):
        await message.reply("Вы не зарегистрированы")
        return
    await message.answer("Выберите действие: ", reply_markup=menu)

@dp.message(F.text == "Профиль")
async def profile(message: types.Message):
    if not db.get_player_info(message.from_user.id):
        await message.reply("Вы не зарегистрированы")
        return
    
    user_id = message.from_user.id
    user_info = db.get_player_info(user_id)
    referrer_id = db.get_referrer(user_id)
    
    if referrer_id:
        referrer_info = db.get_player_info(referrer_id)
        referrer_text = (
            f"Ник: {referrer_info.get('nickname', 'Неизвестно')}, "
            f"Статус: {referrer_info.get('vip_status', 'Неизвестно')}, "
        )
    else:
        referrer_text = "Нет реферера"
    
    referral_link = generate_referral_link(bot_username, message.from_user.id)

    user_info_text = (
        f"Информация о вас:\n"
        f"Ваш ID: {message.from_user.id}\n"
        f"Ваш VIP: {user_info.get('vip_status', 'Статус не установлен')}\n"
        f"Ваш реферер: {referrer_text}\n"
        f"Количество монет: {user_info.get('balance', 0.0)}💲\n"
        f"Ваша реферальная ссылка: {referral_link}\n"
    )
    await message.answer(user_info_text, reply_markup=menu)

kb_list = [
    [KeyboardButton(text="📈 Начать")],
    [KeyboardButton(text="🎫 Поменять ставку")],
    [KeyboardButton(text="🚪 Выйти")]
]
keyboard = ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True, one_time_keyboard=True)

@dp.message(F.text == "Игры🎰🚀")
async def games(message: types.Message):
    if not db.get_player_info(message.from_user.id):
        await message.reply("Вы не зарегистрированы")
        return
    await message.answer("Выберите действие: ", reply_markup=mkeyboard)

@dp.message(F.text == "Crash🚀")
async def with_puree(message: types.Message, state: FSMContext):
    if not db.get_player_info(message.from_user.id):
        await message.reply("Вы не зарегистрированы")
        return
    await message.answer("Введите вашу ставку: ")
    await state.set_state(Crashfsm.pet)

@dp.message(F.text == "Слоты🎰")
async def with_puree(message: types.Message, state: FSMContext):
    if not db.get_player_info(message.from_user.id):
        await message.reply("Вы не зарегистрированы")
        return
    await message.answer("Введите вашу ставку: ")
    await state.set_state(Slotfsm.pet)

@dp.message(F.text == "Рандомайзер🎲")
async def with_puree(message: types.Message, state: FSMContext):
    if not db.get_player_info(message.from_user.id):
        await message.reply("Вы не зарегистрированы")
        return
    await message.answer("Введите вашу ставку: ")
    await state.set_state(Randfsm.pet)

@dp.message(Slotfsm.pet)
async def moneyfsmslot(message: Message, state: FSMContext):
    try:
        pet = int(message.text)
        await state.update_data(pet=pet)
        await state.set_state(Slotfsm.next)
        await message.answer("Выберите действие: ", reply_markup=keyboard)
    except ValueError:
        await message.answer("Введите число!")

@dp.message(Slotfsm.next)
async def startslot(message: Message, state: FSMContext):
    if message.text == "📈 Начать":
        data = await state.get_data()
        result = slots.play(int(data['pet']), user=message.from_user.id)
        await message.answer(result)
        await message.answer("Выберите действие: ", reply_markup=keyboard)
    elif message.text == "🎫 Поменять ставку":
        await message.answer("Введите вашу ставку: ")
        await state.set_state(Slotfsm.pet)
    elif message.text == "🚪 Выйти":
        await state.clear()
        await message.answer("Вы вышли из игры Слоты🎰.", reply_markup=mkeyboard)

@dp.message(Randfsm.pet)
async def moneyfsmrand(message: Message, state: FSMContext):
    try:
        pet = int(message.text)
        await state.update_data(pet=pet)
        await message.answer("Введите на что ставить (например: 1-3, 3-6, 3, 5): ")
        await state.set_state(Randfsm.stavka)
    except ValueError:
        await message.answer("Введите число!")

@dp.message(Randfsm.stavka)
async def stavkarand(message: Message, state: FSMContext):
    try:
        stavka = message.text
        await state.update_data(stavka=stavka)
        data = await state.get_data()
        await message.answer(f"Ваша ставка {data['pet']}, вы поставили на {data['stavka']}x")
        await state.set_state(Randfsm.next)
        await message.answer("Выберите действие: ", reply_markup=keyboard)
    except ValueError:
        await message.answer("Введите число с плавающей точкой, например, 2.0")

@dp.message(Randfsm.next)
async def startrand(message: Message, state: FSMContext):
    if message.text == "📈 Начать":
        data = await state.get_data()
        result = r.game(money=int(data["pet"]), stavka=data["stavka"], userid=message.from_user.id)
        await message.answer(result)
        await message.answer("Выберите действие: ", reply_markup=keyboard)
    elif message.text == "🎫 Поменять ставку":
        await message.answer("Введите вашу ставку: ")
        await state.set_state(Randfsm.pet)
    elif message.text == "🚪 Выйти":
        await state.clear()
        await message.answer("Вы вышли из игры Рандомайзер🎲.", reply_markup=mkeyboard)

@dp.message(Crashfsm.pet)
async def moneyfsmcrash(message: Message, state: FSMContext):
    try:
        pet = int(message.text)
        await state.update_data(pet=pet)
        await message.answer("Введите множитель (например, 2.0): ")
        await state.set_state(Crashfsm.x)
    except ValueError:
        await message.answer("Введите число!")

@dp.message(Crashfsm.x)
async def stavka(message: Message, state: FSMContext):
    try:
        stavka = float(message.text)
        await state.update_data(stavka=stavka)
        data = await state.get_data()
        await message.answer(f"Ваша ставка {data['pet']}, множитель {data['stavka']}x")
        await state.set_state(Crashfsm.next)
        await message.answer("Выберите действие: ", reply_markup=keyboard)
    except ValueError:
        await message.answer("Введите число с плавающей точкой, например, 2.0")

@dp.message(Crashfsm.next)
async def startcrash(message: Message, state: FSMContext):
    if message.text == "📈 Начать":
        data = await state.get_data()
        result = crash.crash(money=int(data["pet"]), stavka=float(data["stavka"]), user=message.from_user.id)
        await message.answer(result)
        await message.answer("Выберите действие: ", reply_markup=keyboard)
    elif message.text == "🎫 Поменять ставку":
        await message.answer("Введите вашу ставку: ")
        await state.set_state(Crashfsm.pet)
    elif message.text == "🚪 Выйти":
        await state.clear()
        await message.answer("Вы вышли из игры Crash🚀.", reply_markup=mkeyboard)

async def main():
    asyncio.create_task(give_money())
    asyncio.create_task(send_message_to_all())
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
