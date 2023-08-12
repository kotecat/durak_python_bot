from aiogram import types

from loader import bot, dp, gm, CHOISE
from objects import *
from logic import actions


async def send_cheat_att(player: Player):
    chat = player.game.chat
    user = player.user
    await bot.send_message(
            chat.id,
            text = f"Попытка считерить {user.get_mention(as_html=True)}"
        )


@dp.chosen_inline_handler()
async def result_handler(query: types.ChosenInlineResult):
    ''' Inline process '''
    user = types.User.get_current()
    player = gm.player_for_user(user)

    if player is None:
        return


    game = player.game
    field_old = game.field
    result_id = query.result_id
    chat = game.chat

    if result_id in ('hand', 'gameinfo', 'nogame'):
        return

    result_id, anti_cheat = result_id.split(':')
    split_result_id = result_id.split('-')
    last_anti_cheat = player.anti_cheat
    player.anti_cheat += 1

    current = game.current_player
    opponent = game.opponent_player


    if result_id.startswith('mode_'):
        # First 5 characters are 'mode_', the rest is the gamemode.
        mode = result_id[5:]
        return
    
    elif len(result_id) == 36:  # UUID result
        return
    
    elif int(anti_cheat) != last_anti_cheat:
        # cheat attempt
        await send_cheat_att(player)
        return
    
    elif result_id == 'draw':
        await actions.do_draw(player)

    elif result_id == 'pass':
        await actions.do_pass(player)
    
    elif len(split_result_id) == 1:  # ATK
        try:
            atk_card = c.from_str(split_result_id[0])
        except:
            return
        else:
            # opponent.anti_cheat += 1
            if game.allow_atack:
                await actions.do_attack_card(player, atk_card)
            else:
                await send_cheat_att(player)
                return

    elif len(split_result_id) == 2:  # DEF
        try:
            atk_card = c.from_str(split_result_id[0])
            def_card = c.from_str(split_result_id[1])
        except:
            return
        else:
            # current.anti_cheat += 1
            await actions.do_defence_card(player, atk_card, def_card)
    
    else:
        return
    
    try:
        gm.get_game_from_chat(chat)
    except NoGameInChatError:
        return
    else:
        if game.started:
            

            if game.current_player != current:
                text = f'Преход хода!\n\nАтакует: {game.current_player.user.get_mention(as_html=True)}\nЗащищается: {game.opponent_player.user.get_mention(as_html=True)}'
                await bot.send_message(chat.id, text, reply_markup=types.InlineKeyboardMarkup(inline_keyboard=CHOISE))
            else:
                if game.field != field_old:
                    if game.current_player == current:
                        text = f'Хорошо, Ход остаётся у: {game.current_player.user.get_mention(as_html=True)}\nЗащищается: {game.opponent_player.user.get_mention(as_html=True)}'
                    else:
                        text = f'Хорошо, переход хода!\n\nАтакует: {game.current_player.user.get_mention(as_html=True)}\nЗащищается: {game.opponent_player.user.get_mention(as_html=True)}'

                    await bot.send_message(chat.id, text, reply_markup=types.InlineKeyboardMarkup(inline_keyboard=CHOISE))