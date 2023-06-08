from dataclasses import dataclass
from environs import Env
from typing import List, ClassVar


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
    DEFAULT_GAMEMODE = "true_none"  # :>