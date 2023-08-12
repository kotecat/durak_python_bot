from objects import *
from db import UserSetting, session

from aiogram import types, Bot
from typing import Dict, List, Union


class GameManager:
    def __init__(self) -> None:
        self.games: Dict[int, Game] = dict()
        self.notify: Dict[int, List[int]] = list()

    
    def new_game(self, chat: types.Chat, creator: types.User) -> Game:
        """
        errors:

        - GameAlreadyInChatError
        """
        if self.games.get(chat.id, None) is not None:
            raise GameAlreadyInChatError
        
        game = Game(chat, creator)
        self.games[chat.id] = game
        return game
    

    def get_game_from_chat(self, chat: types.Chat) -> Game:
        """errors:

        - NoGameInChatError
        """
        game = self.games.get(chat.id, None)

        if game is not None:
            return game
        raise NoGameInChatError
    

    def end_game(self, target: Union[types.Chat, Game]) -> None:
        """errors:

        - NoGameInChatError
        """
        if isinstance(target, types.Chat):
            chat = target
        else:
            chat = target.chat
        
        game = self.games.get(target.id, None)
        if game is not None:
            players = game.players
            
            for pl in players:
                # stats
                with session as s:
                    user = pl.user
                    us = UserSetting.get(id=user.id)
                    if not us:
                        us = UserSetting(id=user.id)

                    if us.stats:
                        us.games_played += 1
            
            del self.games[target.id]
            return
        raise NoGameInChatError

        # else:
        #     for chat_id, game_ in self.games.items():
        #         if target == game_:
        #             del self.games[chat_id]
        #             return
        #     raise NoGameInChatError
        

    def join_in_game(self, game: Game, user: types.User) -> None:
        """
        errors:

        - GameStartedError
        - LobbyClosedError
        - LimitPlayersInGameError
        - AlreadyJoinedError
        """
        if game.started:
            raise GameStartedError
        if not game.open:
            raise LobbyClosedError
        if len(game.players) >= game.MAX_PLAYERS:
            raise LimitPlayersInGameError
        
        for _player in game.players:
            if user == _player.user:
                raise AlreadyJoinedError
        
        if self.check_user_ex_in_all_games(user):
            raise AlreadyJoinedInGlobalError

        player = Player(game, user)
        game.players.append(player)

        return
        

    def start_game(self, game: Game) -> None:
        """
        errors:

        - GameStartedError
        - NotEnoughPlayersError
        """
        if game.started:
            raise GameStartedError
        if len(game.players) <= 1:
            raise NotEnoughPlayersError
        game.start()
        

    def player_for_user(self, user: types.User) -> Player | None:
        for game in self.games.values():
            for player in game.players:
                if player.user == user:
                    return player
        
        return None
    

    def check_user_ex_in_all_games(self, user: types.User) -> bool:
        """
        True - exist
        False - not exist
        """
        for game in self.games.values():
            for player in game.players:
                if player.user.id == user.id:
                    return True
        
        return False