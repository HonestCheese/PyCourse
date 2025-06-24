from unittest import TestCase
from unittest.mock import patch, Mock

from vk_api.bot_longpoll import VkBotEventType, VkBotMessageEvent

from reply_bot import VkBot


class Test1(TestCase):
    def test_run(self):
        count = 5
        events = [{}] * count  # [{}, {}, {},...]
        long_poller_mock = Mock()
        long_poller_mock.listen = Mock(return_value=events)
        with patch('reply_bot.vk_api.VkApi'):
            with patch('reply_bot.vk_api.bot_longpoll.VkBotLongPoll', return_value=long_poller_mock):
                bot = VkBot('', '')
                bot.on_event = Mock()
                bot.run()

                bot.on_event.assert_called()
                bot.on_event.assert_any_call({})
                bot.on_event.call_count == count

    def test_on_event_message_new(self):
        raw_event = {'event_id': '0a3c7c527c21608156f9e1c003eb274352ffe373', 'group_id': 230499513, 'object': {
            'client_info': {
                'button_actions': ['text', 'vkpay', 'open_app', 'location', 'open_link', 'callback', 'intent_subscribe',
                                   'intent_unsubscribe'], 'carousel': True, 'inline_keyboard': True, 'keyboard': True,
                'lang_id': 0},
            'message': {'attachments': [], 'conversation_message_id': 98, 'date': 1748947925, 'from_id': 483849246,
                        'fwd_messages': [], 'id': 105, 'important': False, 'is_hidden': False, 'out': 0,
                        'peer_id': 483849246, 'random_id': 0, 'text': 'Hehehe nigger', 'version': 10000278}}, 'type': 'message_new',
                     'v': '5.199'}
        event = VkBotMessageEvent(raw_event)
        vk_mock =  Mock()
        with patch('reply_bot.vk_api.VkApi'):
            bot = VkBot('', '')
            bot.vk = vk_mock
            bot.on_event(event)
            bot.vk.messages.send.assert_called_once()
