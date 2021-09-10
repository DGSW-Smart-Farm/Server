# -*- coding:utf-8 -*-
import paho.mqtt.client as mqtt

# 서버로부터 CONNTACK 응답을 받을 때 호출되는 콜백
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("smartfarm/sensor")  # 구독 "smartfarm/sensor"

# 서버로부터 publish message를 받을 때 호출되는 콜백
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))  # 토픽과 메세지를 출력한다.

class mqtt_subscribe():
    def __init__(self):
        self.client = mqtt.Client()
        self.client.on_connect = on_connect
        self.client.on_message = on_message
        self.client.connect("web.dgsw.kr", 1883)
        self.client.loop_forever()


