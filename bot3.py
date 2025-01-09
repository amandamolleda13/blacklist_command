import os
from decouple import config 
import telebot
from dotenv import load_dotenv
load_dotenv()

bot3 = telebot.TeleBot(token = os.getenv('api_key3'))
bot3.set_webhook()

@bot3.message_handler(commands=['blacklist'])
def handle_send_alert(message):
    from my_shared import send_alert, token_input
    bot3.send_message(chat_id=message.chat_id3, text=text)


@bot3.message_handler(commands=['blacklist'])
def handle_blacklist(message):
    from my_shared import send_alert, token_input
    token_input(message)

bot3.infinity_polling(timeout=10, long_polling_timeout = 5)