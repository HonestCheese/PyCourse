import requests
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.longpoll import VkLongPoll
from vk_api.utils import get_random_id

def main():
    session = requests.Session()
    vk_session = vk_api.VkApi(token='vk1.a.176tw5aZw9udKpZzSbsWlHCh3DieYMyQYJtwRQeOcDHgLDlVj6t-sTGxuaXTin7vetz70ktle9w6ZGRZx7p8i2t2vo0OKJPRGO1Q-qBRIpXJjjXM5vDpFyhLVU3gVcsatfXw2USzdu2g7KFLMtVfwPaUD_7H4LFIcdo0WPClW7Nekvg18MedfFQD-pWQgKdFWSFofgKcctXGul3XW7Qg8g')
    group = vk_api.bot_longpoll.VkBotLongPoll(group_id=230499513, vk=vk_session)
    vk = vk_session.get_api()
    upload = vk_api.VkUpload(vk_session)
    for event in group.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            print('Новое сообщение:', event.obj.message['text'])
            vk.messages.send(user_id=event.obj.message['from_id'], message=f'Получил какой то бред: {event.obj.message['text']}', random_id = get_random_id())
if __name__ == '__main__':
    main()