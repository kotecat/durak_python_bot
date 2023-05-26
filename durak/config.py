from dataclasses import dataclass


@dataclass
class Config:
    TOKEN: str = ''
    
    WAITING_TIME: int = 120
    MAX_PLAYERS = 6
    COUNT_CARDS_IN_START = 6