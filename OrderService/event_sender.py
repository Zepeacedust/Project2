import pika
from retry import retry
from models.ordermodel import OrderModel
# ekki thread safe en það ætti að vikra í svona litlu kerfi
class EventSender:
    def __init__(self) -> None:
        self.channel = self.__get_connection()
    def send_message(self, order:OrderModel, productData):
        self.channel.basic_publish(exchange='order',
                                   routing_key='order.created',
                                   body={"order":order.dict(), "product":productData})
    @retry(pika.exceptions.AMQPConnectionError, delay=5, jitter=(1, 3))
    def __get_connection(self):
        print("getting connection")
        connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
        channel.exchange_declare(exchange='orders', exchange_type='direct')
        channel = connection.channel()
        channel.queue_declare(queue='order_created')
        print("got connection!")
        return channel