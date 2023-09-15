from datetime import datetime
from aiogram import types
from typing import Any, List, Dict, Optional
import logging

from . import card as c
from .deck import Deck
from .player import Player
from .card import Card

from config import Config


class Game:
    """ This is Game """

    def __init__(self, chat: types.Chat, creator: types.User) -> None:
        self.chat: types.Chat = chat
        self.deck: Deck = Deck()
        self.field: Dict[Card, Optional[Card]] = dict()
        self.trump: c.Suits = None
        self.players: List[Player] = list()
        self.started: bool = False
        self.creator: types.User = creator
        self.open: bool = True
        self.mode: str = Config.DEFAULT_GAMEMODE  # "p"

        self.attacker_index: int = 0
        self.winner: Player | None = None
        self.is_pass: bool = False  # Atack player is PASS
        self.is_final: bool = False

        self.COUNT_CARDS_IN_START: int = Config.COUNT_CARDS_IN_START
        self.MAX_PLAYERS: int = Config.MAX_PLAYERS
        self.logger = logging.getLogger(__name__)


    def start(self):
        self.deck._fill_cards()
        self.trump = self.deck.trump
        self.started = True
        self.take_cards_from_deck()


    def rotate_players(self, list: List[Player], index: int) -> List[Player]:
        return list[index:] + list[:index]
    

    @property
    def attacking_cards(self) -> List[Card]:
        """ List attacking cards """
        return list(filter(bool, self.field.keys()))
    

    @property
    def defending_cards(self) -> List[Card]:
        """ List defending cards (filter None) """
        return list(filter(bool, self.field.values()))
    

    @property
    def any_unbeaten_card(self) -> bool:
        """ exist unbeaten card """
        return any(c is None for c in self.field.values())
    

    @property
    def all_beaten_cards(self) -> bool:
        return all(c is not None for c in self.field.values())
    

    @property
    def current_player(self) -> Player:
        return self.players[self.attacker_index]    


    @property
    def opponent_player(self) -> Player:
        return self.players[(self.attacker_index + 1) % len(self.players)]
    
    
    @property
    def support_player(self) -> Player:
        return self.players[(self.attacker_index + 2) % len(self.players)]
    

    @property
    def allow_atack(self) -> bool:
        return len(self.attacking_cards) < self.COUNT_CARDS_IN_START and \
            len(self.defending_cards)+len(self.opponent_player.cards) > len(self.attacking_cards)
    
    
    def attack(self, card: Card) -> None:
        cur, opp = self.current_player, self.opponent_player
        self.field[card] = None
        return
    

    def defend(self, attacking_card: Card, defending_card: Card) -> None:
        cur, opp = self.current_player, self.opponent_player
        self.field[attacking_card] = defending_card
        return
    

    def _clear_field(self) -> None:
        for atk_card, def_card in self.field.items():
            self.deck.dismiss(atk_card)
            self.deck.dismiss(def_card)
        self.field = dict()


    def take_all_field(self)-> None:
        """ Opponent take all cards from table. """
        cards = self.attacking_cards + self.defending_cards
        self.opponent_player.add_cards(cards)
        self._clear_field()
        return
    

    def take_cards_from_deck(self) -> None:
        players = self.rotate_players(self.players, self.attacker_index)
        for player in players:
            player.draw_cards_from_deck()
        return


    def turn(self, skip_def: bool = False) -> None:
        self.logger.debug("Next Player")
        self.attacker_index = (self.attacker_index + 1 + skip_def) % len(self.players)
        self.is_pass = False
        self._clear_field()
        self.take_cards_from_deck()  # every player add cards to hand
        self.current_player.turn_started = datetime.now()