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

apikey="RGAPI-626d57b2-73d2-463a-9252-5d3b2f413799"

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
    
    # def get_player__in db

    def get_player_account(self, player_name: str) -> PlayerBase:
        # player = self.get_player_in_db(player_id = player_id)
        player = player_name
        if player:
            player = player.replace('','%20')
            request_url = f'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{player}'
            result = requests.get(request_url, headers=headers)
            player_info = result.json()
            return player_info
        else:
            True
    
    def get_player_match(self, player_name = str) -> PlayerBase:
        player_account = self.get_player_account(player_name = player_name)
        player_account = player_account.json()
        requests_url = f"https://kr.api.riotgames.com/lol/match/v5/matches/by-puuid/{player_account['puuid']}/ids"
        result = requests.get(requests_url, headers=headers)
        player_match_info = result.json()
        return player_match_info

    def get_match_info(self, match_id = str):
        requests_url = f"https://kr.api.riotgames.com/lol/match/v5/matches/{match_id}"
        result = requests.get(requests_url, headers=headers)
        match_info = result.json()
        return match_info
    
    def player_match_data(self, player_id = list, match_id = str):
        match_info = self.get_match_info(match_id)
        if match_info['info']['gameMode'] != 'CLASSIC':
            return {'Not Classic'}
        for summoner in match_info['info']['participants']:
            

    