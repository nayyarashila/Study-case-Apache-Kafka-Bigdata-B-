from kafka import KafkaProducer
import json, time, random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

gudang_ids = ['G1', 'G2', 'G3']

while True:
    for gudang in gudang_ids:
        data = {"gudang_id": gudang, "suhu": random.randint(75, 85)}
        producer.send('sensor-suhu-gudang', data)
        print("Sent Suhu:", data)
    time.sleep(1)
