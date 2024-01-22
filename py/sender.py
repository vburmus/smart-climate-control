#!/home/maryush/Documents/IoT/venv/bin/python3

# pylint: disable=no-member
# pylint: disable=missing-docstring

import time
from datetime import datetime
from mqtt_utils import connect,configure_broker,disconnect,publish_message

client = configure_broker()

def get_current_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def send_alerts():
    alert_messages = [
        f"alert;call firefighters;smoke detected;1;{get_current_datetime()}",
        f"alert;decrease temperature;temperature too high;2;{get_current_datetime()}",
        f"alert;increase temperature;temperature too low;3;{get_current_datetime()}",
        f"alert;increase humidity;humidity too low;1;{get_current_datetime()}",
        f"alert;decrease humidity;humidity too high;2;{get_current_datetime()}"
    ]
    for message in alert_messages:
        publish_message(client,message)
        print(f"Published message: {message}")
        time.sleep(1)

if __name__ == "__main__":
    connect(client)
    send_alerts()
    disconnect(client)