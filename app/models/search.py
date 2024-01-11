from datetime import datetime
from pydantic import BaseModel

class MatchInfoBase(BaseModel):
    gameMode : str
    matchId: str
    gameDuration : int
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

    summonerOneChampionName: str
    summonerTwoChampionName : str
    summonerThreeChampionName : str
    summonerFourChampionName : str
    summonerFiveChampionName : str
    summonerSixChampionName : str
    summonerSevenChampionName : str
    summonerEightChampionName : str
    summonerNineChampionName : str
    summonerTenChampionName : str

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
    
    teamRedId : int
    teamRedBan: list
    teamRedWin : int
    teamRedGold : int
    teamRedBaronKills : int
    teamRedChampionKills : int
    teamRedDragonKills : int
    teamRedInhibitorKills : int
    teamRedRiftheraldKills : int
    teamRedTowerKills : int

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
    totalDamageTaken: int
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
    versusTDT: int
    versusTH:int
    versusTTCCD:int
    versusVS: int