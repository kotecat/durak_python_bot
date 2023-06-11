from aiogram import types
from loader import bot, dp, gm
from objects import *


@dp.message_handler(commands=['new'], chat_type=['group', 'supergroup'])
async def new_handler(message: types.Message):
    ''' Creating new game '''
    user = types.User.get_current()
    chat = types.Chat.get_current()

    try:
        # create
        game = gm.new_game(chat, creator=user)
    except GameAlreadyInChatError:
        await message.answer('В этом чате уже есть игра')
        return
    
    await message.answer('Запустил!\n/join')