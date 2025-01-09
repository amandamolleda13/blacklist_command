import os
from decouple import config 
import telebot
from dotenv import load_dotenv
load_dotenv()

bot2 = telebot.TeleBot(token = os.getenv('api_key2'))
bot2.set_webhook()

@bot2.message_handler(commands=['blacklist'])
def handle_send_alert(message):
    from my_shared import send_alert, token_input
    bot2.send_message(chat_id=message.chat_id2, text=text)

@bot2.message_handler(commands=['blacklist'])
def handle_blacklist(message):
    from my_shared import send_alert, token_input
    token_input(message)

bot2.infinity_polling(timeout=10, long_polling_timeout = 5)
