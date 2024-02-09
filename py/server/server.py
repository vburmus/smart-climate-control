#!/home/maryush/Documents/IoT/venv/bin/python3

# pylint: disable=missing-docstring

from mqtt_utils_server import connect,configure_broker,subscribe,disconnect,publish_message,unsubscribe
from db_utils import connect_to_db,close_db_connection
from config_server import MQTT_CONFIG, get_topic
import time
db = connect_to_db()

cursor = db.cursor()

client = configure_broker()

def process_message(client, userdata, message):
    message_decoded = str(message.payload.decode("utf-8"))
    parts = message_decoded.split(";")
    if(message.topic==MQTT_CONFIG['connection_topic']):
        process_client_creation(parts)
    elif(MQTT_CONFIG['client_topic'] in message.topic):
        room_id = message.topic.split("-")[-1]
        parts.insert(1,room_id)
        process_client_message(parts) 

def process_client_creation(parts):
    room_id = create_room(parts)
    subscribe(client, get_topic(MQTT_CONFIG['client_topic'],room_id))
    time.sleep(1)
    publish_message(client, get_topic(MQTT_CONFIG['server_topic'],room_id), "Server: registered Pi client")  

def change_client_avaliability_client(room_id,is_enabled):
    deactivate_query = f"UPDATE room SET is_active = {is_enabled} WHERE id = %s"
    insert_data = (room_id,)
    cursor.execute(deactivate_query, insert_data)
    db.commit()
    print(f"Client {room_id} ", "active" if is_enabled else "inactive")

def process_client_disconnect(room_id):
    unsubscribe(client, get_topic(MQTT_CONFIG['client_topic'],room_id))
    change_client_avaliability_client(room_id,0)

def process_client_message(parts):
    if(parts[0] == "alert"):
        process_alert(parts)
    elif(parts[0] == "update_temperature"):
        room_id, temp = parts[1],parts[2]
        update_room(room_id,preferred_temp=temp)
        publish_message(client, get_topic(MQTT_CONFIG['server_topic'],room_id), f"update_temperature;{temp}")  
    elif(parts[0] == "sensor_data"):
        process_measurement(parts)
    elif(parts[0] == "disconnect"):
        process_client_disconnect(parts[1])
    
def process_measurement(parts):
    if len(parts)==6:
        room_id,temperature,humidity,pressure,date = parts[1],parts[2],parts[3],parts[4],parts[5]
        insert_query = "INSERT INTO measurement (temperature,humidity, pressure, room_id, time) VALUES (%s, %s, %s, %s, %s)"
        insert_data = (temperature, humidity, pressure, room_id, date)
        cursor.execute(insert_query, insert_data)
        db.commit()
        print(f"Measured in room {room_id}: t = {temperature}C, p = {pressure}Pa, h = {humidity}%")
    else:
        print("Invalid message format!")

def process_alert(parts):
    if len(parts) == 5:
        action, cause, room_nr, date = parts[1], parts[2], parts[3], parts[4]
        insert_query = "INSERT INTO alert (action, cause, room_id, date) VALUES (%s, %s, %s, %s)"
        insert_data = (action, cause, room_nr, date)
        cursor.execute(insert_query, insert_data)
        db.commit()
        print(f"Run action: {action}")
    else:
        print("Invalid message format!")

def update_room(room_id, name=None, preferred_temp = None):
    if(name or preferred_temp):
        params = []
        if preferred_temp:
             params.append(f"preferred_temp = {preferred_temp}")
        if name:
            params.append(f"name = '{name}'")
        insert_query = f"UPDATE room SET " + ", ".join(params) + f" WHERE id = {room_id}"
        cursor.execute(insert_query)
        db.commit()
        print(f"Updated room {room_id}: {name} {preferred_temp}C")
    else:    
        print("Wrong parameters got! Provide name or temp!")

def create_room(parts):
    if len(parts) == 3:
        room_id,name, preferred_temp = parts[0], parts[1], parts[2]

        select_query = "SELECT * FROM room WHERE id = %s"
        cursor.execute(select_query, (room_id,))
        existing_room = cursor.fetchone()

        if existing_room:
            print(f"Room with ID {room_id} already exists. Subscribing to topic.")
            change_client_avaliability_client(room_id,1)
            update_room(room_id,name,preferred_temp)
            return room_id
        
        insert_query = "INSERT INTO room (id,name,preferred_temp,is_active) VALUES (%s,%s,%s,True)"
        insert_data = (room_id,name,preferred_temp)
        cursor.execute(insert_query, insert_data)
        db.commit()
        print(f"Created room: {name}")
        return room_id
    else:
        print("Invalid message format!")

def connect_to_broker():
    connect(client,process_message)
    subscribe(client,MQTT_CONFIG['connection_topic'])
    while client.loop() == 0:
        pass

def disconnect_from_broker():
    client.loop_stop()
    disconnect(client)


def run_receiver():
    connect_to_broker()
    disconnect_from_broker()
    close_db_connection()


if __name__ == "__main__":
    run_receiver()