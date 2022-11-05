from dataclasses import dataclass, asdict

@dataclass()
class MerchantModel:
    name:str
    ssn:str
    email:str
    phoneNumber:str
    allowsDiscount:bool

    def dict(self):
        return {k: str(v) for k, v in asdict(self).items()}