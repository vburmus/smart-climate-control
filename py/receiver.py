#source /home/maryush/Documents/IoT/venv/bin/activate

# pylint: disable=missing-docstring

import paho.mqtt.client as mqtt
import mysql.connector as mysql

# The broker name or IP address.
BROKER = "localhost"

# Database
db = mysql.connect(
    host="localhost",
    user="marpad",
    password="marpad",
    database="smart-climate-controll"
)

# DB cursor
cursor = db.cursor()

# The MQTT client.
client = mqtt.Client()

def process_message(client, userdata, message):
    # Decode message.
    message_decoded = str(message.payload.decode("utf-8"))
    print(message_decoded)

def connect_to_broker():
    # Connect to the broker.
    client.connect(BROKER)
    # Send message about conenction.
    client.on_message = process_message
    # Starts client and subscribe.
    client.subscribe("test")
    while client.loop() == 0:
        pass

def disconnect_from_broker():
    # Disconnet the client.
    client.loop_stop()
    client.disconnect()


def run_receiver():
    connect_to_broker()
    disconnect_from_broker()


if __name__ == "__main__":
    run_receiver()
