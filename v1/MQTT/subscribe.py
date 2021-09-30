import time
import paho.mqtt.client as paho
import json

broker = '13.125.136.38'

#define callback
def on_message(client, userdata, message):
    global recvData

    recvData = json.loads(message.payload)

def returnData():
    return recvData

client = paho.Client()
client.on_message = on_message
print("connecting to broker ", broker)
client.connect(broker, 1883)
print("subscribing ")
client.subscribe("smartfarm/sensor")#subscribe
client.loop_start() #start loop to process received messages
time.sleep(1)
