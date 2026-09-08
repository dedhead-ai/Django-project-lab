from django.contrib import admin
from .models import (
    Region,
    WeatherStation,
    ClimateData,
    ClimateAlert
)

admin.site.register(Region)
admin.site.register(WeatherStation)
admin.site.register(ClimateData)
admin.site.register(ClimateAlert)
    
    