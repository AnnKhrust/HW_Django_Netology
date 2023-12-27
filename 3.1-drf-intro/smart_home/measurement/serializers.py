from rest_framework import serializers

from .models import Sensor, Measurement


class MeasurementsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'

class SensorsListSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']

class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementsListSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']