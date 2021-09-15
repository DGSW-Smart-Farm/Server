import paho.mqtt.client as mqtt
import json

broker = ''  # mqtt broker 주소

class mqtt_publish:
  def __init__(self) -> None:
    self.mqtt = mqtt.Client('Python hub')  # Mqtt Client 오브젝트 생성
    self.mqtt.connect(broker, 1883)        # MQTT 서버에 연결
    self.mqtt.loop(2)                      # Time out - 2sec
  
  def led(self, status):
    if status:
      response = {
        "type": "led",
        "cmd": "on"
      }
      mqtt_publish("smartfarm/control", json.dump(response).encode())
    else:
      response = {
        "type": "led",
        "cmd": "off"
      }
      mqtt_publish("smartfarm/control", json.dump(response).encode())
  
  def fan(self, status):
    if status:
      response = {
        "type": "fan",
        "cmd": "on"
      }
      mqtt_publish("smartfarm/control", json.dump(response).encode())
    else:
      response = {
        "type": "fan",
        "cmd": "off"
      }
      mqtt_publish("smartfarm/comtrol", json.dump(response).encode())