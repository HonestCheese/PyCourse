import codecs
import time
from pathlib import Path
import keyboard
from art import text2art
import yaml

# Клавиша для активации
hotkey = "9"
# Клавиша для открытия чата
open_hotkey = "shift+t"
# Включить кнопку открытия чата
enable_open_chat_hotkey = True
# Клавиша для отправки сообщения
send_msg_hotkey = "enter"
# Интервал между символами
character_interval = 0
# Интервал между сообщениями
interval = 0.15

close_hotkey = "H+J"

can_run = True

def remadeConfig():
    config = {
        "hotkey": hotkey,
        "open_hotkey": open_hotkey,
        "enable_open_chat_hotkey": enable_open_chat_hotkey,
        "send_msg_hotkey": send_msg_hotkey,
        "character_interval": character_interval,
        "interval": interval,
        "close_hotkey": close_hotkey
    }
    with codecs.open('config.yml', 'w', encoding="UTF-8") as f:
        yaml.dump(config, f, default_flow_style=False, allow_unicode=True)
    time.sleep(3)
    exit(1)


def initConfig():
    global hotkey, open_hotkey, enable_open_chat_hotkey, send_msg_hotkey, character_interval, interval, close_hotkey
    if Path("config.yml").is_file():
        with codecs.open('config.yml', encoding="UTF-8") as f:
            loadedConfig = yaml.safe_load(f)
            try:
                hotkey = loadedConfig["hotkey"]
                open_hotkey = loadedConfig["open_hotkey"]
                enable_open_chat_hotkey = loadedConfig["enable_open_chat_hotkey"]
                send_msg_hotkey = loadedConfig["send_msg_hotkey"]
                character_interval = loadedConfig["character_interval"]
                interval = loadedConfig["interval"]
                close_hotkey = loadedConfig["close_hotkey"]
            except KeyError:
                print("Конфиг поврежден, перезаписываю его")
                remadeConfig()
            except TypeError:
                print("Конфиг поврежден, перезаписываю его")
                remadeConfig()


            print(
                "Привет, твои текущие настройки программы: \n"
                f"  Клавиша активации: {hotkey}\n"
                f"  Клавиша открытия чата (если включено): {open_hotkey}\n"
                f"  Включить ли клавишу для открытия чата в играх?: " + ("Нет", "Да")[enable_open_chat_hotkey] + "\n"
                f"  Интервал между символами: {character_interval}\n"
                f"  Интервал между сообшениями (рекомендуем оставить 0.2, меньше Дота не тянет): {interval}\n"
                f"  Клавиша деактивации: {close_hotkey}\n"
            )
    else:
        print("Конфиг не найден, создаю новый")
        remadeConfig()
def main():
    print(text2art("1000-7      SCRIPT", "standart"))
    print(" by zenisoft (c) 2021\n")

    initConfig()

    keyboard.add_hotkey(hotkey, lambda: print_1000_7())

    keyboard.add_hotkey(close_hotkey, lambda: invert_run(), suppress=True) # suppress=True - чтобы другие клавиши не работали

    keyboard.wait()

def invert_run():
    global can_run
    can_run = not can_run
    print("Состояние программы: " + ("Выключено", "Включено")[can_run])

def print_1000_7():
    # print("What is 1000-7?")
    if enable_open_chat_hotkey:
        keyboard.press_and_release(open_hotkey)
        keyboard.press_and_release('ctrl+a')
        keyboard.press_and_release('backspace')
        time.sleep(interval)

    keyboard.write("What is 1000-7?", character_interval)
    keyboard.press_and_release(send_msg_hotkey)

    keyboard.press_and_release('ctrl+a')
    keyboard.press_and_release('backspace')
    keyboard.press_and_release('F9')
    keyboard.write("What is 1000-7?", character_interval)
    keyboard.press_and_release(send_msg_hotkey)
    if enable_open_chat_hotkey:
        keyboard.press_and_release(open_hotkey)

    for i in range(5):
        if can_run:
            if enable_open_chat_hotkey:
                keyboard.press_and_release(open_hotkey)
                keyboard.press_and_release('ctrl+a')
                keyboard.press_and_release('backspace')
                time.sleep(interval)
            keyboard.write(str(5-i), character_interval)
            keyboard.press_and_release(send_msg_hotkey)
            time.sleep(1)

    x = 1000
    while x > 0:
        if can_run:
            var = x - 7
            if enable_open_chat_hotkey:
                keyboard.press_and_release(open_hotkey)
                keyboard.press_and_release('ctrl+a')
                keyboard.press_and_release('backspace')
                time.sleep(interval)
            keyboard.write(f"{x} - 7 = {var}", character_interval)
            # print(f"{x} - 7 = {var}")
            x = var
            time.sleep(interval)
            keyboard.press_and_release(send_msg_hotkey)



if __name__ == '__main__':
    main()
    keyboard.wait()