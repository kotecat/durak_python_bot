from aiogram import types
from loader import bot, dp, gm, Commands
import durak.logic.actions as a
from durak.objects import *


@dp.message_handler(commands=[Commands.GLEAVE], chat_type=['group', 'supergroup'])
async def leave_handler(message: types.Message):
    ''' Global leave in a game '''
    user = types.User.get_current()
    
    player = gm.player_for_user(user)

    if player is None:
        await message.answer('Вы не играете!')
        return
    
    game = player.game
    mention = user.get_mention(as_html=True)

    try:
        # kick player (leave)
        await a.do_leave_player(player)
    except NotEnoughPlayersError:
        gm.end_game(game.chat)
        await bot.send_message(game.chat.id, f'({mention}) - Покинул игру!')
        await bot.send_message(game.chat.id, 'Игра завершена!\n')
    else:
        if game.started:
            await bot.send_message(game.chat.id, f'({mention}) - Покинул игру\nХодит игрок {game.current_player}')
        else:
            await bot.send_message(game.chat.id, f'({mention}) - Покинул лобби!')
    
    await message.answer(f'({mention}) - Покинул игру в другом чате!')