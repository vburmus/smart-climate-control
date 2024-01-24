import paho.mqtt.client as mqtt
from config_client import MQTT_CONFIG, get_topic
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

def connect(client, process_message, connection_message):
    print(f"Establishing with connection {config['broker']}:{config['port']} ")
    client.connect(config['broker'], port=config['port'])
    print(f"Subscribing to {config['connection_topic']}...")
    client.publish(config['connection_topic'], connection_message)
    client.on_message = process_message

    
def publish_message(client,topic, message):
    print(f"Publishing '{message}' to {topic}...")
    client.publish(topic, str(message))
    

def disconnect(client):
    client.disconnect()

def subscribe(client,room_id):
    topic = get_topic(config['server_topic'],room_id)
    print(f"Subscribing to {topic}...")
    client.subscribe(topic)