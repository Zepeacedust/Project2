import pika
from retry import retry
from models.ordermodel import OrderModel
import json
# ekki thread safe en það ætti að vikra í svona litlu kerfi
class EventSender:
    def __init__(self) -> None:
        self.channel = self.__get_connection()
    def send_event(self, order:OrderModel, productData,orderId):
        print("sending success event",flush=True)
        self.channel.basic_publish(exchange='orders',
                                   routing_key='orders.created',
                                   body=json.dumps({"order":order.dict(), "product":productData,"id":orderId}))
    @retry(pika.exceptions.AMQPConnectionError, delay=5, jitter=(1, 3))
    def __get_connection(self):
        print("getting connection")
        connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
        channel=connection.channel()
        channel.exchange_declare(exchange='orders', exchange_type='direct')
        channel = connection.channel()
        print("got connection!")
        return channel