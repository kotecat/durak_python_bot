from aiogram import types
from loader import bot, dp, gm, Config, Commands
from objects import *


@dp.message_handler(commands=[Commands.JOIN], chat_type=['group', 'supergroup'])
async def join_handler(message: types.Message):
    ''' Join in a game '''
    user = types.User.get_current()
    chat = types.Chat.get_current()

    try:
        game = gm.get_game_from_chat(chat)
    except NoGameInChatError:
        await message.answer('В этом чате нет игры!!\nСоздайте её при помощи - /new')
        return
    
    try:
        # add user in a game
        gm.join_in_game(game, user)
    except GameStartedError:
        await message.answer('Игра уже запущена! Вы не можете присоединиться!')
    except LobbyClosedError:
        await message.answer('Лобби закрыто!\nОткрыть - /open')
    except LimitPlayersInGameError:
        await message.answer(f'Достигнут лимит в {Config.MAX_PLAYERS} игроков!')
    except AlreadyJoinedInGlobalError:
        await message.answer('Похоже вы играете в другом чате!\nПокинуть эту игру - /gleave')
    except AlreadyJoinedError:
        await message.answer('В игре ты!')
        
    else:
        await message.answer(f'{user.get_mention(as_html=True)} присоединился к игре!')