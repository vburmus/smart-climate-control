#!/home/maryush/Documents/IoT/venv/bin/python3

# pylint: disable=no-member
# pylint: disable=missing-docstring

import time
from datetime import datetime
from mqtt_utils_client import connect,configure_broker,disconnect,publish_message,subscribe
import random
import threading
from config_client import MQTT_CONFIG,get_topic
config = MQTT_CONFIG
class RoomManager:
    def __init__(self):
        self.client = configure_broker()
        self.room_info = None
        self.publish_thread = None
        self.publish_event = None

    def get_current_datetime(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def read_sensor_data(self):
        temperature = round(random.uniform(20.0, 30.0), 2)
        humidity = round(random.uniform(30.0, 70.0), 2)
        pressure = round(random.uniform(900.0, 1100.0), 2)
        return f"sensor_data;{temperature};{humidity};{pressure};{self.get_current_datetime()}"

    def read_user_input(self):
        print("Client setup, to shutdown press CTRL + C")
        room_id = input("Enter room ID: ")
        room_name = input("Enter room name: ")
        preferred_temp = float(input("Enter preferred temperature: "))
        self.room_info = (room_id, room_name, preferred_temp)

    def room_create_message(self):
        return f"{self.room_info[0]};{self.room_info[1]};{self.room_info[2]}"
    
    def process_message(self, client, userdata, message):
        message_decoded = str(message.payload.decode("utf-8"))
        print(message_decoded)

    def establish_connection(self):
        connect(self.client,self.process_message,self.room_create_message())
        subscribe(self.client,self.room_info[0])

    def send_disconnect_message(self):
        publish_message(self.client,get_topic(MQTT_CONFIG['client_topic'],self.room_info[0]),"disconnect")
    
    def publish_sensor_data(self):
        while True:
            time.sleep(30)
            if self.publish_event.is_set():
                self.send_disconnect_message()
                break
            else:
                publish_message(self.client,get_topic(MQTT_CONFIG['client_topic'],self.room_info[0]),self.read_sensor_data())

    def run(self):
        self.read_user_input()
        try:
            self.establish_connection()
            self.publish_thread = threading.Thread(target=self.publish_sensor_data)
            self.publish_event = threading.Event()
            self.publish_thread.start()

            while self.client.loop() == 0:
                pass
            
        except KeyboardInterrupt:
            print("Shutting down....")
        finally:
            self.publish_event.set()
            self.publish_thread.join()
            disconnect(self.client)

if __name__ == "__main__":
    room_manager = RoomManager()
    room_manager.run()