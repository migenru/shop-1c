import telebot
from shop.telegrambot.models import Accessbot

TOKEN = ' '


bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Вам нужно пройти идентификацию. Введите ключевое слово")

@bot.message_handler(content_types=['text'])
def validator(message):
    if message.text == 'programishka':
        bot.send_message(message.chat.id, 'Вы успешно авторизовались')
        access_bot, created = Accessbot.objects.get_or_create(id=message.chat.id, username=message.chat.username, first_name=message.chat.first_name)
    else:
        bot.send_message(message.chat.id, 'Вы не прошли авторизацию. До свидания!')

# a = 1

bot.polling()