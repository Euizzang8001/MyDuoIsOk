from typing import List
from fastapi import Depends, HTTPException
import requests
from pymongo import MongoClient
from config.databases import db
from models.search import MatchInfoBase, SummonerBase
from dotenv import load_dotenv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))
apikey = os.environ["API_KEY"]


headers = {
    "User-Agent": os.environ["USER_AGENT"],
    "Accept-Language": os.environ["ACCEPT_LANGUAGE"],
    "Accept-Charset": os.environ["ACCEPT_CHARSET"],
    "Origin": os.environ["ORIGIN"], 
    "X-Riot-Token": apikey
}

class SummonerRepository():
    def __init__(self) -> None:
        self.db = db

    def get_summoner_puuid(self, summoner_name: str) -> str: #player_name -> player의 계정 정보 return
        summoner = summoner_name
        #del계정
        if summoner[8:] != 'del':
            summoner = summoner.replace('','%20')
        request_url = f'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner}'
        result = requests.get(request_url, headers=headers)
        result.raise_for_status()
        summoner_account = result.json()
        return summoner_account['puuid']
    
    def get_summoner_match(self, puuid: str) -> List[str]: #player_name -> player의 match_id return
        requests_url = f"https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start={0}&count={100}"
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
        result = collection_name.insert_one(dict(match_info_dto))
        if result:
            return {'success': True}
        else:
            return {'success': False}
        
        
    def append_summoner_info(self, puuid: str, summoner_dto: SummonerBase): 
        collection_name = self.db[puuid]
        result = collection_name.insert_one(dict(summoner_dto))
        if result:
            return {'success': True}
        else:
            return {'success': False}

    def delete_match_info(self, match_id: str):
        collection_name = self.db['match']
        result = collection_name.find_one_and_delete({"matchId": match_id})
        if result:
            return {'success': True}
        else:
            return {'success': False, 'message': 'Document not found'}
    
    def delete_summoner_match_info(self, match_id: str, puuid: str):
        collection_name = self.db[puuid]
        result = collection_name.find_one_and_delete({"matchId": match_id})
        if result:
            return {'success': True}
        else:
            return {'success': False, 'message': 'Document not found'}
        
    def check_match_in_db(self, match_id: str):
        collection_name = self.db['match']
        result = collection_name.find({'matchId': match_id})
        if result.count()>0:
            return True
        else:
            return False

    def get_summoner_from_db(self, match_id: str, puuid: str):
        collection_name = self.db[puuid]
        result = collection_name.find_one({"matchId": match_id})
        if result:
            result['_id'] = str(result['_id'])
        return result


    def get_match_from_db(self, match_id: str):
        collection_name = self.db['match']
        result = collection_name.find_one({'matchId': match_id})
        if result:
            result['_id'] = str(result['_id'])
        return result

