from django.views import View
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt    # csrf 비활성화 라이브러리
from django.utils.decorators import method_decorator    # csrf 비활성화를 위한 메서드, 클래스 데코레이터
from .MQTT.publish import *
from .MQTT.subscribe import *

from .__init__ import recv

# -1 or 0 or 1  ==  -1 = 낮음(부족), 0 = 적당, 1 = 높음(많음)
@method_decorator(csrf_exempt, name='dispatch')         # csrf 비활성화
class get_all_sensor(View):
    def get(self, request):
        value = recv()
        print(value)
        returnValue = {
            "humidity_gnd": {
                "status": value['humidity_gnd_status'],
                "value": value['humidity_gnd'],  # Percent
            },
            "humidity": {
                "status": value['humidity_status'],
                "value": value['humidity'],
            },
            "co2": {
                "status": value['air_status'],
                "value": value['air'],
            },
            "temp": {
                "status": value['temp_status'],
                "value": value['temp'],
            }
        }

        if (value['led_status'] == 1) and (value['fan_status'] == 1):
            returnValue['led'] = {'status': True}
            returnValue['fan'] = {'status': True}

        elif (value['led_status'] == 0) and (value['fan_status'] == 1):
            returnValue['led'] = {'status': False}
            returnValue['fan'] = {'status': True}

        elif (value['led_status'] == 1) and (value['fan_status'] == 0):
            returnValue['led'] = {'status': True}
            returnValue['fan'] = {'status': False}

        elif (value['led_status'] == 0) and (value['fan_status'] == 0):
            returnValue['led'] = {'status': False}
            returnValue['fan'] = {'status': False}
        return JsonResponse(returnValue)

@method_decorator(csrf_exempt, name='dispatch')
class temp(View):
    def get(self, request):
        value = recv()
        returnValue = {
            "status": value['temp_status'],
            "value": value['temp']
        }
        return JsonResponse(returnValue)

@method_decorator(csrf_exempt, name='dispatch')
class humidity_gnd(View):
    def get(self, request):
        value = recv()
        returnValue = {
            "status": value['humidity_gnd_status'],
            "value": value['humidity_gnd']
        }
        return JsonResponse(returnValue)

@method_decorator(csrf_exempt, name='dispatch')
class humidity(View):
    def get(self, request):
        value = recv()
        returnValue = {
            "status": value['humidity_status'],
            "value": value['humidity'],
        }
        return JsonResponse(returnValue)

@method_decorator(csrf_exempt, name='dispatch')
class air(View):
    def get(self, request):
        value = recv()
        returnValue = {
            "status": value['air_status'],
            "value": value['air']
        }
        return JsonResponse(returnValue)

@method_decorator(csrf_exempt, name='dispatch')
class led(View):
    def get(self, request):
        value = recv()
        if value['led_status'] == 1:
            returnvalue = {
                "status": True
            }
            return JsonResponse(returnvalue)

        elif value['led_status'] == 0:
            returnvalue = {
                "status": False
            }
            return JsonResponse(returnvalue)

@method_decorator(csrf_exempt, name='dispatch')
class fan(View):
    def get(self, request):
        value = recv()
        if value['fan_status'] == 1:
            returnValue = {
                "status": True
            }
            return JsonResponse(returnValue)
        elif value['fan_status'] == 0:
            returnValue = {
                "status": False
            }
            return JsonResponse(returnValue)

@method_decorator(csrf_exempt, name='dispatch')
class control_fan(View):
    def post(self, request):
        try:
            if request.META['CONTENT_TYPE'] == "application/json":
                request = json.loads(request.body)
                fanstatus = request['status']
            else:
                fanstatus = request.POST['status']
            mqtt = mqtt_publish()
            mqtt.fan(fanstatus)
            return HttpResponse('OK', status=200)
        except Exception as E:
            print(E)
            return HttpResponse('UNKNOWN SERVER ERROR ACCORDED', status=500)

@method_decorator(csrf_exempt, name='dispatch')
class control_led(View):
    def post(self, request):
        try:
            if request.META['CONTENT_TYPE'] == "application/json":
                request = json.loads(request.body)
                ledstatus = request['status']
            else:
                ledstatus = request.POST['status']
            mqtt = mqtt_publish()
            mqtt.led(ledstatus)
            return HttpResponse('OK', status=200)
        except Exception as E:
            print(E)
            return HttpResponse('UNKNOWN SERVER ERROR ACCORDED', status=500)
