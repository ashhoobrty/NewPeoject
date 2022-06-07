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
    caption=f"Hello {message.from_user.first_name}, I Am A Powerful Bot devloped by Himanshu Rastogi."
  )
  
@bot.on_message(filters.regex("start"))
async def start(bot, message):
  await message.reply(
    text="Hello there"
  )

@bot.on_message(filters.command('send'))
async def send(bot, message):
    if len(message.command) == 1:
        return await message.reply('Give me a chat id, whom to send message.')
    chat = message.command[1]
    try:
        chat = int(chat)
    except:
        chat = message.reply_to_message_id
    if len(message.command) == 2:
        return await message.reply('Give me a message.')
    msg = message.command[2]
    try: 
        msg = int(msg)
    except:
        msg=msg
    try:
        await bot.send_message(chat, msg)
        await message.reply(f'Successfully sent {msg} to {chat}.')
    except Exception as e:
        await message.reply(f'Error - {e}')
        
@bot.on_message(filters.regex("hello"))
async def start(bot, message):
  await message.reply(
    text="Hii"
  )

@bot.on_message(filters.private)
async def hello(client, message):
    await message.reply("Hello from Pyrogram!")
    
@bot.on_message(filters.command("info"))
async def info(bot, message):
  if len(message.command) == 1:
    return await message.reply("Give me a user id")
  chat = message.command[1]
  try:
    chat = int(chat)
  except:
    chat = chat
  try:
      await message.get_users(chat)
  except Exeption as e:
    await message.reply(f"#Error - {e}")
    
CHAT = "-1001553569882"
    
@bot.on_message(filters.command('start') & filters.chat(CHAT) & (filters.document))
async def document(bot, message):
  await message.reply(
    text="hello"
  )
 
bot.run()
