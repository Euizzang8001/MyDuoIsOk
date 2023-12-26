from fastapi import Depends

from schemas.search import Player,PlayerBase
from repository.search import PlayerRepository
import json

class PlayerService():
    def __init__(self, repository: PlayerRepository = Depends()) -> None:
        self.repository = repository

    def get_player_puuid(self, player:str) -> str:
        player_puuid = self.repository.get_player_puuid(player_name = player)
        return player_puuid
    
    def get_players_match(self, player: str) -> list:
        summoner = self.repository.get_player_puuid(player_name = player)
        player_puuid = summoner
        match_list = self.repository.get_player_match(puuid = player_puuid)
        return match_list
    
    def get_match(self, puuid:str):
        match_list = self.repository.get_player_match(puuid = puuid)
        return match_list
    
    def get_player_info_per_match(self, player: str, match_id: str):
        player_info_per_match= self.repository.player_in_match_data(player_puuid=player, match_id=match_id)
        return player_info_per_match