from rest_framework import serializers
from .models import ClimateData, WeatherStation


class ClimateDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClimateData
        fields = '__all__'


class WeatherStationSerializer(serializers.ModelSerializer):

    class Meta:
        model = WeatherStation
        fields = '__all__'