from .MQTT import subscribe as mqtt

MQTT = mqtt.MQTT()
MQTT.run()

def recv():
  sensorValue = MQTT.get_data()
  return sensorValue