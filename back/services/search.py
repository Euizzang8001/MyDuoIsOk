from fastapi import Depends

from schemas.search import MatchBase, Summoner, SummonerBase
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
    
    def get_match_info(self, match_id: str):
#match 정보를 불러오고
        match_info= self.repository.get_match_info(match_id=match_id)
        return match_info   