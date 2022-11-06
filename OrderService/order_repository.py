from models.ordermodel import OrderModel
from models.creditcardmodel import CreditCardModel
from errors.order_not_found import OrderNotFound
import sqlite3
class OrderRepository:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("database/orders.db")
        self.cur = self.connection.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS orders (id INTEGER Primary key , productId int, buyerId int,merchantId int, cardnumber VARCHAR(2000), expirationMonth int, expirationYear int, cvc int, discount float );")
        
    def save_order(self, order:OrderModel) -> int:
        self.cur.execute(f"INSERT INTO orders(productId, buyerId, merchantId, cardnumber, expirationMonth, expirationYear, cvc, discount) VALUES ({order.productId}, {order.buyerId},{order.merchantId}, '{order.creditCard.cardNumber}', {order.creditCard.expirationMonth}, {order.creditCard.expirationYear}, {order.creditCard.cvc}, {order.discount});")
        self.connection.commit()
        result = self.cur.execute("SELECT MAX(id) from orders;")
        return result.fetchone()[0]

    def get_order(self, id: int) -> OrderModel:
        # TODO: return message with id from storage
        result = self.cur.execute(f"select productId, buyerId, merchantId, cardnumber, expirationMonth, expirationYear, cvc, discount from orders where id={id};")
        data = result.fetchone()
        if data == None:
            raise OrderNotFound()
        else:
            card = CreditCardModel(*data[3:7])
            return OrderModel(data[0],data[1],data[2], card,data[7])
        
    def __del__(self):
        self.connection.commit()