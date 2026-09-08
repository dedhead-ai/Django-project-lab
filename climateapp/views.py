from django.shortcuts import render, redirect, get_object_or_404

from .models import ClimateData, WeatherStation
from .forms import ClimateDataForm

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ClimateData
from .serializers import ClimateDataSerializer, WeatherStationSerializer


@api_view(['GET'])
def climate_data_api(request):

    climate_data = ClimateData.objects.all()

    serializer = ClimateDataSerializer(
        climate_data,
        many=True
    )

    return Response(serializer.data)


def home(request):
    return render(
        request,
        'climateapp/home.html'
    )


def about(request):
    return render(
        request,
        'climateapp/about.html'
    )


def climate_data(request):

    data = ClimateData.objects.all()

    return render(
        request,
        'climateapp/climate_data.html',
        {'data': data}
    )


def add_climate(request):

    if request.method == 'POST':

        form = ClimateDataForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('climate_data')

    else:

        form = ClimateDataForm()

    return render(
        request,
        'climateapp/add_climate.html',
        {'form': form}
    )


def detail(request, id):

    climate = get_object_or_404(
        ClimateData,
        id=id
    )

    return render(
        request,
        'climateapp/detail.html',
        {'climate': climate}
    )
    
@api_view(['GET'])
def weather_station_api(request):

    weather_stations = WeatherStation.objects.all()

    serializer = WeatherStationSerializer(
        weather_stations,
        many=True
    )

    return Response(serializer.data)

