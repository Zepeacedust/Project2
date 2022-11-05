from fastapi import APIRouter, Depends, Response
import requests
from models.buyermodel import BuyerModel
from dependency_injector.wiring import inject, Provide
from container import Container
from errors.buyer_not_found import BuyerNotFound

router = APIRouter()



@router.get('/buyers/{id}')
@inject
async def get_buyer(id:int, response:Response, buyer_repository = Depends(Provide[Container.buyer_repository_provider])):
    buyer = None
    try:
        buyer = buyer_repository.get_buyer(id)
    except BuyerNotFound:
        response.status_code = 404
        return
    response.status_code = 201
    return buyer



@router.post('/buyers', status_code=201)
@inject
async def set_buyer(buyerdata:BuyerModel, buyer_repository = Depends(Provide[Container.buyer_repository_provider])):
    return buyer_repository.save_buyer(buyerdata)