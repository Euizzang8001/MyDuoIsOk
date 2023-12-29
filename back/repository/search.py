from typing import List
from fastapi import Depends, HTTPException
import requests
from pymongo import MongoClient
from config.databases import db
from models.search import MatchInfoBase, SummonerBase

apikey="RGAPI-ad16881b-b5b8-440c-849e-cafcfe62ae9d"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",    
    "X-Riot-Token": apikey
}

class SummonerRepository():
    def __init__(self) -> None:
        self.db = db

    def get_summoner_puuid(self, summoner_name: str) -> str: #player_name -> player의 계정 정보 return
        summoner = summoner_name
        summoner = summoner.replace('','%20')
        request_url = f'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner}'
        result = requests.get(request_url, headers=headers)
        result.raise_for_status()
        summoner_account = result.json()
        return summoner_account['puuid']
    
    def get_summoner_match(self, puuid: str) -> List[str]: #player_name -> player의 match_id return
        requests_url = f"https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start={1}&count={100}"
        result = requests.get(requests_url, headers=headers)
        result.raise_for_status()
        match_id = result.json()
        return match_id 

    def get_match_info(self, match_id: str): #match_id -> match_info return
        requests_url = f"https://asia.api.riotgames.com/lol/match/v5/matches/{match_id}"
        result = requests.get(requests_url, headers=headers)
        match_info = result.json()
        return match_info
    
    def append_match_info(self, match_info_dto: MatchInfoBase): #match_info_dto를 받아서 match collection에 저장
        collection_name = self.db["match"]
        collection_name.insert_one(dict(match_info_dto))
        return {'success'}
        
        
    def append_summoner_info(self, puuid: str, summoner_dto: SummonerBase): 
        collection_name = self.db[f"{puuid}"]
        collection_name.insert_one(dict(summoner_dto))
        return {'success'}



