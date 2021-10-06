import time
import paho.mqtt.client as paho
import json

broker = '13.209.41.37'

def on_connect(client, userdata, flags, rc):
    client.subscribe("smartfarm/sensor")#subscribe

#define callback
def on_message(client, userdata, message):
    print(message.topic, message.payload)
    pass

class mqtt:
    def __init__(self):
        self.client = paho.Client()
        self.client.on_connect = on_connect
        self.client.on_message = on_message
    
        self.client.connect(broker, 1883)
        print('connect')
