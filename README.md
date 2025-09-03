# Log Streaming Project

This project demonstrates a simple **log streaming pipeline** using **Apache Kafka**, **Python**, and **Elasticsearch**. It simulates log generation, streams logs to Kafka, consumes them, and stores them in Elasticsearch for real-time search and analytics.

<img width="914" height="259" alt="Snipaste_2025-09-03_15-52-32" src="https://github.com/user-attachments/assets/5ba6a0a5-7409-4dd3-a8f9-751688281451" />

---

## Components

- **Log Producer (Python)**: Simulates log data and sends it to a Kafka topic.
- **Kafka (Apache Kafka)**: Handles streaming and message brokering.
- **Kafka Consumer (Python)**: Consumes logs from Kafka and pushes them to Elasticsearch.
- **Elasticsearch**: Stores and indexes log data for querying.
- **Kibana**: Used for visualizing log data.
---

## Data visualization 

This dashboard is able to track live error logs and visualize number of errors over time using Kibana.

<img width="1436" height="722" alt="Snipaste_2025-09-03_15-33-32" src="https://github.com/user-attachments/assets/f4aea67e-3bbe-433c-9c19-b7cbbf3bd86d" />
