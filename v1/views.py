import json, v1.models, django

from django import http
from typing import cast

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt    # csrf 비활성화 라이브러리
from django.utils.decorators import method_decorator    # csrf 비활성화를 위한 메서드, 클래스 데코레이터
from django.utils import timezone
from .MQTT.publish import *
from .MQTT.subscribe import *

# from django.forms.models import model_to_dict
from django.core.serializers import serialize
from .serializers import *
import v1.models


# -1 or 0 or 1  ==  -1 = 낮음(부족), 0 = 적당, 1 = 높음(많음)
@method_decorator(csrf_exempt, name='dispatch')         # csrf 비활성화
class get_all_sensor(View):
    def get(self, request):
        returnvalue = {
            "humidity_gnd": {
                "status": 0,
                "value": 23,        # Percent
            },
            "humidity": {
                "status": 0,
                "value": 84,
            },
            "fertilizer": {
                "status": 0,
            },
            "co2": {
                "status": 0,
                "value": 1400,
            },
            "led": {
                "status": True,
                "time": 2367,
            },
            "temp": {
                "status": 0,
                "value": 28,
            }
        }
        return JsonResponse(returnvalue)

@method_decorator(csrf_exempt, name='dispatch')
class fertilizer(View):
    def get(self, request):
        
        return HttpResponse('NO_DATA', status = 404)

@method_decorator(csrf_exempt, name='dispatch')
class led(View):
    def get(self, request):
        returnvalue = {
            "status": True,
            "time": 2367
        }
        return JsonResponse(returnvalue)

@method_decorator(csrf_exempt, name='dispatch')
class temp(View):
    def get(self, request):
        returnvalue = {
            "status": 0,
            "time": 28
        }
        return JsonResponse(returnvalue)

@method_decorator(csrf_exempt, name='dispatch')
class humidity_gnd(View):
    def get(self, request):
        returnvalue = {
            "status": 0,
            "value": 20
        }
        return JsonResponse(returnvalue)

@method_decorator(csrf_exempt, name='dispatch')
class get_home(View):
    def get(self, request):
        returnvalue = {
            "humidity_gnd": {
                "status": 0,
                "value": 20  # Percent
            },
            "humidity": {
                "status": 0,
                "value": 84
            },
            "fertilizer": {
                "status": 0,
            },
            "co2": {
                "status": 0,
                "value": 1400
            },
            "led": {
                "status": True,
                "time": 2367,
            },
            "temp": {
                "status": 0,
                "value": 28,
            }
        }
        return JsonResponse(returnvalue)


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
            return HttpResponse('OK', status = 200)
        except:
            return HttpResponse('UNKNOWN SERVER ERROR ACCORDED', status = 500)


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
            return HttpResponse('OK', status = 200)
        except:
            return HttpResponse('UNKNOWN SERVER ERROR ACCORDED', status = 500)

@method_decorator(csrf_exempt, name='dispatch')
class control_water(View):
    def post(self, request):
        try:
            if request.META['CONTENT_TYPE'] == "application/json":
                request = json.loads(request.body)
                waterstatus = request['status']
            else:
                waterstatus = request.POST['status']
            mqtt = mqtt_publish()
            mqtt.water(waterstatus)
            return HttpResponse('OK', status = 200)
        except:
            return HttpResponse('UNKOWN SERVER ERROR ACCORDED', status = 500)