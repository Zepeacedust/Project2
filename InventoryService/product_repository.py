from models.productmodel import ProductModel
from errors.product_not_found import ProductNotFound
import sqlite3
class ProductRepository:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("database/products.db")
        self.cur = self.connection.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER Primary key, merchantId int, productName varchar(2000), price float, quantity int, reserved int);")
        
    def save_product(self, product:ProductModel) -> int:
        self.cur.execute(f"INSERT INTO products(merchantId, productName, price, quantity, reserved) VALUES ({product.merchantId}, '{product.productName}', {product.price}, {product.quantity}, {product.reserved});")
        self.connection.commit()
        result = self.cur.execute("SELECT MAX(id) from products;")
        return result.fetchone()[0]

    def get_product(self, id: int) -> ProductModel:
        # TODO: return message with id from storage
        result = self.cur.execute(f"select merchantId, productName, price, quantity, reserved from products where id={id};")
        data = result.fetchone()
        if data == None:
            raise ProductNotFound()
        else:
            return ProductModel(*data)
    
    def update_product(self,id, reserved_change, quantity_change):
        result = self.cur.execute(f"select reserved, quantity from products where id ={id};")
        data = result.fetchone()
        self.cur.execute(f"UPDATE products SET reserved={data[0]+reserved_change}, quantity={data[1]+quantity_change} where id={id};")
        self.connection.commit()
        
        
    def __del__(self):
        self.connection.commit()