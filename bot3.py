import os
from decouple import config 
import telebot
from dotenv import load_dotenv
load_dotenv()

bot3 = telebot.TeleBot(token = os.getenv('api_key3'))


@bot3.message_handler(commands=['blacklist'])
def handle_blacklist(message):
    from my_shared import send_alert, token_input
    token_input(message)

if __name__ == "__main__":
    bot3.infinity_polling(timeout=10, long_polling_timeout=5)
