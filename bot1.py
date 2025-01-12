import os
from decouple import config 
import telebot
from dotenv import load_dotenv
load_dotenv()

bot1 = telebot.TeleBot(token = os.getenv('api_key1'))


@bot1.message_handler(commands=['blacklist'])
def handle_blacklist(message):
    from my_shared import token_input
    token_input(message)
    
if __name__ == "__main__":
    bot1.infinity_polling(timeout=10, long_polling_timeout=5)

