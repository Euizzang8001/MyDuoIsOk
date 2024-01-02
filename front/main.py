import streamlit as st
import requests
import datetime

back_url = 'http://127.0.0.1:8000/myduoisok'
get_puuid_url = back_url + '/get-summoner'
get_match_list_url = back_url + '/get-matchid'
get_match_info_url = back_url + '/get-matchinfo'
check_match_in_db_url = back_url + '/check-match-in-db'

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

summoner_info_per_match_dict = {}

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
        #db에 있는지 확인하고
        match_in_db= requests.get(check_match_in_db_url, params={'match_id': match})
        if not match_in_db:
            #정보 라이엇으로부터 가져오고
            match_info = requests.get(get_match_info_url, params={'match_id': match}).json()
            #db에 저장하고
            
        #db에서 match정보 불러오기
        #db에서 match에 있는 소환사 10명의 정보 불러오기 
        #champion.json나 다른 정보들에 따라 코드 작성
            
    
    

    

        