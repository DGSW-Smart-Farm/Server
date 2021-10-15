import paho.mqtt.client as mqtt
import json

broker = '13.209.41.37'

class mqtt_publish():
    def __init__(self):
        self.mqtt = mqtt.Client("python_hub")   # Mqtt Client 오브젝트 생성
        self.mqtt.connect(broker, 1883)         # MQTT 서버에 연결
        self.mqtt.loop(2)                       # Timeout - 2sec

    def led(self, status):
        if status == 'true':
            response = {
                "type": "led",
                "cmd": "on"
            }
            self.mqtt.publish("smartfarm/control", json.dumps(response).encode())      # 토픽과 메세지 발행
        elif status == 'false':
            response = {
                "type": "led",
                "cmd": "off"
            }
            self.mqtt.publish("smartfarm/control", json.dumps(response).encode())

    def fan(self, status):
        if status == 'true':
            response = {
                "type": "fan",
                "cmd": "on"
            }
            self.mqtt.publish("smartfarm/control", json.dumps(response).encode())
        elif status == 'false':
            response = {
                "type": "fan",
                "cmd": "off"
            }
            self.mqtt.publish("smartfarm/control", json.dumps(response).encode())

    def water(self, status):
        if status == 'true':
            response = {
                "type": "water",
                "cmd": "on"
            }
            self.mqtt.pubclish("smartfarm/control", json.dumps(response).encode())
        elif status == 'false':
            response = {
                "type": "water",
                "cmd": "off"
            }
            self.mqtt.publish("smartfarm/control", json.dumps(response).encode())