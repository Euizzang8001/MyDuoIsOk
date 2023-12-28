from sqlalchemy import Column, DateTime, String, Integer
from sqlalchemy.sql.functions import current_timestamp
from config.database import Base

class MatchInfo(Base):
    __tablename__ = "MatchInfo"
    
    matchId = Column( 
        String(255),
        primary_key=True,
        unique = True,
        comment='Match Id',
    )

    summonerOnePuuid = Column(
        String(255),
        comment = 'Summoner One puuid',
    )
    summonerTwoPuuid = Column(
        String(255),
        comment = 'Summoner Two puuid',
    )
    summonerThreePuuid = Column(
        String(255),
        comment = 'Summoner Three puuid',
    )
    summonerFourPuuid = Column(
        String(255),
        comment = 'Summoner Four puuid',
    )
    summonerFivePuuid = Column(
        String(255),
        comment = 'Summoner Five puuid',
    )
    summonerSixPuuid = Column(
        String(255),
        comment = 'Summoner Six puuid',
    )
    summonerSevenPuuid = Column(
        String(255),
        comment = 'Summoner Seven puuid',
    )
    summonerEightPuuid = Column(
        String(255),
        comment = 'Summoner Eight puuid',
    )
    summonerNinePuuid = Column(
        String(255),
        comment = 'Summoner Nine puuid',
    )
    summonerTenPuuid = Column(
        String(255),
        comment = 'Summoner Ten puuid',
    )
    
    gameMode = Column(
        String(255),
        comment='Game Mode',
    )

    teamBlueId = Column(
        int,
        comment='Team Blue Id'
    )
    teamBlueWin = Column(
        int,
        comment='Team Blue Win'
    )
    teamBlueGold = Column(
        int,
        comment='Team Blue Gold'
    )
    teamBlueBaronKills = Column(
        int,
        comment='Team Blue Baron Kills'
    )
    teamBlueChampionKills = Column(
        int,
        comment='Team Blue Champion kills'
    )
    teamBlueDragonKills = Column(
        int,
        comment='Team Blue Dragon Kills'
    )
    teamBlueInhibitorKills = Column(
        int,
        comment='Team Blue Inhibitor Kills'
    )
    teamBlueRiftheraldKills = Column(
        int,
        comment='Team Blue Riftherald kills'
    )
    teamBlueTowerKills = Column(
        int,
        comment='Team Blue Tower Kills'
    )

    teamPurpleId = Column(
        int,
        comment='Team Purple Id'
    )
    teamPurpleWin = Column(
        int,
        comment='Team Purple Win'
    )
    teamPurpleGold = Column(
        int,
        comment='Team Purple Gold'
    )
    teamPurpleBaronKills = Column(
        int,
        comment='Team Purple Baron Kills'
    )
    teamPurpleChampionKills = Column(
        int,
        comment='Team Purple Champion kills'
    )
    teamPurpleDragonKills = Column(
        int,
        comment='Team Purple Dragon Kills'
    )
    teamPurpleInhibitorKills = Column(
        int,
        comment='Team Purple Inhibitor Kills'
    )
    teamPurpleRiftheraldKills = Column(
        int,
        comment='Team Purple Riftherald kills'
    )
    teamPurpleTowerKills = Column(
        int,
        comment='Team Purple Tower Kills'
    )

class SummonerInfo(Base):
    matchId = Column(
        String(255),
        primary_key=True,
        comment='Match Id',
    )
    championId = Column(
        int,
        comment='Champion Id',
    )
    goldEarned = Column(
        int,
        comment='Earned Gold',
    )
    kills = Column(
        int,
        comment = 'number of champion kill',
    )
    deaths = Column(
        int, 
        comment='number of deaths',
    )
    assists = Column(
        int,
        comment='number of assists',
    )
    lane = Column(
        String(255),
        comment='lane',
    )
    role = Column(
        String(255),
        comment='role',
    )
    teamId = Column(
        int,
        comment='Team Id',
    )
    champLevel = Column(
        int,
        default= 0,
        comment='Champion Level',
    )
    goldSpent = Column(
        int,
        default=0,
        comment='gold Spent',
    )
    totalDamageDealtToChampions = Column(
        int,
        default=0,
        comment = 'total damage dealt to champions',
    )
    totalHeal = Column(
        int,
        default=0,
        comment = 'total heal',
    )
    totalTimeCCDealt = Column(
        int,
        default=0,
        comment = 'total time cc dealt',
    )
    win = Column(
        int,
        comment = 'win or defeat',
    )
    visionScore = Column(
        int,
        default= 0,
        comment = 'vision score',
    )
    lastSearchTime = Column(
        DateTime(timezone=True),
        server_default=current_timestamp(),
        nullable=False,
    )