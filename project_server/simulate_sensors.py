import random
import requests
import time
from datetime import datetime

def simulate(user_id):
    while True:
        SENSOR_NAMES = ["temp", "humidity", "smoke", "movement"]
        sensor_name = SENSOR_NAMES[random.randint(0,3)]
        ROOM_NAMES = ["toilette", "chambre", "garage", "salon"]
        room_name = ROOM_NAMES[random.randint(0,3)]
        CONTROLABLE_NAMES = ["fenetre", "lumiere", "porte", "rideau"]
        controlable_name = CONTROLABLE_NAMES[random.randint(0,3)]
        send_room_controlable_value(controlable=controlable_name,user=user_id,room=room_name)
        if sensor_name == "smoke" or sensor_name == "movement" :
            sensor_value = True if random.randint(0,1) else False
        elif sensor_name == "temp" :
            sensor_value = random.uniform(-20,50)
        elif sensor_name == "humidity" :
            sensor_value = random.random()*100
        print(sensor_value, sensor_name)
        send_sensor_value(value=sensor_value,user=user_id,sensor_type=sensor_name)
        time.sleep(10)

def send_sensor_value(value,user,sensor_type):
    url = f"http://127.0.0.1:5000/{sensor_type}/{user}"  
    headers = {'Content-Type': 'application/json'}
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {'value': value, 'timestamp': timestamp}

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        print('Sensor value sent successfully')
    else:
        print('Failed to send sensor value. Status code:', response.status_code)

def send_room_controlable_value(controlable,user,room):
    url = f"http://127.0.0.1:5000/room/{user}/{room}/{controlable}"  
    headers = {'Content-Type': 'application/json'}
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {'state': controlable, 'timestamp': timestamp}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print('Sensor value sent successfully')
    else:
        print('Failed to send sensor value. Status code:', response.status_code)

REAL_USER_ID = "-NX_qq3ESQlIb7T7W_tN"

simulate(user_id=REAL_USER_ID)