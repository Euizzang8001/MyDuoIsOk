import datetime
from pydantic import BaseModel
from typing import List, Optional

class MatchInfoBase(BaseModel):
    matchId: str
    summonerOnePuuid: str
    summonerTwoPuuid : str
    summonerThreePuuid : str
    summonerFourPuuid : str
    summonerFivePuuid : str
    summonerSixPuuid : str
    summonerSevenPuuid : str
    summonerEightPuuid : str
    summonerNinePuuid : str
    summonerTenPuuid : str

    gameMode : str

    teamBlueId : int
    teamBlueWin : int
    teamBlueGold : int
    teamBlueBaronKills : int
    teamBlueChampionKills : int
    teamBlueDragonKills : int
    teamBlueInhibitorKills : int
    teamBlueRiftheraldKills : int
    teamBlueTowerKills : int
    
    teamPurpleId : int
    teamPurpleWin : int
    teamPurpleGold : int
    teamPurpleBaronKills : int
    teamPurpleChampionKills : int
    teamPurpleDragonKills : int
    teamPurpleInhibitorKills : int
    teamPurpleRiftheraldKills : int
    teamPurpleTowerKills : int

class SummonerBase(BaseModel):
    matchId : str
    championId : int
    goldEarned: int
    kills: int
    deaths : int
    assists: int
    lane: str
    role: str
    teamId: int
    champLevel: int
    goldSpent: int
    totalDamageDealtToChampions: int
    totalHeal: int 
    totalTimeCCDealt: int
    win: int
    visionScore: int


class Summoner(SummonerBase):
    lastSearchTime: datetime.datetime
    
    class Config:
        orm_mode = True
        
