import os
from os import environ
from pyrogram import Client

API_ID = environ.get('API_ID')
API_HASH = environ.get('API_HASH')
BOT_TOKEN = environ.get('BOT_TOKEN')

bot = Client('New Project',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
            )

@bot.on_message(filters.command('start'))
async def start(bot, message):
  await message.reply(
    text=f"Hello {message.from_user.mention}, I Am A Bot devoloped by Himanshu Rastogi Official."
  )
  
bot.run()
