from .MQTT import subscribe as mqtt

MQTT = mqtt.MQTT()
MQTT.run()
sensorValue = MQTT.get_data()

def recv():
  return sensorValue