import logging
from aiogram import types, executor
from loader import gm, bot, dp, Config
import handlers


logging.basicConfig(level=logging.INFO)


async def on_startup(dp):
    print("bot started!")


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)