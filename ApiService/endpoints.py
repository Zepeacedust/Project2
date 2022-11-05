from fastapi import APIRouter, Depends, Response
import requests

from models.merchantmodel import MerchantModel
from models.buyermodel import BuyerModel
router = APIRouter()


@router.get('/api/orders/{id}')
async def get_order(id: int,response:Response):
    return_data = requests.get(f"http://order-service:8000/orders/{id}")
    response.status_code = return_data.status_code
    return return_data.json()


@router.post('/api/orders')
async def set_order(orderdata,response:Response):
    return_data = requests.post('http://order-service:8000/orders', json=orderdata)
    response.status_code = return_data.status_code
    return return_data.json()


@router.get('/api/merchants/{id}')
async def get_merchant(id:int,response:Response):
    return_data = requests.get(f"http://merchant-service:8000/merchants/{id}")
    response.status_code = return_data.status_code
    return return_data.json()


@router.post('/api/merchants')
async def set_merchant(merchantmodel:MerchantModel,response:Response):
    return_data = requests.post('http://merchant-service:8000/merchants', json=merchantmodel.dict())
    response.status_code = return_data.status_code
    return return_data.json()


@router.get('/api/buyers/{id}')
async def get_buyer(id:int, response:Response):
    return_data = requests.get(f"http://buyer-service:8000/buyers/{id}")
    response.status_code = return_data.status_code
    return return_data.json()



@router.post('/api/buyers')
async def set_buyer(buyerdata:BuyerModel, response: Response):
    return_data = requests.post('http://buyer-service:8000/buyers', json=buyerdata.dict())
    response.status_code = return_data.status_code
    return return_data.json()


@router.get('/api/products/{id}')
async def get_product(id: int, response: Response):
    return_data = requests.get(f"http://product-service:8000/products/{id}")
    response.status_code = return_data.status_code
    return return_data.json()


@router.post('/api/products')
async def set_product(productdata, response: Response):
    return_data = requests.post('http://product-service:8000/products', json=productdata.dict())
    response.status_code = return_data.status_code
    return return_data.json()