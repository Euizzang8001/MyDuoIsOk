from typing import List, Optional
from fastapi import Depends
from sqlalchemy.orm import Session
import uuid
from fastapi import HTTPException
import requests
import urllib
import json
import datetime
import time
from config.database import get_db
from models.search import Player as PlayerModel
from schemas.search import Player, PlayerBase
from datetime import date

apikey="RGAPI-e32e0ce6-8c85-4616-a907-4934dc1560b5"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": apikey
}

class PlayerRepository():
    def __init__(self, db: Session = Depends(get_db)) -> None : 
        self.db = db

    def get_player_puuid(self, player_name: str): #player_name -> player의 계정 정보 return
        player = player_name
        player = player.replace('','%20')
        request_url = f'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{player}'
        result = requests.get(request_url, headers=headers)
        result.raise_for_status()
        player_account = result.json()
        return player_account['puuid']
    
    def get_player_match(self, puuid: str) -> List[str]: #player_name -> player의 match_id return
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