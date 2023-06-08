from objects import *
from aiogram import types, Bot
from loader import gm


do_turn = gm.do_turn


async def do_pass(player: Player):
    game = player.game
    bot = Bot.get_current()
    chat = game.chat
    user = player.user
    game.is_pass = True

    if game.all_beaten_cards:
        await do_turn(game)


async def do_draw(player: Player):
    game = player.game
    chat = game.chat
    user = player.user
    game.take_all_field()
    await do_turn(game, True)


async def do_attack_card(player: Player, card: Card):
    player.play_attack(card)
    game = player.game
    chat = game.chat
    user = player.user

    if (not player.cards) or (len(game.opponent_player.cards) <= 1):
        """ Auto Pass """
        game.is_pass = True

            
async def do_defence_card(player: Player, atk_card: Card, def_card: Card):
    player.play_defence(atk_card, def_card)
    game = player.game
    chat = game.chat
    user = player.user

    if not player.cards:
        game.is_pass = True
        
    if game.all_beaten_cards:
        if game.is_pass:
            await do_turn(game)



"""

        if not game.deck.cards:
            if game.winner is None:
                # First Win
                ...
                return
            # Win
            ...
            return
        
        else:

"""