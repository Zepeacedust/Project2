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
        return {k: str(v) for k, v in asdict(self).items()}