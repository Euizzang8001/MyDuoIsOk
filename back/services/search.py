from fastapi import Depends

from schemas.search import MatchInfoBase, Summoner, SummonerBase
from repository.search import SummonerRepository
import json

class SummonerService():
    def __init__(self, repository: SummonerRepository = Depends()) -> None:
        self.repository = repository

    def get_summoner_puuid(self, summoner:str) -> str:
        summoner_puuid = self.repository.get_summoner_puuid(summoner_name = summoner)
        return summoner_puuid
    
    def get_players_match(self, player: str) -> list:
        summoner = self.repository.get_summoner_puuid(summoner_name = summoner)
        summoner_puuid = summoner
        match_list = self.repository.get_summoner_match(puuid = summoner_puuid)
        return match_list
    
    def get_match(self, puuid:str):
        match_list = self.repository.get_summoner_match(puuid = puuid)
        return match_list
    
    def get_match_info(self, match_id: str):
#match 정보를 불러오고
        match_info= self.repository.get_match_info(match_id=match_id)
        return match_info
    
    def append_match_info(self, match_info: MatchInfoBase):
        match_info = self.repository.append_match_info(match_info)
        return match_info

    def append_summoner_info(self, puuid: str, summoner_info : Summoner):
        summoner_info = self.repository.append_summoner_info(puuid = puuid, summoner_dto=summoner_info)
    
    def create_summoner_table(self, puuid: str):
        summoner_info = self.repository.create_new_summoner_table(puuid = puuid)
        return summoner_info
