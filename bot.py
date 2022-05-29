import os
import random
from os import environ
from pyrogram import Client, filters

API_ID = environ.get('API_ID')
API_HASH = environ.get('API_HASH')
BOT_TOKEN = environ.get('BOT_TOKEN')

bot = Client('New Peoject',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
            )

PHOTO = ["https://telegra.ph/file/a977da35cd09e365f985d.jpg", "https://telegra.ph/file/034cbc7e5084c46861b89.jpg", "https://telegra.ph/file/ad55e54a5139d5996d16c.jpg", "https://telegra.ph/file/85d0bc21c67fd6b61a583.jpg", "https://telegra.ph/file/9faa892b86826852f5088.jpg"]

@bot.on_message(filters.command('start'))
async def start(bot, message):
  await message.reply_photo(
    photo=random.choice(PHOTO),
    text=f"Hello {message.from_user.first_name}, I Am A Powerful Bot devloped by Himanshu Rastogi."
  )
  
bot.run()
