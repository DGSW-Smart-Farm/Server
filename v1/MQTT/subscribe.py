import time
import paho.mqtt.client as paho
import json

class MQTT:
    def __init__(self):
        self.broker = '13.209.41.37'
        self.port = 1883
        self.topic = 'smartfarm/sensor'
        self.client = None
        
        # sensor Value
        self.temp = None
        self.humidity = None
        self.humidity_gnd = None
        self.air = None
        self.led_status = None
        self.fan_status = None

    def connect_mqtt(self) -> paho:
        def on_connect(client, userdate, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)
        client = paho.Client()
        client.on_connect = on_connect
        client.connect(self.broker, self.port)
        return client
    
    def subscribe(self, client: paho):
        def on_mesage(client, userdata, msg):
            recv = msg.payload.decode()
            j = json.loads(recv)
            if j:
                self.temp = j['temperature']
                self.humidity = j['humidity']
                self.humidity_gnd = j['soil_humidity']
                self.air = j['air']
                self.led_status = j['led_stat']
                self.fan_status = j['fan_stat']
                print('this is got : {}', format(j))  # 가져온 값 출력
            else:
                print('no data....')

        client.subscribe(self.topic)
        client.on_message = on_mesage

    def run(self):
        self.client = self.connect_mqtt()
        self.subscribe(self.client)
        self.client.loop_start()
        print('run!!')
        time.sleep(2)
        self.get_data()

    def get_data(self):
        if ( (self.temp == None) & (self.humidity == None) & (self.humidity_gnd == None) & (self.air == None) ):
            returnValue = {
                'temp': 0,
                'humidity': 0,
                'humiditi_gnd': 0,
                'air': 0,
                'led_stat': 0,
                'fan_stat': 0
            }
            return returnValue
        
        else:
            returnValue = {
                'temp': self.temp,
                'humidity': self.humidity,
                'humidity_gnd': self.humidity_gnd,
                'air': self.air,
                'led_stat': self.led_status,
                'fan_stat': self.fan_status
            }
            return returnValue