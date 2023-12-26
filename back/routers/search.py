from fastapi import APIRouter, Depends
from schemas.search import Player, PlayerBase
from services.search import PlayerService

router = APIRouter(
    prefix='/myduoisok',
    tags=["myduoisok"],
    responses={
        404: { "description": "Not found"}
    }
)


@router.get('/get-player', response_model = str)
async def get_player_puuid(player:str, service: PlayerService=Depends()):
    result = service.get_player_puuid(player = player)
    return result

@router.get('/get-matchid', response_model = list)
async def get_player_puuid(player_puuid:str, service: PlayerService=Depends()):
    result = service.get_match(player_puuid)
    return result

#소환사 이름들이 같이 있는 match들의 id 정보 제공
@router.post('/post-matchid', response_model=list)
async def get_player_match_id(player: str, service: PlayerService = Depends()):
    result = service.get_players_match(player)
    return result

@router.get('/get-playerinfo-permatch', response_model=dict)
async def get_player_match_id(players: list, match_id: str, service: PlayerService = Depends()):
    result = service.get_player_info_per_match(player_list = players, match_id = match_id)
    return result