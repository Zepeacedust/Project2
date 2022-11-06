from fastapi import APIRouter, Depends, Response, HTTPException
import requests
from models.ordermodel import OrderModel
from dependency_injector.wiring import inject, Provide
from container import Container
from errors.order_not_found import OrderNotFound

router = APIRouter()



@router.get('/orders/{id}')
@inject
async def get_order(id:int, response:Response, order_repository = Depends(Provide[Container.order_repository_provider])):
    order = None
    try:
        order = order_repository.get_order(id)
    except OrderNotFound:
        response.status_code = 404
        return
    response.status_code = 201
    return order



@router.post('/orders', status_code=201)
@inject
async def set_order(orderdata:OrderModel, response:Response, order_repository = Depends(Provide[Container.order_repository_provider])):
    
    merchant = requests.get(f"http://merchant-service:8000/merchants/{orderdata.merchantId}")
    buyer = requests.get(f"http://buyer-service:8000/merchants/{orderdata.buyerId}")
    product = requests.get(f"http://product-service:8000/merchants/{orderdata.productId}")
    
    if merchant.status_code == 404:
        return HTTPException(status_code=400, detail="Merchant does not exist")
    if buyer.status_code == 404:
        return HTTPException(status_code=400, detail="Buyer does not exist")
    if product.status_code == 404:
        return HTTPException(status_code=400, detail="Product does not exist")
    
    
    return order_repository.save_order(orderdata)