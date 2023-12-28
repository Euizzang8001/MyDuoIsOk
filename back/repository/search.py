from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
import requests
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table, DateTime
from sqlalchemy.sql.functions import current_timestamp
from config.database import get_db, engine
from models.search import MatchInfo as MatchInfoModel
from models.search import SummonerInfo as SummonerInfoModel
from schemas.search import MatchInfoBase, Summoner, SummonerBase
from datetime import date

apikey="RGAPI-1ee558c6-a670-474e-ad23-f49e3a2bf216"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",    
    "X-Riot-Token": apikey
}

class SummonerRepository():
    def __init__(self, db: Session = Depends(get_db)) -> None : 
        self.db = db

    def get_summoner_puuid(self, summoner_name: str): #player_name -> player의 계정 정보 return
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
    
    def append_match_info(self, match_info_dto: MatchInfoBase): #match_info_dto를 받아서 MatchInfo table에 저장
        db_match = MatchInfoModel(
            matchId = match_info_dto.matchId,
            summonerOnePuuid = match_info_dto.summonerOnePuuid,
            summonerTwoPuuid = match_info_dto.summonerTwoPuuid,
            summonerThreePuuid =match_info_dto.summonerThreePuuid,
            summonerFourPuuid = match_info_dto.summonerFourPuuid,
            summonerFivePuuid =match_info_dto.summonerFivePuuid,
            summonerSixPuuid = match_info_dto.summonerSixPuuid,
            summonerSevenPuuid =match_info_dto.summonerSevenPuuid,
            summonerEightPuuid = match_info_dto.summonerEightPuuid,
            summonerNinePuuid =match_info_dto.summonerNinePuuid,
            summonerTenPuuid = match_info_dto.summonerTenPuuid,
            gameMode = match_info_dto.gameMode,
            teamBlueId = match_info_dto.teamBlueId,
            teamBlueWin = match_info_dto.teamBlueWin,
            teamBlueGold = match_info_dto.teamBlueGold,
            teamBlueBaronKills = match_info_dto.teamBlueBaronKills,
            teamBlueChampionKills = match_info_dto.teamBlueChampionKills,
            teamBlueDragonKills = match_info_dto.teamBlueDragonKills,
            teamBlueInhibitorKills = match_info_dto.teamBlueInhibitorKills,
            teamBlueRiftheraldKills = match_info_dto.teamBlueRiftheraldKills,
            teamBlueTowerKills = match_info_dto.teamBlueTowerKills,
            teamPurpleId = match_info_dto.teamPurpleId,
            teamPurpleWin = match_info_dto.teamPurpleWin,
            teamPurpleGold = match_info_dto.teamPurpleGold,
            teamPurpleBaronKills = match_info_dto.teamPurpleBaronKills,
            teamPurpleChampionKills = match_info_dto.teamPurpleChampionKills,
            teamPurpleDragonKills = match_info_dto.teamPurpleDragonKills,
            teamPurpleInhibitorKills = match_info_dto.teamPurpleInhibitorKills,
            teamPurpleRiftheraldKills = match_info_dto.teamPurpleRiftheraldKills,
            teamPurpleTowerKills = match_info_dto.teamPurpleTowerKills,
        )
        self.db.add(db_match)
        self.db.commit()
        self.db.refresh(db_match)
        return db_match
    
    def append_summoner_info(self, puuid: str, summoner_dto: Summoner): 
        #match_info_dto를 받아서 {puuid}이름의 table에 저장
        db_summoner = SummonerInfoModel(
            matchId = summoner_dto.matchId,
            championId = summoner_dto.championId,
            goldEarned = summoner_dto.goldEarned,
            kills =summoner_dto.kills,
            deaths = summoner_dto.deaths,
            assists =summoner_dto.assists,
            lane = summoner_dto.lane,
            role =summoner_dto.role,
            teamId = summoner_dto.teamId,
            champLevel =summoner_dto.champLevel,
            goldSpent = summoner_dto.goldSpent,
            totalDamageDealtToChampions = summoner_dto.totalDamageDealtToChampions,
            totalHeal = summoner_dto.totalHeal,
            totalTimeCCDealt = summoner_dto.totalTimeCCDealt,
            win = summoner_dto.win,
            visionScore = summoner_dto.visionScore,
            lastSearchTime = summoner_dto.lastSearchTime,
        )
        self.db.add(db_summoner)
        self.db.commit()
        self.db.refresh(db_summoner)
        return db_summoner
    
    #summoner의 puuid를 받아 puuid이름의 새 table를 생성하는 함수
    def create_new_summoner_table(self, puuid: str, summoner_dto: Summoner):
        metadata = MetaData()
        summoner_table = Table(
            f"{puuid}",
            metadata,
            Column(String(255),primary_key=True,comment='Match Id'),Column(int,comment='Champion Id'),
            Column(int,comment='Earned Gold'),Column(int,comment = 'number of champion kill'),
            Column(int, comment='number of deaths'),Column(int,comment='number of assists'),
            Column(String(255),comment='lane'), Column(String(255),comment='role'),
            Column(int,comment='Team Id'),Column(int,default= 0,comment='Champion Level'),
            Column(int,default=0,comment='gold Spent'), Column(int,default=0,comment = 'total damage dealt to champions'),
            Column(int,default=0,comment = 'total heal'), Column(int,default=0,comment = 'total time cc dealt'),
            Column(int,comment = 'win or defeat'), Column(int,default= 0,comment = 'vision score'),
            Column(DateTime(timezone=True),server_default=current_timestamp(),nullable=False)
        )
        metadata.create_all(bind=engine)


