import os
import random
from os import environ
from pyrogram import Client, filters

API_ID = "11920851"
API_HASH = "8a11554cddfe55b6f19244267b6a5c64"
BOT_TOKEN = "5312381495:AAF_ete6uFJcXHYBUiwod72JbispXEdC74w"

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
    caption=f"Hello {message.from_user.first_name}, I Am A Powerful Bot devloped by Himanshu Rastogi."
  )
  
@bot.on_message(filters.regex("start"))
async def start(bot, message):
  await message.reply(
    text="Hello there"
  )
  
bot.run()
