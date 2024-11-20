from flask import Flask, render_template, jsonify
from kafka import KafkaConsumer
import json
import threading

app = Flask(__name__)
weather_data = []

def consume_messages():
    global weather_data
    consumer = KafkaConsumer(
        'weather_data',
        bootstrap_servers='kafka:9092',
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )
    for message in consumer:
        weather_data.append(message.value)
        print(f"Received message: {message.value}")

# Start the consumer thread
threading.Thread(target=consume_messages, daemon=True).start()

@app.route('/')
def index():
    return render_template('index.html', weather_data=weather_data)

@app.route('/api/weather')
def get_weather_data():
    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(debug=True)