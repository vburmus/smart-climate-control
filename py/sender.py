#source /home/maryush/Documents/IoT/venv/bin/activate

# pylint: disable=no-member
# pylint: disable=missing-docstring

import paho.mqtt.client as mqtt
import ssl 
BROKER = "127.0.0.1"
client = mqtt.Client()

client.tls_set(ca_certs="keys/ca.crt", certfile="keys/client.crt", keyfile="keys/client.key",tls_version=ssl.PROTOCOL_TLSv1_2)
client.tls_insecure_set(True)

def publish_message(message):
    client.publish("test", str(message))

def connect_to_broker():
    client.connect(BROKER, port=8883)
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
    