from sqlalchemy import Column, DateTime, String, Integer
from sqlalchemy.sql.functions import current_timestamp
from config.database import Base

class Match(Base):
    __tablename__ = "matches"
    
    match_id = Column( 
        String(255),
        primary_key=True,
        unique = True,
        comment='Match Id',
    )

    gameMode = Column(
        String(255),
        default='CLASSIC',
        comment = 'Game Mode',
    )
    teamBlue = Column(
        list,
        comment='Team Blue',
    )
    teamPurple = Column(
        list,
        comment='Team Purple'
    )
    participants = Column(
        list, 
        comment = 'Participants'
    )

class Summoner(Base):
    __tablename__ = 'summoners'

    puuid = Column(
        String(255), 
        primary_key=True,
        unique=True,
        comment='puuid',
    )

    riotIdGameName = Column(
        String(255),
        comment='Riot Game Name',
    )

    riotIdTagline = Column(
        String(255),
        comment='Riot Game Tagline',
    )

    match_list = Column(
        list,
        comment = 'Match List Per Summoner',
    )
