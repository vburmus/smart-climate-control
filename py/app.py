#!/home/maryush/Documents/IoT/venv/bin/python3
from flask import Flask, jsonify,request
from mqtt_utils import connect,configure_broker,publish_message
from db_utils import connect_to_db
app = Flask(__name__)

db = connect_to_db()
client = configure_broker()
cursor = db.cursor()

@app.route('/api/v1/send_message', methods=['POST'])
def send_mqtt_message():
    try:
        data = request.get_json()
        message = data['message']
        publish_message(client, str(message))
        return jsonify(message=f'MQTT message sent: {message}'), 200

    except Exception as e:
        return jsonify(error=str(e)), 400
    
@app.route('/api/v1/rooms', methods=['GET'])
def get_all_rooms():
    select_query = "SELECT * FROM room"
    cursor.execute(select_query)
    rooms = cursor.fetchall()
    print(rooms)
    room_list = []
    for room in rooms:
        room_dict = {
            'id': room[0],
            'name': room[1],
            'preferred_temp': room[2]
        }
        room_list.append(room_dict)

    return jsonify(rooms=room_list)

@app.route('/api/v1/rooms', methods=['POST'])
def create_room():
    try:
        data = request.get_json()
        id = data['id']
        name = data['name']
        preferred_temp = data['preferred_temp']
        insert_query = "INSERT INTO room (id,name, preferred_temp) VALUES (%s,%s, %s)"
        insert_data = (id,name, preferred_temp)
        cursor.execute(insert_query, insert_data)
        db.commit()
        return jsonify(message='Room created successfully'), 201

    except Exception as e:
        return jsonify(error=str(e)), 400
    
if __name__ == '__main__':
    connect(client)
    app.run(debug=True, host='0.0.0.0', port=5000)