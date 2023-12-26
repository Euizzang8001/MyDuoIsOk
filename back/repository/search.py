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

    def get_player(self, player_id: str) -> Player:
        # player = self.get_player_in_db(player_id = player_id)
        player = player_id
        if player:
            player_id = player.replace('','%20')
            request_url = f'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{player_id}'
            player_info = requests.get(request_url)
            return player_info
        else:
            True