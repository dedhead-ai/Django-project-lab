from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default="India")

    def __str__(self):
        return self.name


class WeatherStation(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class ClimateData(models.Model):
    region = models.CharField(max_length=100)
    temperature = models.FloatField()
    humidity = models.FloatField()
    rainfall = models.FloatField()
    air_quality = models.FloatField()
    recorded_date = models.DateField()

    def __str__(self):
        return self.region


class ClimateAlert(models.Model):
    ALERT_TYPES = [
        ('HEAT', 'Heat Wave'),
        ('FLOOD', 'Flood'),
        ('STORM', 'Storm'),
        ('AIR', 'Poor Air Quality'),
    ]

    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE
    )

    alert_type = models.CharField(
        max_length=20,
        choices=ALERT_TYPES
    )

    message = models.TextField()

    severity = models.CharField(
        max_length=20
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return f"{self.region.name} - {self.alert_type}"

