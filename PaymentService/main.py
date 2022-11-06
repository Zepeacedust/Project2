import pika
from time import sleep
from retry import retry

@retry(pika.exceptions.AMQPConnectionError, delay=5, jitter=(1, 3))
def get_connection():    
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel=connection.channel()
    channel.exchange_declare(exchange='payment', exchange_type='direct')
    return channel

channel = get_connection()
while True:
    channel.basic_publish(exchange="payment", routing_key="payment.success", body="yeee")
    sleep(3)
    