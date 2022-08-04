from kafka import KafkaProducer
from single_transaction_generator import generate_receiver_transaction
import random
import json

topic = "projet1"
bootstrap_servers = ["localhost:9092"]

def serializer(value):
    return json.dumps(value).encode("utf-8")

data = generate_receiver_transaction(random.randint(1, 3))

producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                         value_serializer=serializer)

producer.send(topic, data)