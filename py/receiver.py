#!/home/maryush/Documents/IoT/venv/bin/python3

# pylint: disable=missing-docstring

import ssl
import paho.mqtt.client as mqtt
import mysql.connector as mysql

# The broker name or IP address.
BROKER = "127.0.0.1"

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
client.enable_logger()

client.tls_set(ca_certs="keys/ca.crt", certfile="keys/client.crt", keyfile="keys/client.key",tls_version=ssl.PROTOCOL_TLSv1_2)
client.tls_insecure_set(True)

def process_message(client, userdata, message):
    # Decode message.
    message_decoded = str(message.payload.decode("utf-8"))
    save_message_to_db(message_decoded)

def save_message_to_db(message):
    # Parse the message
    parts = message.split(";")
    if(parts[0] == "alert"):
        process_alert(parts)

def process_alert(parts):
    if len(parts) == 5:
        action, cause, room_nr, date = parts[1], parts[2], parts[3], parts[4]

        # Insert data into the database
        insert_query = "INSERT INTO alert (action, cause, room_nr, date) VALUES (%s, %s, %s, %s)"
        insert_data = (action, cause, room_nr, date)
        cursor.execute(insert_query, insert_data)
        db.commit()

        print(f"Run action: {action}")
    else:
        print("Invalid message format!")


def connect_to_broker():
    # Connect to the broker.
    client.connect(BROKER, port=8883)
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
