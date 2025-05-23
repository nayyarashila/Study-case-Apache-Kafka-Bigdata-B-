# Study-case-Apache-Kafka-Bigdata-B-

| Nama Lengkap              | NRP           |
| :-----------------------: | :-----------: |
| Nayyara Ashila        | 5027231083    |


## Setup Kafka dan Zookeper dengan Docker
![Screenshot 2025-05-22 201715](https://github.com/user-attachments/assets/351e344d-5487-463f-ad68-81b287e01114)

Kemudian Jalankan Command `docker-compose up -d`
dan cek kontainer yg sedang berjalan `docker ps`

## 1. Buat Topik Kafka

```
docker exec -it <kafka_container_name> bash
kafka-topics --create --topic sensor-suhu-gudang --bootstrap-server localhost:9092
kafka-topics --create --topic sensor-kelembaban-gudang --bootstrap-server localhost:9092
```

![Screenshot 2025-05-22 202114](https://github.com/user-attachments/assets/d9906629-3239-4db3-876b-267d3df46223)

## 2. Simulasikan Data Sensor (Producer Kafka)
- Buat virtual environment
```
python -m venv venv
venv\Scripts\activate 
```
- Install Kafka library
```pip install kafka-python```
- Buat file producer
```
New-Item -Path "producer_suhu.py" -ItemType "File"
New-Item -Path "producer_kelembaban.py" -ItemType "File"
```
  
![Screenshot 2025-05-22 202700](https://github.com/user-attachments/assets/94bd3c89-25d3-4bc2-9552-d8579e8f4d87)

 ### a. Suhu
* Konfigurasi

![Screenshot 2025-05-22 202735](https://github.com/user-attachments/assets/eed59054-007d-49b0-8825-710e0f04e181)

* Hasil dengan menjalankan `python producer_suhu.py`
  
![Screenshot 2025-05-22 204552](https://github.com/user-attachments/assets/c0478d91-7b06-4901-8f38-be1c4f71e9ca)


 ### b. Kelembaban
 * Konfigurasi
   
![Screenshot 2025-05-22 202926](https://github.com/user-attachments/assets/cf134b40-2606-4b04-adc4-84bdf9624a61)

* Hasil dengan menjalankan `python producer_kelembaban.py`

![Screenshot 2025-05-22 204415](https://github.com/user-attachments/assets/7f67fd07-f5d8-46f7-8ad5-866b386cbb9e)

## 3. Konsumsi dan Olah Data dengan PySpark

### Setup Pyspark
- Install Pyspark `pip install pyspark`
- Buat file `New-Item -Path "consumer_filtering.py" -ItemType "File"`
- Jalankan `python consumer_filtering.py`

![image](https://github.com/user-attachments/assets/28fced39-2ecf-4fe9-b345-e696b1d5d3ec)

![image](https://github.com/user-attachments/assets/7cc06fe1-376c-4e69-80f3-7a2cf85404b7)

## 4.  Gabungkan Stream dari Dua Sensor
- Masuk ke container dan install `kafka-python`
  ```
  docker exec -it consumer bash
  pip install kafka-python
  ```
- Jalankan Consumer
`python consumer_filter.py`

![image](https://github.com/user-attachments/assets/4ff47bf5-443f-4261-86c3-0d1cfb060540)

![image](https://github.com/user-attachments/assets/d5e267fb-b17b-43dd-9b97-9967edfe013f)


