print("hello world",flush=True)

import pika
from retry import retry
from event_sender import EventSender
import json


@retry(pika.exceptions.AMQPConnectionError, delay=5, jitter=(1, 3))
def get_connection():    
    print("Payment service: attempting connection",flush=True)
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel=connection.channel()
    channel.exchange_declare(exchange='orders', exchange_type='direct')
    channel.queue_declare(queue="orders")
    channel.queue_bind(queue="orders", exchange="orders" ,routing_key="orders.created")
    print("Payment service: got connection",flush=True)
    return channel
def callback(ch, method, properties, body):
    print("recieved message")
    print(json.loads(body),flush=True)
    
print("Payment Service:starting", flush=True) 
    
channel = get_connection()

sender = EventSender()

channel.basic_consume(queue='orders', on_message_callback=callback, auto_ack=True)
print("Payment Service: started") 
channel.start_consuming()