# Smart Climate Control
___
## Technologies
![Raspberry Pi](https://img.shields.io/badge/-RaspberryPi-C51A4A?style=for-the-badge&logo=Raspberry-Pi)
![Debian](https://img.shields.io/badge/Debian-D70A53?style=for-the-badge&logo=debian&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Mosquitto](https://img.shields.io/badge/mosquitto-%233C5280.svg?style=for-the-badge&logo=eclipsemosquitto&logoColor=white)
![TypeScript](https://img.shields.io/badge/typescript-%23007ACC.svg?style=for-the-badge&logo=typescript&logoColor=white)
![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)
![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

## Description 
The project involves creating a temperature and humidity control system using the Raspberry Pi platform and dedicated sensors. Below are the
main functional requirements for the client (Raspberry Pi) and the server.
### For the client (Raspberry Pi with sensors)
1. Reading temperature, pressure and humidity from sensors
2. Data transmission using SSL encrypted MQTT protocol to the server
3. Visualization of sensor data on the OLED display
4. Enforcement of manual control
### For the server
1. Receiving data from clients via the MQTT protocol
2. Storing received data in a database
3. Running an API that allows you to retrieve data from the database
4. Providing a web interface 
5. Ability to add additional rooms (Plug and Play)
6. Sending feedback to clients
7. Sending notifications to users
