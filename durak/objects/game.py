from .deck import Deck
from .player import Player
from .card import Card
from config import Config
from typing import Any, List


class Game:
    """ This is Game """

    def __init__(self) -> None:
        self.deck: Deck = Deck()
        self.COUNT_CARDS_IN_START: int = Config.COUNT_CARDS_IN_START


    @property
    def rotate_players(list: List[Player], index: int) -> List[Player]:
        return list[index:] + list[:index]