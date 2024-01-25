import paho.mqtt.client as mqtt
from config_server import MQTT_CONFIG
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

def connect(client ,process_message=None):
    print(f"Establishing with connection {config['broker']}:{config['port']} ")
    client.connect(config['broker'], port=config['port'])
    if process_message:
        client.on_message = process_message

def publish_message(client, topic, message):
    client.publish(topic, str(message))
    print(f"Publishing '{message}' to {topic}...")


def disconnect(client):
    client.disconnect()

def subscribe(client,topic):
    client.subscribe(topic)
    print(f"Subscribing to {topic}...")

def unsubscribe(client,topic):
    client.unsubscribe(topic)
    print(f"Unsubscribing from {topic}...")