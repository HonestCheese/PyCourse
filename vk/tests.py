from unittest import TestCase
from unittest.mock import patch

from reply_bot import VkBot


class Test1(TestCase):
    def test_(self):
        with patch('reply_bot.vk_api.VkApi'):
            with patch('reply_bot.vk_api.bot_longpoll.VkBotLongPoll'):
                with patch('reply_bot.vk_session.get_api'):
                    bot = VkBot('','')
                    print()

