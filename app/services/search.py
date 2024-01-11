from fastapi import Depends

from repository.search import SummonerRepository
from models.search import MatchInfoBase, SummonerBase
import json

class SummonerService():
    def __init__(self, repository: SummonerRepository = Depends()) -> None:
        self.repository = repository

    def get_summoner_puuid(self, summoner:str) -> str:
        summoner_puuid = self.repository.get_summoner_puuid(summoner_name = summoner)
        return summoner_puuid
    
    def get_players_match(self, summoner: str) -> list:
        summoner = self.repository.get_summoner_puuid(summoner_name = summoner)
        summoner_puuid = summoner
        match_list = self.repository.get_summoner_match(puuid = summoner_puuid)
        return match_list
    
    def get_match(self, puuid:str):
        match_list = self.repository.get_summoner_match(puuid = puuid)
        return match_list
    
    def get_match_info(self, match_id: str):
        match_info= self.repository.get_match_info(match_id=match_id)
        return match_info
    
    def append_match_info(self, match_info: MatchInfoBase):
        match_info = self.repository.append_match_info(match_info)
        return match_info

    def append_summoner_info(self, puuid: str, summoner_info : SummonerBase):
        summoner_info = self.repository.append_summoner_info(puuid = puuid, summoner_dto=summoner_info)
        return summoner_info
    
    def delete_match_info(self, match_id: str):
        match_delete = self.repository.delete_match_info(match_id = match_id)
        return match_delete
    
    def delete_summoner_match_info(self, match_id: str, puuid: str):
        result = self.repository.delete_summoner_match_info(match_id = match_id, puuid = puuid)
        return result
    
    def check_match_in_db(self, match_id : str):
        result = self.repository.check_match_in_db(match_id = match_id)
        if result == True:
            return True
        return False
    
    def get_summoner_from_db(self, puuid: str, match_id: str):
        result = self.repository.get_summoner_from_db(puuid = puuid, match_id = match_id)
        return result
    
    def get_match_from_db(self, match_id: str):
        result = self.repository.get_match_from_db(match_id = match_id)
        return result
    
