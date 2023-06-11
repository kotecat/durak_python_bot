from aiogram import types
from loader import bot, dp


@dp.message_handler(commands=['help'])
async def help_handler(message: types.Message):
    await message.answer('help')