import datetime
from pydantic import BaseModel
from typing import List, Optional

class PlayerBase(BaseModel):
    Player_name: str

class Player(PlayerBase):
    datetime: datetime.datetime
    class Config:
        orm_mode = True