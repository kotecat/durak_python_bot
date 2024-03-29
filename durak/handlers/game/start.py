from aiogram import types
from loader import bot, dp, gm, CHOISE, Commands
from durak.objects import *
from durak.logic.utils import (
    user_is_admin,
    user_is_creator,
    user_is_bot_admin,
    user_is_creator_or_admin
)


@dp.message_handler(commands=[Commands.START], chat_type=['group', 'supergroup'])
async def start_handler(message: types.Message):
    ''' Start a game '''
    user = types.User.get_current()
    chat = types.Chat.get_current()

    try:
        game = gm.get_game_from_chat(chat)
    except NoGameInChatError:
        await message.answer(f'В этом чате нет игры!!\nСоздайте её при помощи - /{Commands.NEW}')
        return
    
    if not (await user_is_creator_or_admin(user, game, chat)):
        await message.answer('Вы не можете начать игру!')
        return
    try:
        # game start
        gm.start_game(game)
    except GameStartedError:
        await message.answer('Игра уже запущена!')
    except NotEnoughPlayersError:
        await message.answer(f'Недостаточно игроков!\nЗайти в игру - /{Commands.JOIN}')
    
    else:
        await message.answer(f'Игра началась!\n\nКозырь - {game.deck.trump_ico}')

        current = game.current_player
        await message.answer(f'({current.user.get_mention(as_html=True)}) - Ваш ход!', reply_markup=types.InlineKeyboardMarkup(inline_keyboard=CHOISE))