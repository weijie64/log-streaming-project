from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
from elasticsearch.exceptions import ApiError
import json

# Elasticsearch connection (force header compatibility for ES 8.x)
es = Elasticsearch(
    "http://localhost:9200",
    headers={
        "Accept": "application/vnd.elasticsearch+json; compatible-with=8",
        "Content-Type": "application/vnd.elasticsearch+json; compatible-with=8"
    },
    verify_certs=False
)

consumer = KafkaConsumer(
    'logs',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    group_id='log-group-1'
)

print("Consuming logs from Kafka and sending to Elasticsearch...")

for message in consumer:
    log = message.value
    try:
        es.index(index="logs", document=log)
        print(f"Indexed log: {log}")
    except ApiError as e:
        print("Failed to index document (API error):", e)
    except Exception as e:
        print("Failed to index document (other error):", e)
