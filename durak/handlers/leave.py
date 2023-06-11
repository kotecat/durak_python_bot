from aiogram import types
from loader import bot, dp, gm
from objects import *


@dp.message_handler(commands=['leave'], chat_type=['group', 'supergroup'])
async def leave_handler(message: types.Message):
    ''' Leave in a game '''
    user = types.User.get_current()
    chat = types.Chat.get_current()

    try:
        game = gm.get_game_from_chat(chat)
    except NoGameInChatError:
        await message.answer('В этом чате нет игры!!\nСоздайте её при помощи - /new')
        return
    
    player = gm.player_for_user(user)

    if player is None:
        await message.answer('Вы не играете!')
        return
    
    try:
        # kick player
        await gm.leave_player(player)
    except NotEnoughPlayersError:
        gm.end_game(chat)
        await message.answer('Игра завершена!')
    else:
        if game.started:
            await message.answer(f'Хорошо, ходит игрок {game.current_player}')
        else:
            await message.answer(f'({user.get_mention(as_html=True)}) - Покинул лобби!')