from logic.game_manager import GameManager
from config import Config
from aiogram import types, Bot, Dispatcher


gm = GameManager()

bot = Bot(Config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)