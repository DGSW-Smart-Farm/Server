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
                # print('this is got : {}', format(j))  # 가져온 값 출력
                # print(type(self.temp), type(self.humidity), type(self.humidity_gnd), type(self.air))
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
        if (self.temp == None) and (self.humidity == None) and (self.humidity_gnd == None) and (self.air == None) and (self.led_status == None) and (self.fan_status):
            returnValue = {
                'temp': 0,
                'temp_status': 0,
                'humidity': 0,
                'humidity_status': 0,
                'humidity_gnd': 0,
                'humidity_gnd_status': 0,
                'air': 0,
                'air_status': 0,
                'led_status': 0,
                'fan_status': 0
            }
            return returnValue
        
        else:
            returnValue = {
                'temp': self.temp,
                'humidity': self.humidity,
                'humidity_gnd': self.humidity_gnd,
                'air': self.air,
                'led_status': self.led_status,
                'fan_status': self.fan_status
            }
            
            try:
                if self.temp < 15:
                    returnValue['temp_status'] = -1
                elif (self.temp >= 15) and (self.temp <= 25):
                    returnValue['temp_status'] = 0
                else:
                    returnValue['temp_status'] = 1
            except TypeError:
                print('Cannot connect MQTT')

            try:
                if self.humidity < 30:
                    returnValue['humidity_status'] = -1
                elif (self.humidity >= 30) and (self.humidity <= 70):
                    returnValue['humidity_status'] = 0
                else:
                    returnValue['humidity_status'] = 1
            except TypeError:
                print('Cannot connect MQTT')

            try:
                if self.humidity_gnd < 20:
                    returnValue['humidity_gnd_status'] = -1
                elif (self.humidity_gnd >= 20) and (self.humidity_gnd < 25):
                    returnValue['humidity_gnd_status'] = 0
                else:
                    returnValue['humidity_gnd_status'] = 1
            except TypeError:
                print('Cannot connect MQTT')

            try:
                if int(self.air) < 1000:
                    returnValue['air_status'] = -1
                elif (int(self.air) >= 1000) and (int(self.air) < 5000):
                    returnValue['air_status'] = 0
                else:
                    returnValue['air_status'] = 1
            except TypeError:
                print('Cannot connect MQTT')

            return returnValue