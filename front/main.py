import streamlit as st

st.title('My Duo Is OK..? :frowning:')
    
explain1 = 'There are so many players playing with one or more friends.'
explain2 = 'We want to give you some detail information about your party!'
explain3 = 'So you can feel more excited with this info!'
st.write(explain1)
st.write(explain2)
st.write(explain3)

with st.form("Player"):
    player = st.text_input('Write The Player Name')
    search_player = st.form_submit_button('Search')

    if search_player: #검색하기 위해 버튼을 누르면 검색 정보를 db에 저장하고 불러오기
        True