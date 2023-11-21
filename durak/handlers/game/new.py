from aiogram import types
from loader import bot, dp, gm, Commands
from durak.objects import *


@dp.message_handler(commands=[Commands.NEW], chat_type=['group', 'supergroup'])
async def new_handler(message: types.Message):
    ''' Creating new game '''
    print("fd")
    user = types.User.get_current()
    chat = types.Chat.get_current()

    try:
        # create
        game = gm.new_game(chat, creator=user)
    except GameAlreadyInChatError:
        await message.answer('В этом чате уже есть игра')
        return
    
    await message.answer(f'Запустил!\n/{Commands.JOIN} - войти')