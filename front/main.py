import streamlit as st
import requests
import datetime

apikey="RGAPI-626d57b2-73d2-463a-9252-5d3b2f413799"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": apikey
}

st.title('My Duo Is OK..? :frowning:')
    
explain1 = 'There are so many players playing with one or more friends.'
explain2 = 'We want to give you some detail information about your party!'
explain3 = 'So you can feel more excited with this info!'
st.write(explain1)
st.write(explain2)
st.write(explain3)

player = st.text_input('Write The Player Name')
search_player = st.button('Search')
player= player.replace('','%20')
request_url = f'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{player}'
result = requests.get(request_url, headers=headers)
player_info = result.json()

if search_player: #검색하기 위해 버튼을 누르면 검색 정보를 db에 저장하고 불러오기
    st.write(player_info)