from django.urls import path
from . import views

app_name = 'v1'
urlpatterns = [
    path('get_all_sensor/', views.get_all_sensor.as_view(), name='index'),
    path('fertilizer/', views.fertilizer.as_view(), name='index'),
    path('led/', views.led.as_view(), name='index'),
    path('humidity_gnd/', views.humidity_gnd.as_view(), name='index'),
    path('get_home/', views.get_home.as_view(), name='index'),
]