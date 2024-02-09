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
___
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
___
### System architecture
![system](https://github.com/vburmus/smart-climate-control/assets/118392004/bb320d61-e86e-4a7d-84e7-d742e7b2fd15)
___
### User interface 
![ui1](https://github.com/vburmus/smart-climate-control/assets/118392004/4821a559-032b-434d-8414-bb9e78508a4c)
![ui2](https://github.com/vburmus/smart-climate-control/assets/118392004/8f993852-af3c-447d-a8e5-8a6f91b83a58)
![ui3](https://github.com/vburmus/smart-climate-control/assets/118392004/3f59e418-35c7-4a6d-9ed9-c8ae687cc800)
![ui4](https://github.com/vburmus/smart-climate-control/assets/118392004/db0d42f3-a6d4-4754-b7b5-684f1e9e9481)
