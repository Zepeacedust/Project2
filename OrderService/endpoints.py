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
        raise HTTPException(status_code=404, detail="Order does not exist")
    response.status_code = 201
    product = requests.get(f"http://product-service:8000/merchants/{id}").json()
    return {
        "productId": order.productId,
        "merchantID": order.merchantId,
        "buyerId":order.buyerId,
        "cardNumber":"************" + order.creditCard.cardNumber[-4:],
        "totalPrice":product["price"] * order.discount
    }



@router.post('/orders', status_code=201)
@inject
async def set_order(orderdata:OrderModel, response:Response, order_repository = Depends(Provide[Container.order_repository_provider]), event_sender = Depends(Provide[Container.event_sender_provider])):
    
    merchant = requests.get(f"http://merchant-service:8000/merchants/{orderdata.merchantId}")
    buyer = requests.get(f"http://buyer-service:8000/buyers/{orderdata.buyerId}")
    product = requests.get(f"http://inventory-service:8000/product/{orderdata.productId}")
    
    if merchant.status_code == 404:
        raise HTTPException(status_code=400, detail="Merchant does not exist")
    if buyer.status_code == 404:
        raise HTTPException(status_code=400, detail="Buyer does not exist")
    if product.status_code == 404:
        raise HTTPException(status_code=400, detail="Product does not exist")
    
    product_data = product.json()
    
    if product_data["quantity"] -product_data["reserved"] < 1:
        raise HTTPException(status_code=400, detail="Product is sold out")
    
    if product_data["merchantId"] != orderdata.merchantId:
        raise HTTPException(status_code=400, detail="Product does not belong to merchant")
    
    merchant_data = merchant.json()
    if merchant_data["allowsDiscount"] == False and (orderdata.discount != 0 or orderdata.discount != None):
        raise HTTPException(status_code=400, detail="Merchant does not allow discount")
    
    
    requests.post(f"http://inventory-service:8000/product/reserve",json={"productId":orderdata.productId})
    event_sender.send_event(orderdata, product_data)
    return order_repository.save_order(orderdata)