from dataclasses import dataclass, asdict
from typing import Optional
@dataclass
class ReserveRequestModel:
    
    productId:int
    
    def dict(self):
        return {k: str(v) for k, v in asdict(self).items()}