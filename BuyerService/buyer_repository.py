from models.buyermodel import BuyerModel
from errors.buyer_not_found import BuyerNotFound
import sqlite3
class BuyerRepository:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("database/buyers.db")
        self.cur = self.connection.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS buyers (id INTEGER Primary key , name VARCHAR(2000), email VARCHAR(2000), ssn VARCHAR(2000), phoneNumber VARCHAR(2000));")
        
    def save_buyer(self, buyer:BuyerModel) -> int:
        self.cur.execute(f"INSERT INTO buyers(name, email, ssn, phoneNumber) VALUES ('{buyer.name}', '{buyer.email}', '{buyer.ssn}', '{buyer.phoneNumber}');")
        self.connection.commit()
        result = self.cur.execute("SELECT MAX(id) from buyers;")
        return result.fetchone()[0]

    def get_buyer(self, id: int) -> BuyerModel:
        # TODO: return message with id from storage
        result = self.cur.execute(f"select name,ssn,email,phoneNumber from buyers where id={id};")
        data = result.fetchone()
        if data == None:
            raise BuyerNotFound()
        else:
            return BuyerModel(*data)
    def __del__(self):
        self.connection.commit()