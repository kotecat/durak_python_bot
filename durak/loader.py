from logic.game_manager import GameManager
from config import Config, COMMANDS, Commands
from db.database import db
import os
from aiogram import types, Bot, Dispatcher
from aiogram.utils.exceptions import BadRequest
from contextlib import suppress


# Database init
db.bind('sqlite', 'durak.sqlite', create_db=True)
db.generate_mapping(create_tables=True)


# Game Manager
gm = GameManager()


# Button
CHOISE = [[types.InlineKeyboardButton(text='Выбери карту!', switch_inline_query_current_chat='')]]


# SUPPRESSER
async def send_messsge(*a, **kw) -> str:
    with suppress(BadRequest):
        return await bot.send_message(*a, **kw)
    
    
# BOT & DP
bot = Bot(Config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
bot.send_message = send_messsge
dp = Dispatcher(bot)