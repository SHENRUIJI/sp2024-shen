import requests
from kafka import KafkaProducer
import time
import json

API_KEY = 'eea8a51369d64ae920854e58937c94a8'
CITY = "Saint Petersburg"
KAFKA_TOPIC = 'weather_data'
KAFKA_SERVER = 'kafka:9092'

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER, value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def get_weather_data():
    url = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}'
    try:
        response = requests.get(url, timeout=10)  # timeout=10s
        response.raise_for_status()  # Check if the request was successful.
        return response.json()
    except requests.exceptions.Timeout:
        print("Request timed out, please try again later")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve weather data: {e}")
        return None

while True:
    weather_data = get_weather_data()
    if weather_data:
        producer.send(KAFKA_TOPIC, weather_data)
        print(f"Weather Data: {weather_data}")
    time.sleep(60)  # 60s every time