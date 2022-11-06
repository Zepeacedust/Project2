from container import Container
import pika, retry

class EventWatcher:
    def __init__(self) -> None:
        self.repository = Container.product_repository_provider()
        self.channel = self.__get_connection()

        self.channel.basic_consume(queue='message', on_message_callback=self.callback, auto_ack=True)
        self.channel.start_consuming()
    
    def callback(self,ch, method, properties, body):
        pass
    
    @retry(pika.exceptions.AMQPConnectionError, delay=5, jitter=(1, 3))
    def __get_connection(self):
        print("Attempting to get connection...")
        connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
        channel = connection.channel()
        channel.queue_declare(queue='inventory')
        channel.queue_bind(exchange="payment")
        print("got connection!")
        return channel
    