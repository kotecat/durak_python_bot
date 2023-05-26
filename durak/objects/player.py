import logging
import typing
from datetime import datetime
from aiogram import types
from typing import List

from . import card as c
from .errors import (DeckEmptyError)

from config import Config


if typing.TYPE_CHECKING:
    from .game import Game
    from .card import Card


class Player:
    """ This is Player"""

    def __init__(self, game: Game, user: types.User) -> None:
        self.user: types.User = user  # User obj | from Aiogram
        self.game: Game = game  # Game obj
        self.cards: List[Card] = list()
        self.logger = logging.getLogger(__name__)
        self.anti_cheat: int = 0
        self.turn_started: datetime = datetime.now()
        self.waiting_time: int = Config.WAITING_TIME


    def draw_cards_from_deck(self):
        """ Take the missing number of cards from the deck
         The deck will shrink :> """

        lack = max(0, self.game.COUNT_CARDS_IN_START - len(self.cards))
        n = min(len(self.game.deck), lack)

        cards: List[card] = list()
        
        for _ in range(n):
            try:
                card = self.game.deck.draw()
            except DeckEmptyError:
                self.logger.warning(f'DeckEmptyError')
                return

            else:
                cards.append(self.game.deck.draw())

        self.add_cards(cards)


    def add_cards(self, cards: List[Card]):
        """ Add cards in hands """
        self.cards += cards


    def leave(self):
        """ Cleaning self (Cards) """

        for card in self.cards:
            self.game.deck.dismiss(card)

        self.cards.clear()


    def play_attack(self, card: Card):
        """ Plays a card and removes it from hand """
        self.remove_card(card)
        self.game.attack(card)


    def play_defence(self, attacking_card: Card, defending_card: Card):
        self.remove_card(defending_card)
        self.game.defence(attacking_card, defending_card)
    

    def remove_card(self, card: Card):
        self.cards.remove(card)

    def __repr__(self) -> str:
        return repr(self.user)
    

    def __str__(self) -> str:
        return str(self.user)