from fastapi import Depends

from schemas.search import Player,PlayerBase
from repository.search import PlayerRepository

class PlayerService():
    def __init__(self, repository: PlayerRepository = Depends()) -> None:
        self.repository = repository

    def get_player(self, player_id: str) -> PlayerBase:
        return self.repository.get_player(player_id)