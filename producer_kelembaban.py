from kafka import KafkaProducer
import json, time, random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

gudang_ids = ['G1', 'G2', 'G3']

while True:
    for gudang in gudang_ids:
        data = {"gudang_id": gudang, "kelembaban": random.randint(65, 75)}
        producer.send('sensor-kelembaban-gudang', data)
        print("Sent Kelembaban:", data)
    time.sleep(1)
