from dataclasses import dataclass, asdict
from typing import Optional
@dataclass
class ProductModel:
    
    merchantId: int
    productName : str
    price: float
    quantity: int
    reserved: Optional[int] = 0

    def dict(self):
        return {k: v for k, v in asdict(self).items()}