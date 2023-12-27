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


@router.get('/get-player', response_model = str) #플레이어 이름 -> puuid get
async def get_player_puuid(player:str, service: PlayerService=Depends()):
    result = service.get_player_puuid(player = player)
    return result

@router.get('/get-matchid', response_model = list) #puuid -> matchid list return
async def get_player_puuid(player_puuid:str, service: PlayerService=Depends()):
    result = service.get_match(player_puuid)
    return result

@router.get('/get-matchinfo', response_model=dict)
async def get_player_match_id(match_id: str, service: PlayerService = Depends()):
    result = service.get_match_info(match_id = match_id)
    return result