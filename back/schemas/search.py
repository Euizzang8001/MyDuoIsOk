import datetime
from pydantic import BaseModel
from typing import List, Optional

class MatchBase(BaseModel):
    match_id: str
    gameMode:str
    teamBlue:list
    teamPurple:list
    participants: list

class SummonerBase(BaseModel):
    puuid: str
    riotIdGameName:str
    riotIdTagline:list
    match_list:list

class Summoner(SummonerBase):
    datetime: datetime.datetime
    class Config:
        orm_mode = True
