from datetime import datetime
from pydantic import BaseModel

class MatchInfoBase(BaseModel):
    gameMode : str
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

    summonerOneriotIdGameName: str
    summonerTworiotIdGameName : str
    summonerThreeriotIdGameName : str
    summonerFourriotIdGameName : str
    summonerFiveriotIdGameName : str
    summonerSixriotIdGameName : str
    summonerSevenriotIdGameName : str
    summonerEightriotIdGameName : str
    summonerNineriotIdGameName : str
    summonerTenriotIdGameName : str

    summonerOneriotIdTagline: str
    summonerTworiotIdTagline : str
    summonerThreeriotIdTagline : str
    summonerFourriotIdTagline : str
    summonerFiveriotIdTagline : str
    summonerSixriotIdTagline : str
    summonerSevenriotIdTagline : str
    summonerEightriotIdTagline : str
    summonerNineriotIdTagline : str
    summonerTenriotIdTagline : str

    teamBlueId : int
    teamBlueBan: list
    teamBlueWin : int
    teamBlueGold : int
    teamBlueBaronKills : int
    teamBlueChampionKills : int
    teamBlueDragonKills : int
    teamBlueInhibitorKills : int
    teamBlueRiftheraldKills : int
    teamBlueTowerKills : int
    
    teamPurpleId : int
    teamPurpleBan: list
    teamPurpleWin : int
    teamPurpleGold : int
    teamPurpleBaronKills : int
    teamPurpleChampionKills : int
    teamPurpleDragonKills : int
    teamPurpleInhibitorKills : int
    teamPurpleRiftheraldKills : int
    teamPurpleTowerKills : int

class SummonerBase(BaseModel):
    matchId: str
    assists: int
    champLevel: int
    championId: int
    championName: str
    deaths: int
    goldEarned: int
    goldSpent: int
    kills: int
    lane: str
    summonerName: str
    riotIdGameName: str
    riotIdTagline: str
    role: str
    teamId: int
    totalDamageDealtToChampions: int
    totalHeal: int
    totalTimeCCDealt: int
    win: bool
    visionScore: int
    versusassists: int
    versuschampionLevel :int
    versusdeaths:int
    versusgoldEarned:int
    versuskills:int
    versusTDDTC:int
    versusTH:int
    versusTTCCD:int
    versusVS: int