from container import Container
import pika
from retry import retry
import json
class EventWatcher:
    def __init__(self) -> None:
        self.repository = Container.product_repository_provider()
        self.channel = self.__get_connection()
    
    def callback(self,ch, method, properties, body):
        data=json.loads(body)
        if data["success"]:
            self.repository.update_product(data["id"], -1,-1)
        else:
            self.repository.update_product(data["id"], -1, 0)
            
    
    def start(self):
        print("we eating good tonight",flush=True)
        print(type(self))
        self.channel.basic_consume(queue='inventory', on_message_callback=self.callback, auto_ack=True)
        self.channel.start_consuming()
        
    
    @retry(pika.exceptions.AMQPConnectionError, delay=5, jitter=(1, 3))
    def __get_connection(self):
        print("Attempting to get connection...", flush=True)
        print(self)
        connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
        channel = connection.channel()
        channel.exchange_declare(exchange="payment")
        channel.queue_declare(queue='inventory')
        channel.queue_bind(queue="inventory",exchange="payment",routing_key="payment.success")
        channel.queue_bind(queue="inventory",exchange="payment",routing_key="payment.failure")
        print("got connection!",flush=True)
        return channel
    