import logging
from aiogram import types, executor
from loader import gm, bot, dp, Config, COMMANDS
import handlers


logging.basicConfig(level=logging.INFO)


async def on_startup(*args):
    print("bot started!")
    
    commands = []
    for cmd, d in COMMANDS:
        commands.append(types.BotCommand(cmd, d))
    
    await bot.set_my_commands(commands)


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)