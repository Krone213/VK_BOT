import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

def write_msg(user_id, message):
    vk.method("messages.send", {"user_id":user_id, "message":message, "random_id":user_id})
    print(user_id)

#entered the token
token = '*****'

#Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)
while True:
	# Основной цикл
	for event in longpoll.listen():
		print(1)
    	# Если пришло новое сообщение
		if event.type == VkEventType.MESSAGE_NEW:
        	# Если оно имеет метку для бота
			if event.to_me:
            	# Сообщение от пользователя
				request = event.text
            	# логика ответа
				if request == "привет":
					write_msg(event.user_id, "Привет!!!")
					print(0)
				elif request == "пока":
					write_msg(event.user_id, "Пока")
				else:
					write_msg(event.user_id, "Пока не понимаю вас")
