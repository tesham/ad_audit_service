import logging

import pika
import json
from threading import Thread

from audit.models import Audit
from django.conf import settings

logging.basicConfig(level=logging.DEBUG)

def callback(ch, method, properties, body):
    message = json.loads(body)
    print("Received message:", message)

    # Process the message , inserting data to audit table

    audit = Audit(
        user=message.get('user'),
        session_id=message.get('session_id'),
        module=message.get('module'),
        label=message.get('label'),
        action=message.get('action'),
        ip=message.get('ip')
    )
    audit.save()

    print('audit data saved')

def start_consumer(queue_name):
    # connection = pika.BlockingConnection(pika.ConnectionParameters(settings.RABBITMQ_HOST))
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters('rabbitmq', 5672, '/', credentials=pika.PlainCredentials('guest', 'guest')))

        channel = connection.channel()
        channel.queue_declare(queue=queue_name, durable=True)
        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
        print('Waiting for messages...')
        channel.start_consuming()

    except Exception as e:
        print(f"Failed to connect to RabbitMQ: {e}")

def run_consumer(queue_name):
    thread = Thread(target=start_consumer, args=(queue_name,))
    thread.start()