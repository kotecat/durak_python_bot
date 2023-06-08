from __future__ import annotations
from datetime import datetime
from time import time
from aiogram import types
from typing import List, Optional

import logging
import typing

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
        self.anti_cheat: int = int(time())
        self.turn_started: datetime = datetime.now()
        self.waiting_time: int = Config.WAITING_TIME


    def draw_cards_from_deck(self):
        """ Take the missing number of cards from the deck
         The deck will shrink :> """

        lack = max(0, self.game.COUNT_CARDS_IN_START - len(self.cards))
        n = min(len(self.game.deck.cards), lack)

        cards: List[card] = list()
        
        for _ in range(n):
            try:
                card = self.game.deck.draw()
            except DeckEmptyError:
                self.logger.warning(f'DeckEmptyError')
                break

            else:
                cards.append(card)

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
        self.game.defend(attacking_card, defending_card)
    

    def playable_card_atk(self) -> List[Card]:
        playable: List[Card] = []
        game = self.game

        for card in self.cards:
            if not game.allow_atack:
                return []
            if self.can_add_to_field(card):
                playable.append(card)

        return playable
    

    def playable_card_def(self, atk_card: Optional[Card] = None) -> List[Card]:
        playable: List[Card] = []
        game = self.game

        for card in self.cards:
            if self.can_beat(atk_card, card):
                playable.append(card)

        return playable


    def card_match(self, card_1: Card, card_2: Card) -> bool:
        if card_1 is None or card_2 is None:
            return False
        return card_1.value == card_2.value
    

    def can_add_to_field(self, card: Card):
        field = self.game.field

        if not field:
            return True
        
        for atk_card, def_card in field.items():
            if self.card_match(atk_card, card) or \
                self.card_match(def_card, card):
                return True
        return False


    def can_beat(self, atk_card: Card, def_card: Card) -> bool:
        if def_card.suit == self.game.trump:
            return ( atk_card.suit != self.game.trump ) or ( int(def_card.value) > int(atk_card.value) )
        
        elif ( def_card.suit == atk_card.suit ):
            return int(def_card.value) > int(atk_card.value)
        
        else:
            return False


    def remove_card(self, card: Card):
        self.cards.remove(card)

    def __repr__(self) -> str:
        return repr(self.user)
    

    def __str__(self) -> str:
        return str(self.user)