import pika
from retry import retry
from event_sender import EventSender
import json

from credit_card_validator import creditCardValidation

from payment_repository import CreditRepository

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
    print("recieved message",flush=True)
    
    data =json.loads(body) 
    
    if creditCardValidation(data["order"]["creditCard"]["cardNumber"],data["order"]["creditCard"]["expirationMonth"],data["order"]["creditCard"]["expirationYear"],data["order"]["creditCard"]["cvc"]):
        sender.success_message(json.dumps({"id":data["order"]["productId"],"success":True}))
        repo.save_credit_card(data["id"],True)
    else:
        sender.fail_message(json.dumps({"id":data["order"]["productId"],"success":False}))
        repo.save_credit_card(data["id"],False)
    
    
print("Payment Service:starting", flush=True) 
    
channel = get_connection()

sender = EventSender()
repo = CreditRepository()

channel.basic_consume(queue='orders', on_message_callback=callback, auto_ack=True)
print("Payment Service: started") 
channel.start_consuming()