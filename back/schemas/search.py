def match_info(match) -> dict:
    return{
        "matchId": match['matchId'],
        "summonerOnePuuid": match['summonerOnePuuid'],
        "summonerTwoPuuid": match['summonerTwoPuuid'],
        "summonerThreePuuid": match['summonerThreePuuid'],
        "summonerFourPuuid": match['summonerFourPuuid'],
        "summonerFivePuuid": match['summonerFivePuuid'],
        "summonerSixPuuid": match['summonerSixPuuid'],
        "summonerSevenPuuid": match['summonerSevenPuuid'],
        "summonerEightPuuid": match['summonerEightPuuid'],
        "summonerNinePuuid": match['summonerNinePuuid'],
        "summonerTenPuuid": match['summonerTenPuuid'],

        "gameMode": match['gameMode'],

        "teamBlueId": match['teamBlueId'],
        "teamBlueWin": match['teamBlueWin'],
        "teamBlueGold": match['teamBlueGold'],
        "teamBlueBaronKills": match['teamBlueBaronKills'],
        "teamBlueChampionKills": match['teamBlueChampionKills'],
        "teamBlueDragonKills": match['teamBlueDragonKills'],
        "teamBlueInhibitorKills": match['teamBlueInhibitorKills'],
        "teamBlueRiftheraldKills": match['teamBlueRiftheraldKills'],
        "teamBlueTowerKills": match['teamBlueTowerKills'],

        "teamPurpleId": match['teamPurpleId'],
        "teamPurpleWin": match['teamPurpleWin'],
        "teamPurpleGold": match['teamPurpleGold'],
        "teamPurpleBaronKills": match['teamPurpleBaronKills'],
        "teamPurpleChampionKills": match['teamPurpleChampionKills'],
        "teamPurpleDragonKills": match['teamPurpleDragonKills'],
        "teamPurpleInhibitorKills": match['teamPurpleInhibitorKills'],
        "teamPurpleRiftheraldKills": match['teamPurpleRiftheraldKills'],
        "teamPurpleTowerKills": match['teamPurpleTowerKills']
    }

def summoner_info(summoner) -> dict:
    return{
        "matchId": summoner['matchId'],
        "riotName": summoner['riotName'],
        "riotTagline": summoner['riotTagline'],
        "championId": summoner['championId'],
        "goldEarned": summoner['goldEarned'],
        "kills": summoner['kills'],
        "deaths": summoner['deaths'],
        "assists": summoner['assists'],
        "lane": summoner['lane'],
        "role": summoner['role'],
        "teamId": summoner['teamId'],
        "champLevel": summoner['champLevel'],
        "goldSpent": summoner['goldSpent'],
        "totalDamageDealtToChampions": summoner['totalDamageDealtToChampions'],
        "totalHeal": summoner['totalHeal'],
        "totalTimeCCDealt": summoner['totalTimeCCDealt'],
        "win": summoner['win'],
        "visionScore": summoner['visionScore'],
        "lastSearchTime": summoner['lastSearchTime']
    }