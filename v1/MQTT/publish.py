# -*- coding:utf-8 -*-
from django.http import response
import paho.mqtt.client as mqtt
import json

class mqtt_publish():
    def __init__(self):
        self.mqtt = mqtt.Client("python_hub")   # Mqtt Client 오브젝트 생성
        self.mqtt.connect("web.dgsw.kr", 1883)  # MQTT 서버에 연결
        self.mqtt.loop(2)                       # Timeout - 2sec

    def led(self, status):
        if status:
            response = {
                "type": "led",
                "cmd": "on"
            }
            mqtt.publish("smartfarm/control", json.dumps(response).encode())      # 토픽과 메세지 발행
        else:
            response = {
                "type": "led",
                "cmd": "off"
            }
            mqtt.publish("smartfarm/control", json.dumps(response).encode())

    def fan(self, status):
        if status:
            response = {
                "type": "fan",
                "cmd": "on"
            }
            mqtt.publish("smartfarm/control", json.dumps(response).encode())
        else:
            response = {
                "type": "fan",
                "cmd": "off"
            }
            mqtt.publish("smartfarm/control", json.dumps(response).encode())

    def water(self, status):
        if status:
            response = {
                "type": "water",
                "cmd": "on"
            }
            mqtt.pubclish("smartfarm/control", json.dumps(response).encode())
        else:
            response = {
                "type": "water",
                "cmd": "off"
            }
            mqtt.publish("smartfarm/control", json.dumps(response).encode())