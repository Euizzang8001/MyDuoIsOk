import streamlit as st
import requests
import datetime
import json
import os
from PIL import Image
import io

back_url = 'http://127.0.0.1:8000/myduoisok'
get_puuid_url = back_url + '/get-summoner'
get_match_list_url = back_url + '/get-matchid'
get_match_info_url = back_url + '/get-matchinfo'
check_match_in_db_url = back_url + '/check-match-in-db'
append_match_info_url = back_url + '/append-matchinfo'

image_url = 'https://ddragon.leagueoflegends.com/cdn/13.24.1/img/champion/'

champion_data = requests.get('https://ddragon.leagueoflegends.com/cdn/13.24.1/data/en_US/champion.json').json()

number_list = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']

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
    summoner_list = list(summoner_nospace.split(','))
    st.write(f':man_and_woman_holding_hands:{summoner}:woman_and_man_holding_hands: Your Matches Are Here!')
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
        st.write(match)
        goldSum = {}
        #db에 있는지 확인하고
        match_in_db = requests.get(check_match_in_db_url, params={'match_id': match}).json()
        if not match_in_db:
            #정보 라이엇으로부터 가져오고
            match_info = requests.get(get_match_info_url, params={'match_id': match}).json()
            same_lane_enemey = {}
            lane_list = []
            for i in range(10):
                lane_str = match_info['info']['participants'][i]['teamPosition']
                if lane_str == 'TOP':
                    lane = 0
                elif lane_str == 'JUNGLE':
                    lane = 1
                elif lane_str == 'MIDDLE':
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
            for i in range(10):
                if 'riotIdGameName' in match_info['info']['participants'][i]:
                    riotIdGameName = match_info['info']['participants'][i]['riotIdGameName']
                else: 
                    riotIdGameName = match_info['info']['participants'][i]['summonerName']

                if 'riotIdTagline' in match_info['info']['participants'][i]:
                    riotIdTagline = match_info['info']['participants'][i]['riotIdTagline']
                else: 
                    riotIdTagline = 'KR1'

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
                        "lane": match_info['info']['participants'][i]['teamPosition'],
                        "summonerName": match_info['info']['participants'][i]['summonerName'],
                        "riotIdGameName":  riotIdGameName,
                        "riotIdTagline":  riotIdTagline,
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
                        "lane": match_info['info']['participants'][i]['teamPosition'],
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

                        "versusassists": -same_lane_enemey[lane_list[i]][0],
                        "versuschampionLevel" :-same_lane_enemey[lane_list[i]][1],
                        "versusdeaths":-same_lane_enemey[lane_list[i]][2],
                        "versusgoldEarned":-same_lane_enemey[lane_list[i]][3],
                        "versuskills":-same_lane_enemey[lane_list[i]][4],
                        "versusTDDTC":-same_lane_enemey[lane_list[i]][5],
                        "versusTH":-same_lane_enemey[lane_list[i]][6],
                        "versusTTCCD":-same_lane_enemey[lane_list[i]][7],
                        "versusVS": -same_lane_enemey[lane_list[i]][8],
                    }
                if per_summoner_info['teamId'] not in goldSum:
                    goldSum[per_summoner_info['teamId']] = 0
                goldSum[per_summoner_info['teamId']] += per_summoner_info['goldEarned']
                append_summoner_info_url = back_url + f"/append-summonerinfo/{match_info['metadata']['participants'][i]}"
                result = requests.put(append_summoner_info_url, params={'puuid': match_info['metadata']['participants'][i]},  json=per_summoner_info)
            #db에 저장하고
            per_match_info = {
                "gameMode": match_info['info']['gameMode'],
                'matchId':  match,
                "gameDuration": match_info['info']['gameDuration'],
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

                'summonerOneriotIdGameName': match_info['info']['participants'][0]['riotIdGameName'],
                'summonerTworiotIdGameName': match_info['info']['participants'][1]['riotIdGameName'],
                'summonerThreeriotIdGameName': match_info['info']['participants'][2]['riotIdGameName'],
                'summonerFourriotIdGameName': match_info['info']['participants'][3]['riotIdGameName'],
                'summonerFiveriotIdGameName': match_info['info']['participants'][4]['riotIdGameName'],
                'summonerSixriotIdGameName': match_info['info']['participants'][5]['riotIdGameName'],
                'summonerSevenriotIdGameName': match_info['info']['participants'][6]['riotIdGameName'],
                'summonerEightriotIdGameName': match_info['info']['participants'][7]['riotIdGameName'],
                'summonerNineriotIdGameName': match_info['info']['participants'][8]['riotIdGameName'],
                'summonerTenriotIdGameName': match_info['info']['participants'][9]['riotIdGameName'],

                'summonerOneriotIdTagline': match_info['info']['participants'][0]['riotIdTagline'],
                'summonerTworiotIdTagline': match_info['info']['participants'][1]['riotIdTagline'],
                'summonerThreeriotIdTagline':match_info['info']['participants'][2]['riotIdTagline'],
                'summonerFourriotIdTagline':match_info['info']['participants'][3]['riotIdTagline'],
                'summonerFiveriotIdTagline': match_info['info']['participants'][4]['riotIdTagline'],
                'summonerSixriotIdTagline': match_info['info']['participants'][5]['riotIdTagline'],
                'summonerSevenriotIdTagline': match_info['info']['participants'][6]['riotIdTagline'],
                'summonerEightriotIdTagline': match_info['info']['participants'][7]['riotIdTagline'],
                'summonerNineriotIdTagline': match_info['info']['participants'][8]['riotIdTagline'],
                'summonerTenriotIdTagline': match_info['info']['participants'][9]['riotIdTagline'],

                'summonerOneChampionName': match_info['info']['participants'][0]['championName'],
                'summonerTwoChampionName': match_info['info']['participants'][1]['championName'],
                'summonerThreeChampionName':match_info['info']['participants'][2]['championName'],
                'summonerFourChampionName':match_info['info']['participants'][3]['championName'],
                'summonerFiveChampionName': match_info['info']['participants'][4]['championName'],
                'summonerSixChampionName': match_info['info']['participants'][5]['championName'],
                'summonerSevenChampionName': match_info['info']['participants'][6]['championName'],
                'summonerEightChampionName': match_info['info']['participants'][7]['championName'],
                'summonerNineChampionName': match_info['info']['participants'][8]['championName'],
                'summonerTenChampionName': match_info['info']['participants'][9]['championName'],

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
                "teamRedId": match_info['info']['teams'][1]['teamId'],
                "teamRedBan": list(match_info['info']['teams'][1]['bans'][i]['championId'] for i in range(5)),
                "teamRedWin": match_info['info']['teams'][1]['win'],
                "teamRedGold": goldSum[match_info['info']['teams'][1]['teamId']],
                "teamRedBaronKills": match_info['info']['teams'][1]['objectives']['baron']['kills'],
                "teamRedChampionKills": match_info['info']['teams'][1]['objectives']['champion']['kills'],
                "teamRedDragonKills": match_info['info']['teams'][1]['objectives']['dragon']['kills'],
                "teamRedInhibitorKills": match_info['info']['teams'][1]['objectives']['inhibitor']['kills'],
                "teamRedRiftheraldKills": match_info['info']['teams'][1]['objectives']['riftHerald']['kills'],
                "teamRedTowerKills": match_info['info']['teams'][1]['objectives']['tower']['kills'],
            }
            match_result = requests.post(append_match_info_url, json = per_match_info)
        get_matchinfo_from_db_url = back_url + f'/get-matchinfo-from-db/{match}'
        per_match_info = requests.get(get_matchinfo_from_db_url, params = {'match_id' : match}).json()
        summoner_list_per_match = []
        for j in range(len(summoner_list)):
            get_summoner_from_db_url = back_url + f'/get-summonerinfo-from-db/{summoner_puuid_list[j]}/{match}'
            summoner_list_per_match.append(requests.get(get_summoner_from_db_url, params = {'puuid': summoner_puuid_list[j],'match_id' : match}).json())


        #champion.json와 다른 정보에 따라 코드 작성
    # matchId 마다의 container
    with st.container(border = True):
        duration_seconds = per_match_info['gameDuration']%60
        st.write(f"Game Time  {per_match_info['gameDuration']//60}:{duration_seconds:02}")
        #게임 요약 부분(team Blue)
        with st.container(border = True):
            with st.container():
                if per_match_info['teamBlueWin'] == 0:
                    st.write('<p style="text-align: center; font-size: 2;">Blue Team Defeat / Red Team Win</p>', unsafe_allow_html=True)
                else:
                    st.write('<p style="text-align: center; font-size: 2;">Blue Team Win / Red Team Defeat</p>', unsafe_allow_html=True)
            #blue team 요약
            with st.container():
               with st.container(border = True):
                    st.write('<p style="text-align: center; font-size: 2;">Blue Team Infomation</p>', unsafe_allow_html=True)
                    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
                    with col1:
                        with st.container():
                            st.write(f"<p style='text-align: center; font-size: 2;'>Gold", unsafe_allow_html=True)
                        with st.container():
                            st.write(f"<p style='text-align: center; font-size: 2;'>{per_match_info['teamBlueGold']}", unsafe_allow_html=True)
                    with col2:
                        with st.container():
                            st.write(f"<p style='text-align: center; font-size: 2;'>Baron", unsafe_allow_html=True)
                        with st.container():
                            st.write(f"<p style='text-align: center; font-size: 2;'>{per_match_info['teamBlueBaronKills']}", unsafe_allow_html=True)
                    with col3:
                        with st.container():
                            st.write(f"<p style='text-align: center; font-size: 2;'>Kills", unsafe_allow_html=True)
                        with st.container():
                            st.write(f"<p style='text-align: center; font-size: 2;'>{per_match_info['teamBlueChampionKills']}", unsafe_allow_html=True)
                    with col4:
                        with st.container():
                            st.write(f"<p style='text-align: center; font-size: 2;'>Dragon", unsafe_allow_html=True)
                        with st.container():
                            st.write(f"<p style='text-align: center; font-size: 2;'>{per_match_info['teamBlueDragonKills']}", unsafe_allow_html=True)
                    with col5:
                        with st.container():
                            st.write(f"<p style='text-align: center; font-size: 2;'>Inhibitor", unsafe_allow_html=True)
                        with st.container():
                            st.write(f"<p style='text-align: center; font-size: 2;'>{per_match_info['teamBlueInhibitorKills']}", unsafe_allow_html=True)
                    with col6:
                        with st.container():
                            st.write(f"<p style='text-align: center; font-size: 2;'>Rift Herald", unsafe_allow_html=True)
                        with st.container():
                            st.write(f"<p style='text-align: center; font-size: 2;'>{per_match_info['teamBlueRiftheraldKills']}", unsafe_allow_html=True)
                    with col7:
                        with st.container():
                            st.write(f"<p style='text-align: center; font-size: 2;'>Tower", unsafe_allow_html=True)
                        with st.container():
                            st.write(f"<p style='text-align: center; font-size: 2;'>{per_match_info['teamBlueTowerKills']}", unsafe_allow_html=True)
            #red team 요약
            with st.container():
                with st.container(border = True):
                    st.write('<p style="text-align: center; font-size: 2;">Red Team Infomation</p>', unsafe_allow_html=True)
                    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
                    with col1:
                        with st.container():
                            st.write(f"<p style='text-align: center; font-size: 2;'>Gold", unsafe_allow_html=True)
                        with st.container():
                            st.write(f"<p style='text-align: center; font-size: 2;'>{per_match_info['teamRedGold']}", unsafe_allow_html=True)
                    with col2:
                        with st.container():
                            st.write(f"<p style='text-align: center; font-size: 2;'>Baron", unsafe_allow_html=True)
                        with st.container():
                            st.write(f"<p style='text-align: center; font-size: 2;'>{per_match_info['teamRedBaronKills']}", unsafe_allow_html=True)
                    with col3:
                        with st.container():
                            st.write(f"<p style='text-align: center; font-size: 2;'>Kills", unsafe_allow_html=True)
                        with st.container():
                            st.write(f"<p style='text-align: center; font-size: 2;'>{per_match_info['teamRedChampionKills']}", unsafe_allow_html=True)
                    with col4:
                        with st.container():
                            st.write(f"<p style='text-align: center; font-size: 2;'>Dragon", unsafe_allow_html=True)
                        with st.container():
                            st.write(f"<p style='text-align: center; font-size: 2;'>{per_match_info['teamRedDragonKills']}", unsafe_allow_html=True)
                    with col5:
                        with st.container():
                            st.write(f"<p style='text-align: center; font-size: 2;'>Inhibitor", unsafe_allow_html=True)
                        with st.container():
                            st.write(f"<p style='text-align: center; font-size: 2;'>{per_match_info['teamRedInhibitorKills']}", unsafe_allow_html=True)
                    with col6:
                        with st.container():
                            st.write(f"<p style='text-align: center; font-size: 2;'>Rift Herald", unsafe_allow_html=True)
                        with st.container():
                            st.write(f"<p style='text-align: center; font-size: 2;'>{per_match_info['teamRedRiftheraldKills']}", unsafe_allow_html=True)
                    with col7:
                        with st.container():
                            st.write(f"<p style='text-align: center; font-size: 2;'>Tower", unsafe_allow_html=True)
                        with st.container():
                            st.write(f"<p style='text-align: center; font-size: 2;'>{per_match_info['teamRedTowerKills']}", unsafe_allow_html=True)
            #여기는 챔피언픽(사진), 소환사 이름, 소환사 태그, 벤픽(사진)
            with st.container():
                with st.container():
                    col1, col2, col3 = st.columns([3, 3, 3])
                    with col1:
                        st.write('<p style="text-align: center; font-size: 2;">BLUE</p>', unsafe_allow_html=True)
                    with col2:
                        st.write('<p style="text-align: center; font-size: 2;">Ban & Pick</p>', unsafe_allow_html=True)
                    with col3:
                        st.write('<p style="text-align: center; font-size: 2;">RED</p>', unsafe_allow_html=True)
                for k in range(5):
                    with st.container():
                        col1, col2, col3, col4, col5, col6 = st.columns([0.4, 2, 0.4, 0.4, 2, 0.4])
                        #픽 이미지
                        with col1:
                            per_summoner_champion_per_match = per_match_info[f'summoner{number_list[k]}ChampionName']
                            champion_image_url = image_url + per_summoner_champion_per_match + '.png'
                            champion_image = requests.get(champion_image_url, stream=True)
                            st.image(champion_image.content, use_column_width = True)
                        #소환사 이름
                        with col2:
                            per_summoner_name = per_match_info[f'summoner{number_list[k]}riotIdGameName']
                            per_summoner_tagline = per_match_info[f'summoner{number_list[k]}riotIdTagline']
                            st.write(f"<p style='text-align: center; font-size: 2;'>{per_summoner_name}#{per_summoner_tagline}</p>", unsafe_allow_html=True)
                        # 밴 이미지
                        with col3:
                            per_summoner_ban_key = per_match_info['teamBlueBan'][k]
                            per_summoner_ban = str(0)
                            for champion_key in champion_data['data']:
                                if champion_data['data'][champion_key]['key'] ==  str(per_summoner_ban_key):
                                    per_summoner_ban = champion_data['data'][champion_key]['name']
                                    break
                            ban_image_url = image_url + per_summoner_ban + '.png'
                            ban_image = requests.get(ban_image_url, stream=True).content
                            pil_image = Image.open(io.BytesIO(ban_image))
                            grayscale_image = pil_image.convert("L")
                            st.image(grayscale_image, use_column_width = True)

                        with col4:
                            per_summoner_ban_key = per_match_info['teamRedBan'][k]
                            per_summoner_ban = str(0)
                            for champion_key in champion_data['data']:
                                if champion_data['data'][champion_key]['key'] ==  str(per_summoner_ban_key):
                                    per_summoner_ban = champion_data['data'][champion_key]['name']
                                    break
                            ban_image_url = image_url + per_summoner_ban + '.png'
                            ban_image = requests.get(ban_image_url, stream=True).content
                            pil_image = Image.open(io.BytesIO(ban_image))
                            grayscale_image = pil_image.convert("L")
                            st.image(grayscale_image, use_column_width = True)

                        with col5:
                            per_summoner_name = per_match_info[f'summoner{number_list[k+5]}riotIdGameName']
                            per_summoner_tagline = per_match_info[f'summoner{number_list[k+5]}riotIdTagline']
                            st.write(f"<p style='text-align: center; font-size: 2;'>{per_summoner_name}#{per_summoner_tagline}</p>", unsafe_allow_html=True)
                            
                        with col6:
                            per_summoner_champion_per_match = per_match_info[f'summoner{number_list[k+5]}ChampionName']
                            champion_image_url = image_url + per_summoner_champion_per_match + '.png'
                            champion_image = requests.get(champion_image_url, stream=True)
                            st.image(champion_image.content, use_column_width = True)

                    
                
        # 각 플레이어마다의 요약 정보
        for i in range(len(summoner_list)):
            with st.container(border = True):
                st.write(f"{summoner_list[i]}")
    

    

# (same_lane_enemey[lane_list[i]][0] * 100 + same_lane_enemey[lane_list[i]][1] * 100 + same_lane_enemey[lane_list[i]][2] * -100 + same_lane_enemey[lane_list[i]][3] + same_lane_enemey[lane_list[i]][4] * 150 + same_lane_enemey[lane_list[i]][5] / 4 + same_lane_enemey[lane_list[i]][6] / 100 + same_lane_enemey[lane_list[i]][7] * 5 + same_lane_enemey[lane_list[i]][8] * 15)