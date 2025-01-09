import os
from decouple import config 
import telebot
from dotenv import load_dotenv
load_dotenv()

bot1 = telebot.TeleBot(token = os.getenv('api_key'))
bot1.set_webhook()


@bot1.message_handler(commands=['blacklist'])
def handle_send_alert(message):
    from my_shared import send_alert, token_input
    bot1.send_message(chat_id=message.chat_id1, text=text)

@bot1.message_handler(commands=['blacklist'])
def handle_blacklist(message):
    from my_shared import send_alert, token_input
    token_input(message)
    

bot1.infinity_polling(timeout=10, long_polling_timeout = 5)


