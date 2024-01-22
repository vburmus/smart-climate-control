#!/home/maryush/Documents/IoT/venv/bin/python3

# pylint: disable=missing-docstring

from mqtt_utils import connect,configure_broker,subscribe,disconnect
from db_utils import connect_to_db,close_db_connection

db = connect_to_db()

cursor = db.cursor()

client = configure_broker()

def process_message(client, userdata, message):
    message_decoded = str(message.payload.decode("utf-8"))
    save_message_to_db(message_decoded)

def save_message_to_db(message):
    parts = message.split(";")
    if(parts[0] == "alert"):
        process_alert(parts)
    elif(parts[0] == "room"):
        process_room_action(parts)
    

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

def create_room(parts):
    if len(parts) == 5:
        id,name, preferred_temp = parts[2], parts[3],parts[4]
        insert_query = "INSERT INTO room (id,name,preferred_temp) VALUES (%s,%s, %s)"
        insert_data = (id,name,preferred_temp)
        cursor.execute(insert_query, insert_data)
        db.commit()
        print(f"Created room: {name}")
    else:
        print("Invalid message format!")

def update_preferred_temp(parts):
    if len(parts) == 4:
        id, preferred_temp = parts[2], parts[3]
        insert_query = "UPDATE room SET preferred_temp = %s WHERE id = %s"
        insert_data = (preferred_temp,id)
        cursor.execute(insert_query, insert_data)
        db.commit()
        print(f"Updated tempreture in room: {id} to {preferred_temp}")
    else:
        print("Invalid message format!")

def process_room_action(parts):
    if(parts[1]=="create"):
            create_room(parts)
    elif (parts[1]=="update") :
            update_preferred_temp(parts)
    else:
         print("Invalid message format!")


def connect_to_broker():
    connect(client)
    client.on_message = process_message
    subscribe(client)
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