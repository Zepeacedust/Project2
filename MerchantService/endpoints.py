from fastapi import APIRouter, Depends, Response
import requests
from models.merchantmodel import MerchantModel
from dependency_injector.wiring import inject, Provide
from container import Container
from errors.merchant_not_found import MerchantNotFound

router = APIRouter()



@router.get('/merchants/{id}')
@inject
async def get_merchant(id:int, response:Response, merchant_repository = Depends(Provide[Container.merchant_repository_provider])):
    merchant = None
    try:
        merchant = merchant_repository.get_merchant(id)
    except MerchantNotFound:
        response.status_code = 404
        return
    response.status_code = 201
    return merchant



@router.post('/merchants', status_code=201)
@inject
async def set_merchant(merchantdata:MerchantModel, merchant_repository = Depends(Provide[Container.merchant_repository_provider])):
    return merchant_repository.save_merchant(merchantdata)