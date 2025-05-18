import logging
import random
import time
from kafka import KafkaProducer
import json
from datetime import datetime

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Simulated log messages
log_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
messages = {
    "DEBUG": ["Debugging connection", "Checking config", "Entering method X"],
    "INFO": ["User logged in", "Request received", "Process started"],
    "WARNING": ["Disk usage high", "Slow response", "Retrying connection"],
    "ERROR": ["File not found", "Database error", "Unhandled exception"],
    "CRITICAL": ["System crash", "Memory leak detected", "Kernel panic"]
}

def generate_random_log():
    level = random.choices(log_levels, weights=[0.2, 0.3, 0.2, 0.2, 0.1])[0]
    message = random.choice(messages[level])
    return {
        "timestamp": datetime.utcnow().isoformat() + "Z",  # ISO format with UTC indicator
        "level": level,
        "message": message,
        "app": "my-python-service"
    }

while True:
    log_entry = generate_random_log()
    producer.send("logs", log_entry)
    print(f"Sent: {log_entry}")
    time.sleep(random.uniform(0.5, 2))  # simulate logs at random intervals
