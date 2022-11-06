from dataclasses import dataclass, asdict

@dataclass
class CreditCardModel:
    
    cardNumber: str
    expirationMonth : int
    expirationYear: int
    cvc: int

    def dict(self):
        return {k: v for k, v in asdict(self).items()}