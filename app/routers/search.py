from fastapi import APIRouter, Depends
from models.search import MatchInfoBase, SummonerBase
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
async def get_summoner_matchid(summoner_puuid:str, service: SummonerService=Depends()):
    result = service.get_match(summoner_puuid)
    return result

@router.get('/get-matchinfo')
async def get_match_info(match_id: str, service: SummonerService = Depends()):
    result = service.get_match_info(match_id = match_id)
    return result

@router.post('/append-matchinfo') #match info를 받으면 db에 저장하는 router
async def append_match_info(match_info: MatchInfoBase, service: SummonerService = Depends()):
    result = service.append_match_info(match_info = match_info)
    return result

@router.put('/append-summonerinfo/{puuid}') #summoner table에 새로운 match data 입력
async def append_summoner_info( puuid: str, summoner_info: SummonerBase, service: SummonerService = Depends()):
    result = service.append_summoner_info(puuid = puuid, summoner_info = summoner_info)
    return result

@router.delete('/delete{matchId}')
async def delete_match_info(match_id: str, service : SummonerService = Depends()):
    result = service.delete_match_info(match_id = match_id)
    return result

@router.delete('/delete/{matchId}/{puuid}')
async def delete_summoner_match_info(match_id: str, puuid: str, service: SummonerService = Depends()):
    result = service.delete_summoner_match_info(match_id=match_id, puuid=puuid)
    return result

@router.get('/check-match-in-db')
async def check_match_in_db(match_id: str, service : SummonerService=Depends()):
    result = service.check_match_in_db(match_id = match_id)
    if result == True:
        return True
    else:
        return False

@router.get('/get-summonerinfo-from-db/{puuid}/{match_id}')
async def get_summoner_from_db(puuid: str, match_id: str, service: SummonerService = Depends()):
    result = service.get_summoner_from_db(puuid = puuid, match_id = match_id)
    return result

@router.get('/get-matchinfo-from-db/{matchId}')
async def get_match_from_db(match_id: str, service: SummonerService = Depends()):
    result = service.get_match_from_db(match_id = match_id)
    return result