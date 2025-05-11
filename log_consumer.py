from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'logs',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',   
    enable_auto_commit=True,
    group_id='log-consumer-group',
    value_deserializer=lambda x: x.decode('utf-8')
)

print("Listening for messages on 'logs' topic...")
for message in consumer:
    print(f"[RECEIVED] {message.value}")
    