from pony.orm import Optional, PrimaryKey
from .database import db
from .database import session


class UserSetting(db.Entity):

    id = PrimaryKey(int, auto=False, size=64)  # Telegram User ID
    stats = Optional(bool, default=True)  # Opt-in to keep game statistics
    first_places = Optional(int, default=0)  # Nr. of games won in first place
    games_played = Optional(int, default=0)  # Nr. of games completed
    cards_played = Optional(int, default=0)  # Nr. of cards played total
    cards_beaten = Optional(int, default=0)  # Nr. of cards beaten total
    cards_atack = Optional(int, default=0)  # Nr. of cards atack total