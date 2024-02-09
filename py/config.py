import ssl
DATABASE_CONFIG = {
    'host': 'localhost',
    'user': 'marpad',
    'password': 'marpad',
    'database': 'smart-climate-controll'
}

MQTT_CONFIG = {
    'broker': '127.0.0.1',
    'port': 8883,
    'topic': 'test',
    'ca_certs': 'keys/ca.crt',
    'certfile': 'keys/client.crt',
    'keyfile': 'keys/client.key',
    'tls_version': ssl.PROTOCOL_TLSv1_2,
    'tls_insecure_set': True
}