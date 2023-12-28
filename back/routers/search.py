from fastapi import APIRouter, Depends
from schemas.search import MatchInfoBase, Summoner, SummonerBase
from services.search import SummonerService

router = APIRouter(
    prefix='/myduoisok',
    tags=["myduoisok"],
    responses={
        404: { "description": "Not found"}
    }
)


@router.get('/get-summoner', response_model = str) #플레이어 이름 -> puuid get
async def get_summoner_puuid(summoner:str, service: SummonerService=Depends()):
    result = service.get_summoner_puuid(summoner = summoner)
    return result

@router.get('/get-matchid', response_model = list) #puuid -> matchid list return
async def get_summoner_puuid(summoner_puuid:str, service: SummonerService=Depends()):
    result = service.get_match(summoner_puuid)
    return result

@router.get('/get-matchinfo', response_model=dict)
async def get_summoner_match_id(match_id: str, service: SummonerService = Depends()):
    result = service.get_match_info(match_id = match_id)
    return result

@router.post('/append-matchinfo', response_model = MatchInfoBase) #match info를 받으면 db에 저장하는 router
async def append_match_info(match_info: MatchInfoBase, service: SummonerService = Depends()):
    result = service.append_match_info(match_info = match_info)
    return result

@router.create('/create-summoner-table', response_model = Summoner) #summoner가 새로 들어오면 summoner에 대한 table을 새로 생성
async def create_summoner_table(puuid: str, service: SummonerService = Depends()):
    result = service.create_summoner_table(puuid = puuid)
    return result

@router.post('/append-summoner-info', response_model = Summoner) #summoner table에 새로운 match data 입력
async def append_summoner_info(puuid:str, summoner_info: SummonerBase, service: SummonerService = Depends()):
    result = service.append_summoner_info(puuid = puuid, summoner_info = summoner_info)
    return result