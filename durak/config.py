from dataclasses import dataclass


@dataclass
class Config:
    TOKEN: str = ''
    WAITING_TIME: int = 120