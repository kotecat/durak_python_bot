from aiogram import types
from aiogram.types import InlineQueryResultArticle, InlineQueryResult, \
                    InlineQueryResultCachedSticker as Sticker, \
                    InputTextMessageContent, InlineKeyboardButton, \
                    InlineKeyboardMarkup
from typing import List
from uuid import uuid4
from config import Commands

from objects import Player, Game, Card, card as c


def add_no_game(results: List[InlineQueryResult]):
    """Add text result if user is not playing"""
    results.append(
        InlineQueryResultArticle(
            id="nogame",
            title = "Вы не играете",
            input_message_content=
            InputTextMessageContent('Вы сейчас не играете. Используйте /new чтобы '
                                    'начать игру или /join, чтобы присоединиться к игре '
                                    'текущая игра в этой группе')
        )
    )


def add_not_started(results: List[InlineQueryResult]):
    """Add text result if the game has not yet started"""
    results.append(
        InlineQueryResultArticle(
            id="nogame",
            title = "Игра еще не началась",
            input_message_content=
            InputTextMessageContent(f'Запустить игру /{Commands.START}')
        )
    )


def add_draw(player: Player, results: List[InlineQueryResult]):
    """Add option to draw"""
    game = player.game
    n = len(game.attacking_cards)+len(game.defending_cards)

    results.append(
        Sticker(
            id="draw", sticker_file_id=c.STICKERS['draw'],
            input_message_content=
            # InputTextMessageContent(f'Взял(а) {n} 🃏')
            InputTextMessageContent("Взял(а) карты!")
        )
    )


def add_gameinfo(game: Game, results: List[InlineQueryResult]):
    """Add option to show game info"""

    results.append(
        Sticker(
            id="gameinfo",
            sticker_file_id=c.STICKERS['info'],
            input_message_content=game_info(game)
        )
    )


def add_pass(results: List[InlineQueryResult], game: Game):
    """Add option to pass"""
    results.append(
        Sticker(
            id="pass", sticker_file_id=c.STICKERS['pass'],
            input_message_content=InputTextMessageContent(
                'Pass'
            )
        )
    )



def add_card(game: Game, atk_card: Card, results: List[InlineQueryResult], can_play: bool, def_card: Card = None):
    """Add an option that represents a card"""

    if can_play:
        id = repr(atk_card)

        if def_card:
            id += f'-{repr(def_card)}'

            results.append(
                Sticker(id=id, sticker_file_id=c.STICKERS['normal'][repr(def_card)],
                    input_message_content=InputTextMessageContent(
                        f"Побил карту {str(atk_card)}, картой {str(def_card)}"
                    )
                )
            )

        else:
            beat = [[InlineKeyboardButton(text='Побить эту карту!', switch_inline_query_current_chat=f'{repr(atk_card)}')]]
            results.append(
                    Sticker(id=id, sticker_file_id=c.STICKERS['normal'][repr(atk_card)],
                        input_message_content=InputTextMessageContent(
                            f"Кинул карту: {str(atk_card)}"
                        ),
                        reply_markup=InlineKeyboardMarkup(inline_keyboard=beat)
                    )
                )
    
    else:
        results.append(
            Sticker(id=str(uuid4()), sticker_file_id=c.STICKERS['grey'][repr(def_card or atk_card)],
                    input_message_content=game_info(game))
        )


def game_info(game: Game):
    players = game.players
    field = game.field
    trump = game.trump
    count_cards_in_deck = len(game.deck.cards)

    pleyers_info = ''.join(f"\n• {len(pl.cards)} 🃏 | {pl.user.get_mention(as_html=True)}" for pl in players)
    
    field_info = ''.join(f'\n  {str(a)} ◄-- {str(d) if not d is None else "❌"}' for a, d in field.items())

    return InputTextMessageContent(
        f"Атакующий: {game.current_player.user.get_mention(as_html=True)}\n"
        f"Отбивающий: {game.opponent_player.user.get_mention(as_html=True)}\n\n"
        f"Козырь: {game.deck.trump_ico}\n"
        f"В колоде: {len(game.deck.cards)}\n\n"
        f"Игроки: {pleyers_info}\n"
        f"Поле: \n{field_info if field else '  тут пусто~'}\n"
    )