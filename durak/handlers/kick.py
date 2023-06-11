from aiogram import types
from loader import bot, dp, gm
from objects import *
from logic.utils import (
    user_is_admin,
    user_is_creator,
    user_is_bot_admin,
    user_is_creator_or_admin
)


@dp.message_handler(commands=['kick'], chat_type=['group', 'supergroup'])
async def kick_handler(message: types.Message):
    ''' Kick user in a game '''
    reply = message.reply_to_message
    if not reply:
        return
    
    _from_user = types.User.get_current()   # User who kicks out
    _to_user = reply.from_user              # User who is being kicked out
    chat = types.Chat.get_current()

    try:
        game = gm.get_game_from_chat(chat)
    except NoGameInChatError:
        await message.answer('В этом чате нет игры!!\nСоздайте её при помощи - /new')
        return
    
    _from_player = gm.player_for_user(_from_user)   # Player who kicks out
    _to_player = gm.player_for_user(_to_user)       # Player who is being kicked out

    if _from_player is None:
        if not (await user_is_creator_or_admin(_from_user, game, chat)):
            await message.reply('Вы не можете кикнуть этого игрока!')
            return
    else:
        if _from_player.game != game:
            await message.reply('Вы не можете кикнуть этого игрока!')
            return
    
    if _to_player is None:
        await message.reply('Данный пользователь не играет!')
        return
    
    if _to_player.game != game:
        await message.reply('Данный игрок не играет в этом чате!')
        return
    
    try:
        # kick player
        await gm.leave_player(_to_player)
    except NotEnoughPlayersError:
        gm.end_game(chat)
        await message.answer('Игра завершена!')
    else:
        if game.started:
            await message.answer(f'Хорошо, ходит игрок {game.current_player}')
        else:
            await message.answer(f'({_to_user.get_mention(as_html=True)}) был кикнут игроком - {_from_user.get_mention(as_html=True)}!')