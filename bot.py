import os
from os import environ
from pyrogram import Client

API_ID = environ.get('API_ID')
API_HASH = environ.get('API_HASH')
BOT_TOKEN = environ.get('BOT_TOKEN')

bot = Client('New Peoject',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
            )
  
bot.run()
