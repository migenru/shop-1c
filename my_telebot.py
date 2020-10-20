import telebot

TOKEN = '1161359976:AAH_FxXhROq3aX0tjX5oYxEI5_Z50_naJoM'


bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Вам нужно пройти идентификацию. Введите ключевое слово")

@bot.message_handler(content_types=['text'])
def validator(message):
    if message.text == 'programishka':
        bot.send_message(message.chat.id, 'Вы успешно авторизовались')
    else:
        bot.send_message(message.chat.id, 'Вы не прошли авторизацию. До свидания!')


bot.polling()