from objects import *

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
            game = self.games.get(target.id, None)
            if game is not None:
                del self.games[target.id]
                return
            raise NoGameInChatError

        else:
            for chat_id, game_ in self.games.items():
                if target == game_:
                    del self.games[chat_id]
                    return
            raise NoGameInChatError
        

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
    

    async def do_turn(self, game: Game, skip_def: bool = False):
        """errors:
        ...
        """
        game.turn(skip_def=skip_def)
        chat = game.chat
        bot = Bot.get_current()

        for pl in game.players:
            if pl.cards:
                continue
            # Win ▼
            if not game.winner:
                # First
                game.winner = pl
                await bot.send_message(chat.id, f'({pl.user.get_mention(as_html=True)}) - Первый победитель!')
            else:
                await bot.send_message(chat.id, f'({pl.user.get_mention(as_html=True)}) - Побеждает!')

            try:
                await self.leave_player(pl)
            except NotEnoughPlayersError:
                self.end_game(game.chat)

            try:
                game = self.get_game_from_chat(chat)
            except NoGameInChatError:
                await bot.send_message(chat.id, 'Игра завершена!')

    

    async def leave_player(self, player: Player):
        """errors:

        - NotEnoughPlayersError
        """
        game = player.game

        if not game.started:
            game.players.remove(player)
            return
        
        index = game.players.index(player)

        current = game.current_player
        opponent = game.opponent_player
        attacker_id = game.attacker_index

        if player in [current, opponent]:
            game._clear_field()

        game.players.remove(player)
        if not (player in [current, opponent] or index > attacker_id+1):
            game.attacker_index = (game.attacker_index + 1) % len(game.players)

        if len(game.players) <= 1:
            raise NotEnoughPlayersError
        
        if player in [current, opponent]:
            await self.do_turn(game)
        

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