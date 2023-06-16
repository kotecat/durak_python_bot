from dataclasses import dataclass
from enum import StrEnum
from environs import Env
from typing import List, Tuple, Dict, ClassVar


env = Env()
env.read_env()


BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = list(map(int, env.list("ADMINS")))


@dataclass
class Config:
    BOT_TOKEN: str = BOT_TOKEN
    ADMINS: ClassVar[List[int]] = ADMINS

    WAITING_TIME: int = 120
    MAX_PLAYERS: int = 6
    COUNT_CARDS_IN_START: int = 6
    DEFAULT_GAMEMODE: str = "true_none"  # :> .......
    DEBUG: bool = True
    

class Commands(StrEnum):
    NEW: str = 'new'
    JOIN: str = 'join'
    START: str = 'run'
    LEAVE: str = 'leave'
    GLEAVE: str = 'gleave'
    KICK: str = 'kick'
    KILL: str = 'kill'
    HELP: str = 'help'
    STATS: str = 'stats'
    SOURCE: str = 'source'
    

COMMANDS: List = [
    (Commands.NEW, 'Создать новую игру'),
    (Commands.JOIN, 'Присоедениться к игре'),
    (Commands.START, 'Запустить игру'),
    (Commands.LEAVE, 'Покинуть игру или лобби'),
    (Commands.GLEAVE, 'Покинуть игру во всех чатах'),
    (Commands.KICK, 'Выгнать игрока'),
    (Commands.KILL, 'Завершить игру'),
    (Commands.HELP, 'Помощь по боту'),
    (Commands.STATS, 'Ваша статистика'),
    (Commands.SOURCE, 'Исходный код')
]