class DeckEmptyError(Exception):
    pass


class NoGameInChatError(Exception):
    pass


class AlreadyJoinedError(Exception):
    pass


class AlreadyJoinedInGlobalError(Exception):
    pass


class LobbyClosedError(Exception):
    pass


class NotEnoughPlayersError(Exception):
    pass


class GameAlreadyInChatError(Exception):
    pass


class LimitPlayersInGameError(Exception):
    pass


class GameStartedError(Exception):
    pass