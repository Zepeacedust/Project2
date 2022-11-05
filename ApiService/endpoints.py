from fastapi import APIRouter, Depends
import requests
router = APIRouter()


@router.get('api/orders/{id}')
async def get_order(id:int):
    return requests.get(f"orderservice/{id}")
@router.POST('api/orders')
async def set_order(orderdata):
    return requests.post('productservice', json=orderdata)
@router.get('api/merchants/{id}')
async def get_merchant():
    return requests.get(f"merchantservice/{id}")
@router.POST('api/merchants')
async def set_merchant(merchantdata):
    return requests.post('productservice', json=merchantdata)
@router.get('api/buyers/{id}')
async def get_buyer():
    return requests.get(f"buyerservice/{id}")
@router.POST('api/buyers')
async def set_buyer(buyerdata):
    return requests.post('productservice', json=buyerdata)
@router.get('api/products/{id}')
async def get_product(id:int):
    return requests.get(f"productservice/{id}")
@router.POST('api/products')
async def set_product(productdata):
    return requests.post('productservice', json=productdata)