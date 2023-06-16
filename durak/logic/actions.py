from objects import *
from loader import gm
from db import UserSetting, session
from aiogram import types, Bot


async def do_turn(game: Game, skip_def: bool = False):
    """errors:
    ...
    """
    game.turn(skip_def=skip_def)
    chat = game.chat
    bot = Bot.get_current()

    for pl in game.players:
        if pl.cards:
            continue
        # Win ▼
        if not game.winner:
            # First
            # satistic
            with session as s:
                user = pl.user
                us = UserSetting.get(id=user.id)
                if not us:
                    us = UserSetting(id=user.id)

                if us.stats:
                    us.first_places += 1  # first winner
                    us.games_played += 1
                
            game.winner = pl
            await bot.send_message(chat.id, f'({pl.user.get_mention(as_html=True)}) - Первый победитель!')
        else:
            # stats
            with session as s:
                user = pl.user
                us = UserSetting.get(id=user.id)
                if not us:
                    us = UserSetting(id=user.id)

                if us.stats:
                    us.games_played += 1
                    
            await bot.send_message(chat.id, f'({pl.user.get_mention(as_html=True)}) - Побеждает!')

        try:
            await do_leave_player(pl)
        except NotEnoughPlayersError:
            gm.end_game(game.chat)

        try:
            game = gm.get_game_from_chat(chat)
        except NoGameInChatError:
            await bot.send_message(chat.id, 'Игра завершена!')

    
async def do_leave_player(player: Player):
    """errors:

    - NotEnoughPlayersError
    """
    game = player.game

    if not game.started:
        game.players.remove(player)
        return
    
    index = game.players.index(player)

    current = game.current_player
    opponent = game.opponent_player
    attacker_id = game.attacker_index

    if player in [current, opponent]:
        game._clear_field()

    game.players.remove(player)
    if not (player in [current, opponent] or index > attacker_id+1):
        game.attacker_index = (game.attacker_index + 1) % len(game.players)

    if len(game.players) <= 1:
        raise NotEnoughPlayersError
    
    if player in [current, opponent]:
        await do_turn(game)


async def do_pass(player: Player):
    game = player.game
    game.is_pass = True

    if game.all_beaten_cards:
        await do_turn(game)


async def do_draw(player: Player):
    game = player.game
    game.take_all_field()
    await do_turn(game, True)


async def do_attack_card(player: Player, card: Card):
    player.play_attack(card)
    game = player.game
    user = player.user
    
    # stats
    with session:
        us = UserSetting.get(id=user.id)
        if not us:
            us = UserSetting(id=user.id)
        if us.stats:
            us.cards_played += 1
            us.cards_atack += 1

    if (not player.cards) or not (game.allow_atack):
        """ Auto Pass """
        game.is_pass = True
        
        # play last card in a game
        if len(game.players) <= 2:
            if (not player.cards) and (not game.deck.cards):
                await do_turn(game)  # -> end game

            
async def do_defence_card(player: Player, atk_card: Card, def_card: Card):
    player.play_defence(atk_card, def_card)
    game = player.game
    user = player.user
    
    # stats
    with session:
        us = UserSetting.get(id=user.id)
        if not us:
            us = UserSetting(id=user.id)
        
        if us.stats:
            us.cards_played += 1
            us.cards_beaten += 1
    
    if not player.cards:
        game.is_pass = True
        
    if game.all_beaten_cards:
        if game.is_pass:
            await do_turn(game)