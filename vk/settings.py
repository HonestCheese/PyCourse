TOKEN = 'vk1.a.176tw5aZw9udKpZzSbsWlHCh3DieYMyQYJtwRQeOcDHgLDlVj6t-sTGxuaXTin7vetz70ktle9w6ZGRZx7p8i2t2vo0OKJPRGO1Q-qBRIpXJjjXM5vDpFyhLVU3gVcsatfXw2USzdu2g7KFLMtVfwPaUD_7H4LFIcdo0WPClW7Nekvg18MedfFQD-pWQgKdFWSFofgKcctXGul3XW7Qg8g'
GROUP_ID = 230499513

START = '''Добро пожаловать!
Наш бот может
1 - оскорбить вашу маму по месту пребывания
2 - оскорбить вашу маму по месту использования
3 - оскорбить вашу маму по знаниям
4 - попиздеть по мужски'''
INTENTS = [
    {
        'name': "Адрес",
        'tokens': ('Место', 'место', 'адрес', 'Адрес', 'Где', 'где', '1'),
        'scenario': None,
        'answer': 'у мамки твоей в подвале',
    },
    {
        'name': "Время",
        'tokens': ('сколько', "когда", '2'),
        'scenario': None,
        'answer': 'а тебя ебет?',
    }, {
        'name': "Спиздануть",
        'tokens': ('спиздани', '3'),
        'scenario': None,
        'answer': 'у мамаши своей будешь такое просить',
    }, {
        'name': "мужской базар",
        'tokens': ('4'),
        'scenario': 'registration',
        'answer': None,
    }

]

SCENARIOS = {
    'registration': {
        'first_step': 'step_1',
        'start_message': 'че пьешь?',
        'end_message': 'Спасибо...',
        'steps': {
            'step_1': {
                'text': 'че ты пьешь?',
                'text_failure': 'че бля? {}? ты вообще себя уважаешь?',
                'handler': 'handle_drink',
                'next_step': 'step_2'

            },
            'step_2': {
                'text': 'а закусон имеется?',
                'text_failure': 'че бля? {}? ты вообще себя уважаешь?',
                'handler': 'handle_food',
                'next_step': 'step_3'
            },
            'step_3': {
                'text': 'а чем полировать будешь?',
                'text_failure': 'че бля? {}? ты вообще себя уважаешь?',
                'handler': 'handle_final',
                'next_step': 'step_4'
            },
            'step_4': {
                'text': 'спасибо бля за участие?',
                'text_failure': None,
                'handler': None,
                'next_step': None
            }
        }
    }
}
DEFAULT_ANSWER = 'не ебу о чем ты дорогуша. Лучше скажи что будешь пить'
