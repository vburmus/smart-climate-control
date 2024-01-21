#!/home/maryush/Documents/IoT/venv/bin/python3

# pylint: disable=no-member
# pylint: disable=missing-docstring

import time
import ssl
from datetime import datetime
import paho.mqtt.client as mqtt

BROKER = "127.0.0.1"
client = mqtt.Client()

client.tls_set(ca_certs="keys/ca.crt", certfile="keys/client.crt", keyfile="keys/client.key",tls_version=ssl.PROTOCOL_TLSv1_2)
client.tls_insecure_set(True)

def get_current_datetime():
    # Get the current date and time in the specified format
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def publish_message(message):
    client.publish("test", str(message))

def connect_to_broker():
    client.connect(BROKER, port=8883)

def disconnect_from_broker():
    client.disconnect()

def send_alerts():
    alert_messages = [
        f"alert;call firefighters;smoke detected;101;{get_current_datetime()}",
        f"alert;decrease temperature;temperature too high;103;{get_current_datetime()}",
        f"alert;increase temperature;temperature too low;301;{get_current_datetime()}",
        f"alert;increase humidity;humidity too low;102;{get_current_datetime()}",
        f"alert;decrease humidity;humidity too high;202;{get_current_datetime()}"
    ]
    for message in alert_messages:
        publish_message(message)
        print(f"Published message: {message}")
        time.sleep(1)

if __name__ == "__main__":
    connect_to_broker()
    send_alerts()
    disconnect_from_broker()