from dataclasses import dataclass

@dataclass
class MerchantModel:
    name:str
    ssn:str
    email:str
    phoneNumber:str
    allowsDiscount:bool
