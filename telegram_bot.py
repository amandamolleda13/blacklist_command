import os
from decouple import config 
from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, ContextTypes
import telebot
import asyncio
from pymongo import MongoClient 
from pymongo.server_api import ServerApi
url = 'mongodb+srv://amanda_molleda:Macbookair13!@cluster0.tmj4x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
api_key = '7897127269:AAGxdCCm59RIsjMdGrxSZiVH27BoNl-S0T8'
chat_id = '7649031477'
bot_username = '@tg_solana_token_bot'


client = MongoClient(os.getenv('url'), server_api=ServerApi("1"),connect=False)
db = client['blacklisted_tokens']
collection = db['blacklist']


bot = telebot.TeleBot(token = os.getenv('api_key'))
bot.set_webhook()

def send_alert():
    bot.send_message(chat_id = os.getenv('chat_id'), text = 'You should sell this :)')



@bot.message_handler(commands=['blacklist'])
def token_input(message):
  token_id = message.text.split()
  token_address = {"token_address":token_id[1]}
  insert_tokens = collection.insert_one(token_address)

bot.polling()
    






