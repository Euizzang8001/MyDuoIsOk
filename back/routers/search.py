from fastapi import APIRouter, Depends
from models.search import MatchInfoBase, SummonerBase
from schemas.search import match_info, summoner_info
from bson import ObjectId
from services.search import SummonerService


router = APIRouter(
    prefix='/myduoisok',
    tags=["myduoisok"],
    responses={
        404: { "description": "Not found"}
    }
)


@router.get('/get-summoner', response_model=str)
async def get_summoner_puuid(summoner: str, service: SummonerService = Depends()):
    result = service.get_summoner_puuid(summoner=summoner)
    return result

@router.get('/get-matchid') #puuid -> matchid list return
async def get_summoner_puuid(summoner_puuid:str, service: SummonerService=Depends()):
    result = service.get_match(summoner_puuid)
    return result

@router.get('/get-matchinfo')
async def get_summoner_match_id(match_id: str, service: SummonerService = Depends()):
    result = service.get_match_info(match_id = match_id)
    return result

@router.post('/append-matchinfo') #match info를 받으면 db에 저장하는 router
async def append_match_info(match_info: MatchInfoBase, service: SummonerService = Depends()):
    result = service.append_match_info(match_info = match_info)
    return result

@router.post('/append-summoner-info') #summoner table에 새로운 match data 입력
async def append_summoner_info(puuid:str, summoner_info: SummonerBase, service: SummonerService = Depends()):
    result = service.append_summoner_info(puuid = puuid, summoner_info = summoner_info)
    return result
