from kafka import KafkaConsumer
import json

topic = "projet1"
bootstrap_servers = ["localhost:9092"]

def deserializing(value):
    json_data = value.decode("utf-8")
    return json.loads(json_data)

consumer = KafkaConsumer(topic,
                         value_deserializer=deserializing,
                         bootstrap_servers=bootstrap_servers)

for message in consumer:
    print(message)