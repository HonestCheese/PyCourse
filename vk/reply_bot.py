import logging

import requests
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
from logging import getLogger, FileHandler, Formatter, DEBUG
from vk.settings import TOKEN, GROUP_ID, SCENARIOS, INTENTS, START
import vk.handler as h

logger = getLogger("pablo")
logger.setLevel(DEBUG)
handler = FileHandler('bot.log')
formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class UserState:
    """Состояние пользователя внутри сценария"""

    def __init__(self, scenario_name, step_name, context):
        self.scenario_name = scenario_name
        self.step_name = step_name
        self.context = context


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
        self.user_states = dict()  # user_id -> user_state
        self.send = 0
        logger.info('Сервер был открыт')

    def run(self):
        for event in self.group.listen():
            if event.raw['type'] != 'message_typing_state' and event.raw['type'] != 'message_reply':
                try:
                    self.on_event(event)
                except KeyboardInterrupt:
                    exit("Server closed by owner")
                # except Exception as e:
                #     logger.error(f'Server down due {e}')

    def on_event(self, event):
        if VkBotEventType.MESSAGE_NEW == event.type:
            user = event.obj.message['from_id']
            text = event.object.message['text']
            if user in self.user_states:
                text_to_send = self.continue_scenario(event, user, self.send)
                self.vk.messages.send(user_id=event.obj.message['from_id'],
                                      message=text_to_send,
                                      random_id=get_random_id(),
                                      )
            else:
                for intent in INTENTS:
                    if any(token in intent['tokens'] for token in text.split(' ')):
                        text_to_send = intent['answer']
                        if intent['scenario']:
                            if user not in self.user_states:
                                self.user_states[user] = UserState(scenario_name='registration',
                                                                   context=event.obj.message['text'],
                                                                   step_name=SCENARIOS['registration'][
                                                                       'first_step'])
                                text_to_send = SCENARIOS['registration']['start_message']
                                self.vk.messages.send(user_id=event.obj.message['from_id'],
                                                      message=text_to_send,
                                                      random_id=get_random_id())
                                break
                        self.vk.messages.send(user_id=event.obj.message['from_id'],
                                              message=text_to_send,
                                              random_id=get_random_id())
                        break

                else:
                    self.vk.messages.send(user_id=event.obj.message['from_id'],
                                          message=START,
                                          random_id=get_random_id())

    def continue_scenario(self, event, user, send):
        state = self.user_states[user]
        step = SCENARIOS[state.scenario_name]['steps'][state.step_name] if SCENARIOS[state.scenario_name]['steps'][
                                                                               state.step_name] is not None else None
        hand = getattr(h, step['handler']) if step['handler'] is not None else True
        text_to_send = SCENARIOS[state.scenario_name]['steps'][state.step_name]['text']
        if step['next_step'] is None:
            self.user_states.pop(user)
            return START
        elif hand(event.object.message['text']):
            self.user_states[user].step_name = SCENARIOS[state.scenario_name]['steps'][state.step_name]['next_step']
            text_to_send = SCENARIOS[state.scenario_name]['steps'][state.step_name]['text']
            return text_to_send.format(event.object.message['text'])
        else:
            text_to_send = SCENARIOS[state.scenario_name]['steps'][state.step_name]['text_failure']
            return text_to_send.format(event.object.message['text'])


if __name__ == '__main__':
    bot = VkBot(TOKEN, GROUP_ID)
    bot.run()
