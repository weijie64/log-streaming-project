from kafka import KafkaProducer
import time
import random
from datetime import datetime

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: v.encode('utf-8')
)

levels = ['INFO', 'ERROR', 'WARN']
endpoints = ['/api/user', '/api/order', '/api/cart']
messages = ['login success', 'failed to connect', 'timeout', 'slow response']

print("Sending logs to Kafka topic: 'logs'...")

while True:
    log = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {random.choice(levels)} {random.choice(endpoints)} {random.choice(messages)}"
    producer.send('logs', value=log)
    print(f"[Sent] {log}")
    time.sleep(1)
