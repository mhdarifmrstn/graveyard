from pyrogram import Client, idle
from dotenv import load_dotenv
from os import getenv
from asyncio import get_event_loop

load_dotenv()

api_id = int(getenv("API_ID"))
api_hash = getenv("API_HASH")
string_session = getenv("USER_STRING_SESSION")
bot_token = getenv("BOT_TOKEN")
user_account = Client("graveyard_user", api_id, api_hash, session_string=string_session)
bot_account = Client("graveyard_bot", api_id, api_hash, bot_token=bot_token)
loop = get_event_loop()

async def init():
  await user_account.start()
  user = await user_account.get_me()
  print(f"App started as {user.first_name}")
  await bot_account.start()
  bot = await bot_account.get_me()
  print(f"App started as {bot.username}")
  await idle()

loop.run_until_complete(init())