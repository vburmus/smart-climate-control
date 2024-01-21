#source /home/maryush/Documents/IoT/venv/bin/activate

# pylint: disable=no-member
# pylint: disable=missing-docstring

import paho.mqtt.client as mqtt

BROKER = "localhost"
client = mqtt.Client()

def publish_message(message):
    client.publish("test", str(message))

def connect_to_broker():
    client.connect(BROKER)
    publish_message("Client connected")

def disconnect_from_broker():
    publish_message("Client disconnected")
    client.disconnect()


def test():
    print('Write message')
    connect_to_broker()
    while input() != "exit":
        message = input()
        publish_message(message)
    disconnect_from_broker()



if __name__ == "__main__":
    test()
    