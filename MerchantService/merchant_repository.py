from models.merchantmodel import MerchantModel
from errors.merchant_not_found import MerchantNotFound
import sqlite3
class MerchantRepository:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("database/merchants.db")
        self.cur = self.connection.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS merchants (id INTEGER Primary key , name VARCHAR(2000), email VARCHAR(2000), ssn VARCHAR(2000), phoneNumber VARCHAR(2000), allowsDiscount boolean);")
        
    def save_merchant(self, merchant:MerchantModel) -> int:
        self.cur.execute(f"INSERT INTO merchants(name, email, ssn, phoneNumber,allowsDiscount) VALUES ('{merchant.name}', '{merchant.email}', '{merchant.ssn}', '{merchant.phoneNumber}',{merchant.allowsDiscount});")
        self.connection.commit()
        result = self.cur.execute("SELECT MAX(id) from merchants;")
        return result.fetchone()[0]

    def get_merchant(self, id: int) -> MerchantModel:
        # TODO: return message with id from storage
        result = self.cur.execute(f"select name,ssn,email,phoneNumber,allowsDiscount from merchants where id={id};")
        data = result.fetchone()
        if data == None:
            raise MerchantNotFound()
        else:
            return MerchantModel(*data)
    def __del__(self):
        self.connection.commit()