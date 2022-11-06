from models.credidcardmodel import CreditCardModel
from errors.credit_card_not_found import CreditCardNotFound
import sqlite3
class CreditRepository:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("database/creditCard.db")
        self.cur = self.connection.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS creditCard (id INTEGER Primary key, orderId int, success boolean);")
        
    def save_credit_card(self, orderId:int, success:bool) -> int:
        self.cur.execute(f"INSERT INTO creditCard(orderId) VALUES ({orderId}, {success});")
        self.connection.commit()