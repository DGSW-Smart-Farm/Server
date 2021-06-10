from django.db import models
from django.conf import settings
from django.utils import timezone

class humidity_gnd(models.Model):
    humidity_gnd_status = models.IntegerField()
    humidity_gnd_value = models.IntegerField()

class waterpump(models.Model):
    time = models.DateTimeField(default=timezone.now)
    status = models.BooleanField()

class humidity(models.Model):
    status = models.IntegerField()
    value = models.IntegerField()
    time = models.DateTimeField(default=timezone.now)

class fertilizer(models.Model):
    status = models.IntegerField()
    time = models.DateTimeField(default=timezone.now)

class co2(models.Model):
    status = models.IntegerField()
    value = models.IntegerField()
    time = models.DateTimeField(default=timezone.now)

class led(models.Model):
    status = models.BooleanField()
    value = models.IntegerField()
    time = models.DateTimeField(default=timezone.now)

class temp(models.Model):
    status = models.IntegerField()
    value = models.IntegerField()
    time = models.DateTimeField(default=timezone.now)
