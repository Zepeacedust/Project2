from fastapi import APIRouter, Depends, Response, HTTPException
import requests
from models.merchantmodel import MerchantModel
from dependency_injector.wiring import inject, Provide
from container import Container
from errors.merchant_not_found import MerchantNotFound

router = APIRouter()



@router.get('/merchants/{id}',status_code=200)
@inject
async def get_merchant(id:int, merchant_repository = Depends(Provide[Container.merchant_repository_provider])):
    merchant = None
    try:
        merchant = merchant_repository.get_merchant(id)
    except MerchantNotFound:
        raise HTTPException(status_code=404, detail="Merchant does not exist")
    return merchant



@router.post('/merchants', status_code=201)
@inject
async def set_merchant(merchantdata:MerchantModel, merchant_repository = Depends(Provide[Container.merchant_repository_provider])):
    return merchant_repository.save_merchant(merchantdata)