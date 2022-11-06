import pika
from retry import retry
from models.credidcardmodel import CreditCardModel
from credid_card_validator import creditCardValidation
# ekki thread safe en það ætti að vikra í svona litlu kerfi
class EventSender:
    def __init__(self) -> None:
        self.channel = self.__get_connection()
    def send_message(self, order:CreditCardModel):
        self.channel.basic_publish(exchange='',
                                   routing_key='',
                                   body=order.dict())
    @retry(pika.exceptions.AMQPConnectionError, delay=5, jitter=(1, 3))
    def __get_connection(self):
        print("Validating credid card")
        connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
        channel.exchange_declare(exchange='orders', exchange_type='direct')
        channel = connection.channel()
        channel.queue_declare(queue='order_created')
        if creditCardValidation():
            print("payment success")
        else:
            print("payment failure ")
        return channel