# Log Streaming Project

This project demonstrates a simple **log streaming pipeline** using **Apache Kafka**, **Python**, and **Elasticsearch**. It simulates log generation, streams logs to Kafka, consumes them, and stores them in Elasticsearch for real-time search and analytics.

![Uploading image.png…]()

---

## Components

- **Log Producer (Python)**: Simulates log data and sends it to a Kafka topic.
- **Kafka (Apache Kafka)**: Handles streaming and message brokering.
- **Kafka Consumer (Python)**: Consumes logs from Kafka and pushes them to Elasticsearch.
- **Elasticsearch**: Stores and indexes log data for querying.
- **Kibana**: Used for visualizing log data.

---

## Architecture

```text
[ Log Producer ] ---> [ Kafka Topic ] ---> [ Kafka Consumer ] ---> [ Elasticsearch ]
