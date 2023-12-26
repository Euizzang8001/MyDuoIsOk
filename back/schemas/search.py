import datetime
from pydantic import BaseModel
from typing import List, Optional

class PlayerBase(BaseModel):
    id: str
    accountId:str
    puuid:str
    name:str
    profileIconId: int
    revisionDate:int
    summonerLevel:int

class Player(PlayerBase):
    datetime: datetime.datetime
    class Config:
        orm_mode = True
