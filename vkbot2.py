from vk_api.longpoll import VkLongPoll, VkEventType

import requests
import vk_api

vk_session = vk_api.VkApi(token='******')
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
   #Слушаем longpoll		
        if event.text == 'Привет' or event.text == 'привет': #Если написали заданную фразу
            if event.from_user:
                print('Привет')
                vk.messages.send( #Отправляем сообщение
                    user_id=event.user_id,
                    message='Привет.',
                    random_id=event.user_id
		)
        elif event.text == 'Пока' or event.text == 'пока': #Если написали заданную фразу
            if event.from_user: 
                print('Пока')
                vk.messages.send( #Отправляем сообщение
                    user_id=event.user_id,
                    message='Пока.',
                    random_id=event.user_id
        )
        else:
            if event.from_user: 
                print('Я вас не понимаю')
                vk.messages.send( #Отправляем сообщение
                    user_id=event.user_id,
                    message='Я вас не понимаю.',
                    random_id=event.user_id
        )