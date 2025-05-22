from kafka import KafkaConsumer
import json
import time

consumer = KafkaConsumer(
    'sensor-suhu-gudang',
    'sensor-kelembaban-gudang',
    bootstrap_servers='kafka:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    group_id='gudang-consumer'
)

print("Consumer filter with join is running...")

# Simpan data terbaru per gudang
suhu_data = {}
kelembaban_data = {}

# Window duration dalam detik
window_duration = 10
last_check_time = time.time()

def cek_status(suhu, kelembaban):
    if suhu > 80 and kelembaban > 70:
        return "[PERINGATAN KRITIS]\nStatus: Bahaya tinggi! Barang berisiko rusak"
    elif suhu > 80:
        return "Status: Suhu tinggi, kelembaban normal"
    elif kelembaban > 70:
        return "Status: Kelembaban tinggi, suhu aman"
    else:
        return "Status: Aman"

while True:
    for message in consumer:
        topic = message.topic
        data = message.value
        gudang_id = data['gudang_id']

        if topic == 'sensor-suhu-gudang':
            suhu_data[gudang_id] = data['suhu']
        elif topic == 'sensor-kelembaban-gudang':
            kelembaban_data[gudang_id] = data['kelembaban']

        # Check setiap window_duration detik
        current_time = time.time()
        if current_time - last_check_time >= window_duration:
            last_check_time = current_time
            print("\nStatus gabungan setiap 10 detik:")
            # Gabungkan gudang yang ada di suhu atau kelembaban
            semua_gudang = set(suhu_data.keys()) | set(kelembaban_data.keys())

            for gudang in semua_gudang:
                suhu = suhu_data.get(gudang, "N/A")
                kelembaban = kelembaban_data.get(gudang, "N/A")

                print(f"Gudang {gudang}:")
                print(f"- Suhu: {suhu if suhu != 'N/A' else '-'}°C")
                print(f"- Kelembaban: {kelembaban if kelembaban != 'N/A' else '-'}%")

                # Kalau salah satu data ada dan bukan 'N/A', cek status
                if suhu != "N/A" and kelembaban != "N/A":
                    status = cek_status(suhu, kelembaban)
                elif suhu != "N/A":
                    status = "Status: Suhu terdeteksi, data kelembaban tidak ada"
                elif kelembaban != "N/A":
                    status = "Status: Kelembaban terdeteksi, data suhu tidak ada"
                else:
                    status = "Status: Data tidak tersedia"

                print(status)
            print("-" * 30)