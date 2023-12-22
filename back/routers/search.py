from fastapi import APIRouter, Depends
from schemas.search import Player
from services.search import PlayerService

router = APIRouter(
    prefix='/estock',
    tags=["estock"],
    responses={
        404: { "description": "Not found"}
    }
)

#id로 사용자의 전적에 대한 분석을 제공
@router.get('/get', response_model=Player)
async def get_player(player_id: str, service: PlayerService = Depends()):
    result = service.get_player(player_id)
    return result
