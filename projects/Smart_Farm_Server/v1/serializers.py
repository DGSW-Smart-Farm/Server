from rest_framework import serializers
from .models import *


class fertilizerSerialzer(serializers.ModelSerializer):
    class Meta:
        model = fertilizer
        fields = '__all__'


