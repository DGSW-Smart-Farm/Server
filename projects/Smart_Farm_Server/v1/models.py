from django.db import models
from django.conf import settings
from django.utils import timezone

class sensor(models.Model):
    humidity_gnd_status = models.IntegerField()
    humidity_gnd_value = models.IntegerField()
    humidity_gnd_time = models.DateTimeField(default=timezone.now)

    humidity_status = models.IntegerField()
    humidity_value = models.IntegerField()
    humidity_time = models.DateTimeField(default=timezone.now)

    fertilizer_status = models.IntegerField()
    fertilizer_time = models.DateTimeField(default=timezone.now)

    co2_status = models.IntegerField()
    co2_value = models.IntegerField()
    co2_time = models.DateTimeField(default=timezone.now)

    led_status = models.BooleanField()
    led_value = models.IntegerField()
    led_time = models.DateTimeField(default=timezone.now)

    temp_status = models.IntegerField()
    temp_value = models.IntegerField()
    temp_time = models.DateTimeField(default=timezone.now)