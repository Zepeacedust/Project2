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
            "productId":str(self.productId),
            "merchantId":str(self.merchantId),
            "buyerId":str(self.buyerId),
            "creditCard":str(self.creditCard.dict()),
            "discount": str(self.discount)
        }