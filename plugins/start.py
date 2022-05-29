import pyrogram
from pyrogram import filters
from pyrogram import Client as Bot

@Bot.on_message(filters.command('start'))
async def start(bot, message):
  await message.reply(
    text=f"Hello {message.from_user.mention}, I Am A Bot devoloped by Himanshu Rastogi Official."
  )
