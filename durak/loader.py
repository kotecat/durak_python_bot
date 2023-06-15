from logic.game_manager import GameManager
from config import Config, COMMANDS, Commands
from aiogram import types, Bot, Dispatcher


gm = GameManager()
CHOISE = [[types.InlineKeyboardButton(text='Выбери карту!', switch_inline_query_current_chat='')]]

bot = Bot(Config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)