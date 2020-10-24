from django.core.management.base import BaseCommand, CommandError
import telebot
from telegrambot.models import Accessbot

class Command(BaseCommand):
    help = 'Telegrambot'

    def handle(self, *args, **options):
        TOKEN = '1161359976:AAH_FxXhROq3aX0tjX5oYxEI5_Z50_naJoM'

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