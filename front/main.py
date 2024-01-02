import streamlit as st
import requests
import datetime

back_url = 'http://127.0.0.1:8000/myduoisok'
get_puuid_url = back_url + '/get-player'
get_match_list_url = back_url + '/get-matchid'
get_match_info_url = back_url + '/get-matchinfo'

st.title('My Duo Is OK..? :frowning:')
    
explain1 = 'There are so many players playing with one or more friends.'
explain2 = 'We want to give you some detail information about your party!'
explain3 = 'So you can feel more excited with this info!'
st.write(explain1)
st.write(explain2)
st.write(explain3)

player = st.text_input('Write The Player Name')
search_player = st.button('Search')
player_nospace = ''.join(i for i in player if not i.isspace())
player_list = list(player_nospace.split(','))

player_puuid_list = []

match_id_list = []

player_info_per_match_dict = {}

if search_player: #검색하기 위해 버튼을 누르면 검색 정보를 db에 저장하고 불러오기
    for player_name in player_list:
        player_puuid = requests.get(get_puuid_url, params={'player': player_name}).json()
        player_puuid_list.append(player_puuid)
        if len(match_id_list) == 0:
            match_id_list = requests.get(get_match_list_url, params={'player_puuid': player_puuid}).json()
        else:
            match_id_list = list(set(match_id_list) & set(requests.get(get_match_list_url, params={'player_puuid': player_puuid}).json()))

for match in match_id_list:
    
    
    

    

        