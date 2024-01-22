#!/home/maryush/Documents/IoT/venv/bin/python3

# pylint: disable=no-member
# pylint: disable=missing-docstring

import time
from datetime import datetime
from mqtt_utils import connect,configure_broker,disconnect,publish_message
import random

class RoomManager:
    def __init__(self):
        self.client = configure_broker()
        self.room_info = None

    def get_current_datetime(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def generate_sensor_data(self):
        temperature = round(random.uniform(20.0, 30.0), 2)
        humidity = round(random.uniform(30.0, 70.0), 2)
        pressure = round(random.uniform(900.0, 1100.0), 2)
        return temperature, humidity, pressure

    def get_user_input(self):
        room_id = input("Enter room ID: ")
        room_name = input("Enter room name: ")
        preferred_temp = float(input("Enter preferred temperature: "))
        self.room_info = (room_id, room_name, preferred_temp)

    def send_sensor_data(self):
        temperature, humidity, pressure = self.generate_sensor_data()
        sensor_data_message = f"sensor_data;{self.room_info[0]};{temperature};{humidity};{pressure};{self.get_current_datetime()}"
        publish_message(self.client, sensor_data_message)
        print(f"Published sensor data: {sensor_data_message}")

    def send_room_information(self):
        room_info_message = f"room;create;{self.room_info[0]};{self.room_info[1]};{self.room_info[2]}"
        publish_message(self.client, room_info_message)
        print(f"Published room information: {room_info_message}")

    def establish_connection(self):
        connect(self.client)
        self.get_user_input()
        self.send_room_information()

    def run(self):
        try:
            self.establish_connection()
            while True:
                time.sleep(10)
                self.send_sensor_data()
        except KeyboardInterrupt:
            print("Script terminated by user.")
        finally:
            disconnect(self.client)

if __name__ == "__main__":
    room_manager = RoomManager()
    room_manager.run()