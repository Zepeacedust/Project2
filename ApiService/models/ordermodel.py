from dataclasses import dataclass, asdict
from models.creditcardmodel import CreditCardModel

@dataclass
class OrderModel:
    productId:int
    merchantId:int
    buyerId:int

    creditCard: CreditCardModel
    
    discount: float

    def dict(self):
        return {
            "productId":self.productId,
            "merchantId":self.merchantId,
            "buyerId":self.buyerId,
            "creditCard":str(self.creditCard.dict()),
            "discount": self.discount
        }