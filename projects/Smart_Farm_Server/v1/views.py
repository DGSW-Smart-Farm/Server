from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse

import json

from django.views.decorators.csrf import csrf_exempt    # csrf 비활성화 라이브러리
from django.utils.decorators import method_decorator    # csrf 비활성화를 위한 메서드, 클래스 데코레이터


# -1 or 0 or 1  ==  -1 = 낮음(부족), 0 = 적당, 1 = 높음(많음)
@method_decorator(csrf_exempt, name='dispatch')         # csrf 비활성화
class get_all_sensor(View):
    def get(self, request):
        returnvalue = {
            "humidity_gnd": {
                "status": 0,
                "value": 48,        # Percent
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
        returnvalue = {
            "status": 0,
            "value": 48
        }
        return JsonResponse(returnvalue)

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
            "value": 48
        }
        return JsonResponse(returnvalue)

@method_decorator(csrf_exempt, name='dispatch')
class get_home(View):
    def get(self, request):
        returnvalue = {
            "humidity_gnd": {
                "status": 0,
                "value": 48  # Percent
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