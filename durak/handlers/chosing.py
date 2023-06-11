from aiogram import types
from typing import List

from loader import bot, dp, gm, CHOISE
from objects import *
from logic import result as r


@dp.inline_handler()
async def inline_handler(query: types.InlineQuery):
    ''' Inline handler :> '''
    user = types.User.get_current()
    text = query.query or ''
    player = gm.player_for_user(user)
    result: List[types.InlineQueryResult] = []
    if player is None:
        # not playing
        r.add_no_game(result)
    else:

        game = player.game

        if not game.started:
            # game not started
            r.add_not_started(result)
        else:
        
            playable = []  # playable cards 

            if player == game.current_player:
                # player is ATK
                if not game.is_pass:
                    r.add_pass(result, game)
                playable = player.playable_card_atk()
                playable.sort()

                for card_ in player.cards:
                    r.add_card(game, card_, result, (card_ in playable))
                
            elif player == game.opponent_player:
                # player is DEF
                if game.field and not game.all_beaten_cards:
                    r.add_draw(player, result)
                try:
                    card = c.from_str(text)
                except:
                    for card_ in player.cards:
                        r.add_card(game, None, result, False, card_)
                else:
                    if card in game.attacking_cards:
                        if game.field.get(card) is None:
                            playable = player.playable_card_def(c.from_str(text))
                            playable.sort()

                    for card_ in player.cards:
                        r.add_card(game, card, result, (card_ in playable), card_)

            r.add_gameinfo(game, result)

        for res in result:
            res.id += ':%d' % player.anti_cheat

    await query.answer(result, cache_time=0)
    return