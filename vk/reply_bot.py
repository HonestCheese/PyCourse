import logging

import requests
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id

from logging import getLogger, FileHandler, Formatter, DEBUG

from vk.settings import TOKEN, GROUP_ID

logger = getLogger("pablo")
logger.setLevel(DEBUG)
handler = FileHandler('bot.log')
formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
class VkBot:
    """
    Creates a bot to handle incoming messages
    """
    def __init__(self, TOKEN, GROUP_ID):
        self.token = TOKEN
        self.group_id = GROUP_ID
        self.vk_session = vk_api.VkApi(token=self.token)
        self.group = vk_api.bot_longpoll.VkBotLongPoll(group_id=self.group_id, vk=self.vk_session)
        self.vk = self.vk_session.get_api()
        logger.info('Сервер был открыт')
    def run(self):
        try:
            for event in self.group.listen():
                if event.type == VkBotEventType.MESSAGE_NEW:
                    logger.info(f'New message - {event.obj.message['text']}')
                    self.vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=f'Получил какой то бред: {event.obj.message['text']}',
                                     random_id = get_random_id())
                    logger.info(f'Reply - Получил какой то бред: {event.obj.message['text']}')
                if event.type == VkBotEventType.MESSAGE_TYPING_STATE:
                    self.vk.messages.send(user_id=event['from_id'], #TODO разобраться с текстом
                                          message=f'Хватит печатать',
                                          random_id=get_random_id())
        except KeyboardInterrupt:
            exit("Server closed by owner")
        except Exception as e:
            logger.error(f'Server down due {e}')
if __name__ == '__main__':
    bot = VkBot(TOKEN, GROUP_ID)
    bot.run()