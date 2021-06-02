from django.db import models

# Create your models here.
class sensor(models.Model):
    humidity_gnd_status = models.IntegerField()
    humidity_gnd_value = models.IntegerField()
    humidity_gnd_time = models.DateTimeField()

    humidity_status = models.IntegerField()
    humidity_value = models.IntegerField()
    humidity_time = models.DateTimeField()

    fertilizer_status = models.IntegerField()
    fertilizer_time = models.DateTimeField()

    co2_status = models.IntegerField()
    co2_value = models.IntegerField()
    co2_time = models.DateTimeField()

    led_status = models.BooleanField()
    led_value = models.IntegerField()
    led_time = models.DateTimeField()

    temp_status = models.IntegerField()
    temp_value = models.IntegerField()
    temp_time = models.DateTimeField()