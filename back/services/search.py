from fastapi import Depends

from schemas.search import Player,PlayerBase
from repository.search import PlayerRepository

class PlayerService():
    def __init__(self, repository: PlayerRepository = Depends()) -> None:
        self.repository = repository

    def get_players_match(self, player_list: list):
        duo_list = []
        for player in player_list:
            summoner = self.repository.get_player_account(player)
            duo_list.append(summoner['puuid'])
        match_set = {}
        for i in range(len(duo_list)):
            player_match = set(self.repository.get_player_match(duo_list['puuid']))
            if i==0:
                match_set = player_match
            else:
                match_set = match_set & player_match
        return match_set
    
    def get_player_info_per_match(self, player_list: list, match_id: str):
        player_info_per_match = {}
        for player in player_list:
            player_info_per_match[player] = self.repository.player_in_match_data(player_puuid=player, match_id=match_id)
        return player_info_per_match
