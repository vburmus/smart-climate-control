import paho.mqtt.client as mqtt
from config import MQTT_CONFIG
config = MQTT_CONFIG

def configure_broker():
    client = mqtt.Client()
    client.tls_set(
        ca_certs=config['ca_certs'],
        certfile=config['certfile'],
        keyfile=config['keyfile'],
        tls_version=config['tls_version']
    )
    client.tls_insecure_set(config['tls_insecure_set'])
    return client

def connect(client):
    client.connect(config['broker'], port=config['port'])

def publish_message(client, message):
    client.publish(config['topic'], str(message))

def disconnect(client):
    client.disconnect()

def subscribe(client):
    client.subscribe(config['topic'])