from fastapi import APIRouter, Depends, Response, HTTPException
import requests
from models.productmodel import ProductModel
from dependency_injector.wiring import inject, Provide
from container import Container
from errors.product_not_found import ProductNotFound

router = APIRouter()

from models.reserverequestmodel import ReserveRequestModel


@router.get('/products/{id}', status_code=200)
@inject
async def get_product(id:int, product_repository = Depends(Provide[Container.product_repository_provider])):
    order = None
    try:
        order = product_repository.get_product(id)
    except ProductNotFound:
        raise HTTPException(status_code=404, detail="Product does not exist")
    return order



@router.post('/products', status_code=201)
@inject
async def set_product(productdata:ProductModel, product_repository = Depends(Provide[Container.product_repository_provider])):
    return product_repository.save_product(productdata)

@router.post('/products/reserve', status_code=200)
@inject
async def reserve_product(reserve_request:ReserveRequestModel, product_repository = Depends(Provide[Container.product_repository_provider])):
    return product_repository.update_product(reserve_request.productId,1,0)
