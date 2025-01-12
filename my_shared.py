import os
from decouple import config 
from telegram.ext import CommandHandler, MessageHandler, ContextTypes
from telegram import Update
import telebot
import asyncio
from pymongo import MongoClient 
from pymongo.server_api import ServerApi
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

def send_alert(bot_id, text):
    bot_instance, chat_id = bot_instances.get(bot_id, (None, None))
    if bot_instance and chat_id:
        bot_instance.send_message(chat_id=chat_id, text=text)


def token_input(message):
  token_id = message.text.split()
  token_address = {"token_address":token_id[1]}
  insert_tokens = collection.insert_one(token_address)




