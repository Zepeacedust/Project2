import pika
from retry import retry
# ekki thread safe en það ætti að vikra í svona litlu kerfi
class EventSender:
    def __init__(self) -> None:
        self.channel = self.__get_connection()
    def success_message(self, body):
        print("sending success event", flush=True)
        self.channel.basic_publish(exchange='payment',
                                   routing_key='payment.success',
                                   body=body)
        
    def fail_message(self,body):
        print("sending fail event", flush=True)
        self.channel.basic_publish(exchange='payment',
                                   routing_key='payment.failure',
                                   body=body)
    @retry(pika.exceptions.AMQPConnectionError, delay=5, jitter=(1, 3))
    def __get_connection(self):
        print("getting connection")
        connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
        channel=connection.channel()
        channel.exchange_declare(exchange='payment', exchange_type='direct')
        channel = connection.channel()
        channel.queue_declare(queue='payment')
        print("got connection!")
        return channel