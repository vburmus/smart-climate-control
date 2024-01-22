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
    select_query = "SELECT r.id,r.name, m.temperature, m.humidity,m.pressure, MAX(m.time) as last_time FROM room AS r JOIN measurement AS m ON r.id=m.room_id GROUP BY id;"
    cursor.execute(select_query)
    rooms = cursor.fetchall()
    room_list = []
    for room in rooms:
        room_dict = {
            'id': room[0],
            'name': room[1],
            'temperature': room[2],
            'humidity':room[3],
            'pressure':room[4],
            'last_time':room[5].strftime("%Y-%m-%d %H:%M:%S")
        }
        room_list.append(room_dict)

    return jsonify(rooms=room_list)

@app.route('/api/v1/alerts', methods=['GET'])
def get_all_allerts():
    select_query = "SELECT * FROM alert;"
    cursor.execute(select_query)
    allerts = cursor.fetchall()
    room_list = []
    for allert in allerts:
        room_dict = {
            'id': allert[0],
            'action': allert[1],
            'cause': allert[2],
            'date':allert[3].strftime("%Y-%m-%d %H:%M:%S"),
            'room_id': allert[4]
        }
        room_list.append(room_dict)
    return jsonify(rooms=room_list)

@app.route('/api/v1/rooms/<int:room_id>', methods=['GET'])
def get_room_by_id(room_id):
    select_query = "SELECT r.*, m.temperature, m.humidity, m.pressure, m.time FROM room as r JOIN measurement as m ON r.id = m.room_id WHERE r.id = %s ORDER BY m.time DESC LIMIT 1"
    cursor.execute(select_query, (room_id,))
    room = cursor.fetchone()

    if room:
        room_dict = {
            'id': room[0],
            'name': room[1],
            'preferred_temp': room[2],
            'temperature': room[3],
            'humidity': room[4],
            'pressure': room[5],
            'time': room[6].strftime("%Y-%m-%d %H:%M:%S")
        }
        return jsonify(room_dict)
    else:
        return jsonify(message='Room not found'), 404

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