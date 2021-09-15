from time import sleep
import paho.mqtt.client as mqtt
import json

broker = ''  # mqtt broker 주소

# 서버로부터 CONTACK 응답을 받았을 때 호출 되는 콜백
def on_connect(client, userdata, flags, rc):
  print("Connected with result code " + str(rc))
  client.subscribe("smartfarm/sensor")

# 서버로부터 publish message를 받을 때 호출되는 콜백
def on_message(client, userdata, msg):
  print(msg.topic + " " + str(msg.payload))   # Topic과 Message를 출력한다.

class matt_subscribe():
  def __init__(self):
    self.client = mqtt.Client()
    self.client.on_connect = on_connect
    self.client.on_message = on_message
    self.client.connect(broker, 1883)