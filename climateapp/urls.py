from django.urls import path
from . import views


urlpatterns = [

    path(
        '',
        views.home,
        name='home'
    ),

    path(
        'about/',
        views.about,
        name='about'
    ),

    path(
        'climate-data/',
        views.climate_data,
        name='climate_data'
    ),

    path(
        'add-climate/',
        views.add_climate,
        name='add_climate'
    ),

    path(
        'climate/<int:id>/',
        views.detail,
        name='detail'
    ),
    path(
        'api/climate-data/',
        views.climate_data_api,
        name='climate_data_api'
    ),
    path(
    'api/weather-stations/',
    views.weather_station_api,
    name='weather_station_api'
    ),

]