from fastapi import APIRouter, Depends, Response
import requests

router = APIRouter()


@router.get('api/orders/{id}')
async def get_order(id: int,response:Response):
    return_data = requests.get(f"orderservice/{id}").json()
    response.status_code = return_data.status_code
    return return_data.json()


@router.POST('api/orders')
async def set_order(orderdata,response:Response):
    return_data = requests.post('productservice', json=orderdata).json()
    response.status_code = return_data.status_code
    return return_data.json()


@router.get('api/merchants/{id}')
async def get_merchant(id:int,response:Response):
    return_data = requests.get(f"merchantservice/{id}").json()
    response.status_code = return_data.status_code
    return return_data.json()


@router.POST('api/merchants')
async def set_merchant(merchantdata,response:Response):
    return_data = requests.post('productservice', json=merchantdata).json()
    response.status_code = return_data.status_code
    return return_data.json()


@router.get('api/buyers/{id}')
async def get_buyer(id:int, response:Response):
    return_data = requests.get(f"buyerservice/{id}").json()
    response.status_code = return_data.status_code
    return return_data.json()



@router.POST('api/buyers')
async def set_buyer(buyerdata, response: Response):
    return_data = requests.post('productservice', json=buyerdata)
    response.status_code = return_data.status_code
    return return_data.json()


@router.get('api/products/{id}')
async def get_product(id: int, response: Response):
    return_data = requests.get(f"productservice/{id}")
    response.status_code = return_data.status_code
    return return_data.json()


@router.POST('api/products')
async def set_product(productdata, response: Response):
    return_data = requests.post('productservice', json=productdata)
    response.status_code = return_data.status_code
    return return_data.json()