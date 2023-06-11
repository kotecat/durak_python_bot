from objects import *
from loader import gm, bot, dp, Config
from logic.utils import user_is_bot_admin, user_is_creator, user_is_creator_or_admin

from logic import actions
from logic import result as r

from typing import List
from aiogram import Bot, types, executor
from aiogram.dispatcher.filters import ChatTypeFilter
from contextlib import suppress
from pprint import pprint
import logging


logging.basicConfig(level=logging.INFO)
CHOISE = [[types.InlineKeyboardButton(text='Выбери карту!', switch_inline_query_current_chat='')]]


@dp.message_handler(commands=['help'])
async def help_handler(message: types.Message):
    await message.answer('help')



# THIS CODE IS TEMPORARY ▼ ▼ ▼
@dp.message_handler(commands=['status'], chat_type=['group', 'supergroup'])
async def status_handler(message: types.Message):
    user = types.User.get_current()
    chat = types.Chat.get_current()

    player = gm.player_for_user(user)

    if player is None:
        return
    
    game = player.game

    for pl in game.players:
        print(f'{pl.cards}   {pl.user.first_name}')

    # print(game)
    print()
    # print(f'players: {game.players}')
    print(f'deck: {game.deck.cards}')
    print()
    print(f'started: {game.started}    pass: {game.is_pass}    trump: {game.trump}')
    print()
    print(f'atacker: {game.current_player.user.first_name}   defender: {game.opponent_player.user.first_name}')
    pprint(f'field: {game.field}')
    pprint(f'field: {game.defending_cards}')
    print()
    print()
# THIS CODE IS TEMPORARY ▲ ▲ ▲



@dp.message_handler(commands=['new'], chat_type=['group', 'supergroup'])
async def new_handler(message: types.Message):
    ''' Creating new game '''
    user = types.User.get_current()
    chat = types.Chat.get_current()

    try:
        # create
        game = gm.new_game(chat, creator=user)
    except GameAlreadyInChatError:
        await message.answer('В этом чате уже есть игра')
        return
    
    await message.answer('Запустил!\n/join')



@dp.message_handler(commands=['join'], chat_type=['group', 'supergroup'])
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



@dp.message_handler(commands=['gleave'], chat_type=['group', 'supergroup'])
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
        # kick player
        await gm.leave_player(player)
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



@dp.message_handler(content_types=[types.ContentTypes.LEFT_CHAT_MEMBER], chat_type=['group', 'supergroup'])
async def auto_leave_handler(message: types.Message):
    ''' Automatic kick players (left from the group) '''
    user = message.left_chat_member
    chat = types.Chat.get_current()

    if not user:
        return
    
    try:
        game = gm.get_game_from_chat(chat)
    except NoGameInChatError:
        return
    
    mention = user.get_mention(as_html=True)
    player = gm.player_for_user(user)

    if player is None:
        return
    
    if player.game != game:
        return

    try:
        # kick player
        await gm.leave_player(player)
    except NotEnoughPlayersError:
        gm.end_game(chat)
        await bot.send_message(chat.id, f'({mention}) - Покинул игру!')
        await bot.send_message(chat.id, 'Игра завершена!\n')
    else:
        if game.started:
            await bot.send_message(chat.id, f'({mention}) - Покинул игру\nХодит игрок {game.current_player}')
        else:
            await bot.send_message(chat.id, f'({mention}) - Покинул лобби!')



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



@dp.message_handler(commands=['kill'], chat_type=['group', 'supergroup'])
async def start_handler(message: types.Message):
    ''' Kill a game '''
    user = types.User.get_current()
    chat = types.Chat.get_current()

    try:
        game = gm.get_game_from_chat(chat)
    except NoGameInChatError:
        await message.answer('В этом чате нет игры!!\nСоздайте её при помощи - /new')
        return
    
    mention = user.get_mention(as_html=True)

    if (await user_is_creator_or_admin(user, game, chat)):
        # game end
        gm.end_game(chat)
        await message.answer(f'{mention} Завершил игру!')
        return
    else:
        await message.answer('Вы не можете завершить игру!')
        return



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
        await bot.send_message(
            chat.id,
            text = f"Попытка считерить {player.user.get_mention(as_html=True)}"
        )
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
            await actions.do_attack_card(player, atk_card)

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

    await status_handler(query)


if __name__ == "__main__":
    executor.start_polling(dp)