import streamlit as st
import requests
import datetime

back_url = 'http://127.0.0.1:8000'
get_puuid_url = back_url + 'get-player'

st.title('My Duo Is OK..? :frowning:')
    
explain1 = 'There are so many players playing with one or more friends.'
explain2 = 'We want to give you some detail information about your party!'
explain3 = 'So you can feel more excited with this info!'
st.write(explain1)
st.write(explain2)
st.write(explain3)

player = st.text_input('Write The Player Name')
search_player = st.button('Search')
player_list = player.split(', ')

match_id = []

@router.get('/get-player', response_model = str) #플레이어 이름 -> puuid get
async def get_player_puuid(player:str, service: PlayerService=Depends()):
    result = service.get_player_puuid(player = player)
    return result


if search_player: #검색하기 위해 버튼을 누르면 검색 정보를 db에 저장하고 불러오기
    for i in range(len(player_list)):
        match_list = requests(get_puuid_url, player = player_list[i])