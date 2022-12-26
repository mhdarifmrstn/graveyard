from typing import Dict
from pyrogram import Client, filters, idle
from pyrogram.types import Message
from dotenv import load_dotenv
from os import getenv
from asyncio import get_event_loop
from astaroth_game import AstarothGame

load_dotenv()

api_id = int(getenv("API_ID"))
api_hash = getenv("API_HASH")
string_session = getenv("USER_STRING_SESSION")
bot_token = getenv("BOT_TOKEN")
user_account = Client("graveyard_user", api_id, api_hash, session_string=string_session)
bot_account = Client("graveyard_bot", api_id, api_hash, bot_token=bot_token)
loop = get_event_loop()
astaroth_id = 2075925757
astaroth_game: Dict[int, AstarothGame] = {}

@user_account.on_message(filters.group & filters.bot)
async def astaroth_remaining_cards(_, message: Message):
  if message.from_user.id != astaroth_id: return
  chat_id = message.chat.id

  if message.text.find("Permainan dimulai!") != -1:
    astaroth_game[chat_id] = AstarothGame()
    astaroth_game[chat_id].set_played_numbers(message)
    astaroth_game[chat_id].set_unplayed_numbers(message)

async def init():
  await user_account.start()
  user = await user_account.get_me()
  print(f"App started as {user.first_name}")
  await bot_account.start()
  bot = await bot_account.get_me()
  print(f"App started as {bot.username}")
  await idle()

loop.run_until_complete(init())