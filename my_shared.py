import os
from decouple import config 
from telegram.ext import CommandHandler, MessageHandler, ContextTypes
from telegram import Update
import telebot
import asyncio
from pymongo import MongoClient 
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
load_dotenv()
from bot1 import bot1
from bot2 import bot2
from bot3 import bot3

client = MongoClient(os.getenv('url'), server_api=ServerApi("1"),connect=False)
db = client['blacklisted_tokens']
collection = db['blacklist']

bot_instances = {
    '1': (bot1, os.getenv('chat_id1')),
    '2': (bot2, os.getenv('chat_id2')),
    '3': (bot3, os.getenv('chat_id3')),
}

def send_alert(bot, text):
    bot_instance, chat_id = bot_instances.get(bot, None)
    bot_instance.send_message(chat_id=chat_id, text=text)
    

'''def send_alert(bot,text):
    from bot1 import bot1
    from bot2 import bot2
    from bot3 import bot3
    if bot == '1':
        bot1.send_message(chat_id = os.getenv('chat_id1'), text = text ) 
    elif bot == '2':
        bot2.send_message(chat_id = os.getenv('chat_id2'), text = text)
    elif bot == '3':
        bot3.send_message(chat_id = os.getenv('chat_id3'), text = text)'''


def token_input(message):
  token_id = message.text.split()
  token_address = {"token_address":token_id[1]}
  insert_tokens = collection.insert_one(token_address)


