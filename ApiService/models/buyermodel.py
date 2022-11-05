from dataclasses import dataclass, asdict

@dataclass
class BuyerModel:
    name:str
    ssn:str
    email:str
    phoneNumber:str 

    def dict(self):
        return {k: str(v) for k, v in asdict(self).items()}