from django.db import models
from django.conf import settings
from django.utils import timezone

class humidity_gnd(models.Model):
    status = models.IntegerField()
    value = models.IntegerField()
    time = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.time)

class waterpump(models.Model):
    time = models.DateTimeField(default=timezone.now)
    status = models.BooleanField()
    def __str__(self):
        return str(self.time)

class humidity(models.Model):
    status = models.IntegerField()
    value = models.IntegerField()
    time = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.time)

class fertilizer(models.Model):
    status = models.IntegerField()
    time = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.time)

class co2(models.Model):
    status = models.IntegerField()
    value = models.IntegerField()
    time = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.time)

class led(models.Model):
    status = models.BooleanField()
    value = models.IntegerField()
    time = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.time)

class temp(models.Model):
    status = models.IntegerField()
    value = models.IntegerField()
    time = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.time)
