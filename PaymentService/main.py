import pika
from retry import retry
from event_sender import EventSender
@retry(pika.exceptions.AMQPConnectionError, delay=5, jitter=(1, 3))
def get_connection():    
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel=connection.channel()
    channel.exchange_declare(exchange='orders', exchange_type='direct')
    channel.queue_declare(queue="orders")
    channel.queue_bind(queue="orders", exchange="orders" ,routing_key="orders.created")
    return channel
def callback(ch, method, properties, body):
    print(body)
channel = get_connection()

sender = EventSender()

channel.basic_consume(queue='orders', on_message_callback=callback, auto_ack=True)
channel.start_consuming()