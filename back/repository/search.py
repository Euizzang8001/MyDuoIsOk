from typing import List, Optional
from fastapi import Depends
from sqlalchemy.orm import Session
import uuid
from fastapi import HTTPException

from config.database import get_db
from models.search import Player as PlayerModel
from schemas.search import Player, PlayerBase
from datetime import date

apikey=""


class PlayerRepository():
    def __init__(self, db: Session = Depends(get_db)) -> None : 
        self.db = db

    
    def get_player(self, player_id: str) -> Player:
        player = self.get_player_in_db(player_id = player_id)
        if player:
            return player
        else:
            True