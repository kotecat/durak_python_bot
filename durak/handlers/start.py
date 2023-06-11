from aiogram import types
from loader import bot, dp, gm, CHOISE
from objects import *


@dp.message_handler(commands=['start'], chat_type=['group', 'supergroup'])
async def start_handler(message: types.Message):
    ''' Start a game '''
    user = types.User.get_current()
    chat = types.Chat.get_current()

    try:
        game = gm.get_game_from_chat(chat)
    except NoGameInChatError:
        await message.answer('В этом чате нет игры!!\nСоздайте её при помощи - /new')
        return
    
    try:
        # game start
        gm.start_game(game)
    except GameStartedError:
        await message.answer('Игра уже запущена!')
    except NotEnoughPlayersError:
        await message.answer('Недостаточно игроков!\nЗайти в игру - /join')
    
    else:
        await message.answer(f'Игра началась!\n\nКозырь - {game.deck.trump_ico}')

        current = game.current_player
        await message.answer(f'({current.user.get_mention(as_html=True)}) - Ваш ход!', reply_markup=types.InlineKeyboardMarkup(inline_keyboard=CHOISE))