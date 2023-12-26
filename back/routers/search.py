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

#id로 사용자의 전적에 대한 분석을 제공
@router.get('/get-matchid', response_model=set)
async def get_player_match_id(players: list, service: PlayerService = Depends()):
    result = service.get_players_match(players)
    return result

@router.get('/get-playerinfo-permatch', response_model=dict)
async def get_player_match_id(players: list,match_id: str, service: PlayerService = Depends()):
    result = service.get_player_info_per_match(player_list = players, match_id=match_id)
    return result

