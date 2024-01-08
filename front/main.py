import streamlit as st
import requests
import datetime

back_url = 'http://127.0.0.1:8000/myduoisok'
get_puuid_url = back_url + '/get-summoner'
get_match_list_url = back_url + '/get-matchid'
get_match_info_url = back_url + '/get-matchinfo'
check_match_in_db_url = back_url + '/check-match-in-db'
append_match_info_url = back_url + '/append-matchinfo'


st.title('My Duo Is OK..? :frowning:')
    
explain1 = 'There are so many players playing with one or more friends.'
explain2 = 'We want to give you some detail information about your party!'
explain3 = 'So you can feel more excited with this info!'
st.write(explain1)
st.write(explain2)
st.write(explain3)

summoner = st.text_input('Write The Summoner Name')
search_summoner = st.button('Search')

summoner_puuid_list = []

match_id_list = []

if search_summoner: #검색하기 위해 버튼을 누르면 검색 정보를 db에 저장하고 불러오기
    summoner_nospace = ''.join(i for i in summoner if not i.isspace())
    st.write(summoner_nospace)
    summoner_list = list(summoner_nospace.split(','))
    st.write(summoner_list)
    for summoner_name in summoner_list:
        summoner_puuid = requests.get(get_puuid_url, params={'summoner': summoner_name}).json()
        summoner_puuid_list.append(summoner_puuid)
        if len(match_id_list) == 0:
            match_id_list = requests.get(get_match_list_url, params={'summoner_puuid': summoner_puuid}).json()
        else:
            match_id_list = list(set(match_id_list) & set(requests.get(get_match_list_url, params={'summoner_puuid': summoner_puuid}).json()))

    if len(match_id_list) == 0:
        st.error('Are You Duo? No game You Played Together In Last 100 Games !!')
    else:
        #일단 가장 최신 전적만 해보자
        match = match_id_list[0]
        goldSum = {}
        #db에 있는지 확인하고
        match_in_db= requests.get(check_match_in_db_url, params={'match_id': match}).json()
        lane_list = []
        if not match_in_db:
            #정보 라이엇으로부터 가져오고
            match_info = requests.get(get_match_info_url, params={'match_id': match}).json()
            same_lane_enemey = {}
            for i in range(10):
                if match_info['info']['participants'][i]['lane'] == 'TOP':
                    lane = 0
                elif match_info['info']['participants'][i]['lane'] == 'JUNGLE':
                    lane = 1
                elif match_info['info']['participants'][i]['lane'] == 'MIDDLE':
                    lane = 2
                elif match_info['info']['participants'][i]['role'] == 'CARRY':
                    lane = 3
                else:
                    lane = 4
                lane_list.append(lane)
                if lane not in same_lane_enemey:
                    same_lane_enemey[lane] = [match_info['info']['participants'][i]['assists'],
                                              match_info['info']['participants'][i]['champLevel'],
                                              match_info['info']['participants'][i]['deaths'],
                                              match_info['info']['participants'][i]['goldEarned'],
                                              match_info['info']['participants'][i]['kills'],
                                              match_info['info']['participants'][i]['totalDamageDealtToChampions'],
                                              match_info['info']['participants'][i]['totalHeal'],
                                              match_info['info']['participants'][i]['totalTimeCCDealt'],
                                              match_info['info']['participants'][i]['visionScore']
                                              ]
                else:
                    same_lane_enemey[lane][0] -= match_info['info']['participants'][i]['assists']
                    same_lane_enemey[lane][1] -= match_info['info']['participants'][i]['champLevel']
                    same_lane_enemey[lane][2] -= match_info['info']['participants'][i]['deaths']
                    same_lane_enemey[lane][3] -= match_info['info']['participants'][i]['goldEarned']
                    same_lane_enemey[lane][4] -= match_info['info']['participants'][i]['kills']
                    same_lane_enemey[lane][5] -= match_info['info']['participants'][i]['totalDamageDealtToChampions']
                    same_lane_enemey[lane][6] -= match_info['info']['participants'][i]['totalHeal']
                    same_lane_enemey[lane][7] -= match_info['info']['participants'][i]['totalTimeCCDealt']
                    same_lane_enemey[lane][8] -= match_info['info']['participants'][i]['visionScore']
            st.write(same_lane_enemey)
            for i in range(10):
                if i < 5:
                    per_summoner_info = {
                        "matchId": match,
                        "assists": match_info['info']['participants'][i]['assists'],
                        "champLevel": match_info['info']['participants'][i]['champLevel'],
                        "championId": match_info['info']['participants'][i]['championId'],
                        "championName": match_info['info']['participants'][i]['championName'],
                        "deaths": match_info['info']['participants'][i]['deaths'],
                        "goldEarned": match_info['info']['participants'][i]['goldEarned'],
                        "goldSpent": match_info['info']['participants'][i]['goldSpent'],
                        "kills": match_info['info']['participants'][i]['kills'],
                        "lane": match_info['info']['participants'][i]['lane'],
                        "summonerName": match_info['info']['participants'][i]['summonerName'],
                        "riotIdGameName":  match_info['info']['participants'][i]['riotIdGameName'],
                        "riotIdTagline":  match_info['info']['participants'][i]['riotIdTagline'],
                        "role": match_info['info']['participants'][i]['role'],
                        "teamId": match_info['info']['participants'][i]['teamId'],
                        "totalDamageDealtToChampions":match_info['info']['participants'][i]['totalDamageDealtToChampions'],
                        "totalHeal": match_info['info']['participants'][i]['totalHeal'],
                        "totalTimeCCDealt": match_info['info']['participants'][i]['totalTimeCCDealt'],
                        "win": match_info['info']['participants'][i]['win'],
                        "visionScore": match_info['info']['participants'][i]['visionScore'],

                        "versusassists": same_lane_enemey[lane_list[i]][0],
                        "versuschampionLevel" :same_lane_enemey[lane_list[i]][1],
                        "versusdeaths":same_lane_enemey[lane_list[i]][2],
                        "versusgoldEarned":same_lane_enemey[lane_list[i]][3],
                        "versuskills":same_lane_enemey[lane_list[i]][4],
                        "versusTDDTC":same_lane_enemey[lane_list[i]][5],
                        "versusTH":same_lane_enemey[lane_list[i]][6],
                        "versusTTCCD":same_lane_enemey[lane_list[i]][7],
                        "versusVS": same_lane_enemey[lane_list[i]][8],
                    }
                else:
                    per_summoner_info = {
                        "matchId": match,
                        "assists": match_info['info']['participants'][i]['assists'],
                        "champLevel": match_info['info']['participants'][i]['champLevel'],
                        "championId": match_info['info']['participants'][i]['championId'],
                        "championName": match_info['info']['participants'][i]['championName'],
                        "deaths": match_info['info']['participants'][i]['deaths'],
                        "goldEarned": match_info['info']['participants'][i]['goldEarned'],
                        "goldSpent": match_info['info']['participants'][i]['goldSpent'],
                        "kills": match_info['info']['participants'][i]['kills'],
                        "lane": match_info['info']['participants'][i]['lane'],
                        "summonerName": match_info['info']['participants'][i]['summonerName'],
                        "riotIdGameName":  match_info['info']['participants'][i]['riotIdGameName'],
                        "riotIdTagline":  match_info['info']['participants'][i]['riotIdTagline'],
                        "role": match_info['info']['participants'][i]['role'],
                        "teamId": match_info['info']['participants'][i]['teamId'],
                        "totalDamageDealtToChampions":match_info['info']['participants'][i]['totalDamageDealtToChampions'],
                        "totalHeal": match_info['info']['participants'][i]['totalHeal'],
                        "totalTimeCCDealt": match_info['info']['participants'][i]['totalTimeCCDealt'],
                        "win": match_info['info']['participants'][i]['win'],
                        "visionScore": match_info['info']['participants'][i]['visionScore'],

                        "versusassists": same_lane_enemey[lane_list[i]][0],
                        "versuschampionLevel" :same_lane_enemey[lane_list[i]][1],
                        "versusdeaths":same_lane_enemey[lane_list[i]][2],
                        "versusgoldEarned":same_lane_enemey[lane_list[i]][3],
                        "versuskills":same_lane_enemey[lane_list[i]][4],
                        "versusTDDTC":same_lane_enemey[lane_list[i]][5],
                        "versusTH":same_lane_enemey[lane_list[i]][6],
                        "versusTTCCD":same_lane_enemey[lane_list[i]][7],
                        "versusVS": same_lane_enemey[lane_list[i]][8],
                    }
                if per_summoner_info['teamId'] not in goldSum:
                    goldSum[per_summoner_info['teamId']] = 0
                goldSum[per_summoner_info['teamId']] += per_summoner_info['goldEarned']
                st.write(per_summoner_info)
                append_summoner_info_url = back_url + f"/append-summonerinfo/{match_info['metadata']['participants'][i]}"
                result = requests.put(append_summoner_info_url, params={'puuid': match_info['metadata']['participants'][i]},  json=per_summoner_info)
            #db에 저장하고
            per_match_info = {
                "gameMode": match_info['info']['gameMode'],
                'matchId':  match,
                'summonerOnePuuid': match_info['metadata']['participants'][0],
                'summonerTwoPuuid': match_info['metadata']['participants'][1],
                'summonerThreePuuid': match_info['metadata']['participants'][2],
                'summonerFourPuuid': match_info['metadata']['participants'][3],
                'summonerFivePuuid': match_info['metadata']['participants'][4],
                'summonerSixPuuid': match_info['metadata']['participants'][5],
                'summonerSevenPuuid': match_info['metadata']['participants'][6],
                'summonerEightPuuid': match_info['metadata']['participants'][7],
                'summonerNinePuuid': match_info['metadata']['participants'][8],
                'summonerTenPuuid': match_info['metadata']['participants'][9],
                "teamBlueId": match_info['info']['teams'][0]['teamId'],
                "teamBlueBan": list(match_info['info']['teams'][0]['bans'][i]['championId'] for i in range(5)),
                "teamBlueWin": match_info['info']['teams'][0]['win'],
                "teamBlueGold": goldSum[match_info['info']['teams'][0]['teamId']],
                "teamBlueBaronKills": match_info['info']['teams'][0]['objectives']['baron']['kills'],
                "teamBlueChampionKills": match_info['info']['teams'][0]['objectives']['champion']['kills'],
                "teamBlueDragonKills": match_info['info']['teams'][0]['objectives']['dragon']['kills'],
                "teamBlueInhibitorKills": match_info['info']['teams'][0]['objectives']['inhibitor']['kills'],
                "teamBlueRiftheraldKills": match_info['info']['teams'][0]['objectives']['riftHerald']['kills'],
                "teamBlueTowerKills": match_info['info']['teams'][0]['objectives']['tower']['kills'],
                "teamPurpleId": match_info['info']['teams'][1]['teamId'],
                "teamPurpleBan": list(match_info['info']['teams'][1]['bans'][i]['championId'] for i in range(5)),
                "teamPurpleWin": match_info['info']['teams'][1]['win'],
                "teamPurpleGold": goldSum[match_info['info']['teams'][1]['teamId']],
                "teamPurpleBaronKills": match_info['info']['teams'][1]['objectives']['baron']['kills'],
                "teamPurpleChampionKills": match_info['info']['teams'][1]['objectives']['champion']['kills'],
                "teamPurpleDragonKills": match_info['info']['teams'][1]['objectives']['dragon']['kills'],
                "teamPurpleInhibitorKills": match_info['info']['teams'][1]['objectives']['inhibitor']['kills'],
                "teamPurpleRiftheraldKills": match_info['info']['teams'][1]['objectives']['riftHerald']['kills'],
                "teamPurpleTowerKills": match_info['info']['teams'][1]['objectives']['tower']['kills'],
            }
            match_result = requests.post(append_match_info_url, json = per_match_info)
            st.write(match_result)
            


        #db에서 match정보 불러오기
        #db에서 match에 있는 소환사 10명의 정보 불러오기 
        #champion.json나 다른 정보들에 따라 코드 작성
            
    
    

    

        