from sqlalchemy import Column, DateTime, String, Integer
from sqlalchemy.sql.functions import current_timestamp
from config.database import Base

class Player(Base):
    __tablename__ = "players"
    
    id = Column( 
        String(255),
        primary_key=True,
        unique = True,
        comment='Player ID',
    )
    accointId = Column(
        String(255),
        primary_key=True,
        unique = True,
        comment='Player Account ID',
    )
    puuid = Column(
        String(255),
        unique = True,
        comment='Player PUUID',
    )
    name = Column(
        String(255),
        comment = 'Player Name',
    )
    profileIconId = Column(
        Integer,
        comment = "Player Profile Icon ID",
    )
    revisionDate = Column(
        Integer,
        comment="Revision Date",
    )
    summonerLevel = Column(
        Integer,
        comment="Summoner Level",
    )