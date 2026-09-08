from django import forms
from .models import ClimateData
from datetime import date


class ClimateDataForm(forms.ModelForm):

    class Meta:
        model = ClimateData

        fields = [
            'region',
            'temperature',
            'humidity',
            'rainfall',
            'air_quality',
            'recorded_date'
        ]

        widgets = {
            'recorded_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }

    def clean_region(self):

        region = self.cleaned_data.get('region')

        if not region:
            raise forms.ValidationError(
                "Region name is required."
            )

        if len(region) < 3:
            raise forms.ValidationError(
                "Region name must contain at least 3 characters."
            )

        return region

    def clean_temperature(self):

        temperature = self.cleaned_data.get('temperature')

        if temperature < -50 or temperature > 60:
            raise forms.ValidationError(
                "Temperature must be between -50°C and 60°C."
            )

        return temperature

    def clean_humidity(self):

        humidity = self.cleaned_data.get('humidity')

        if humidity < 0 or humidity > 100:
            raise forms.ValidationError(
                "Humidity must be between 0% and 100%."
            )

        return humidity

    def clean_rainfall(self):

        rainfall = self.cleaned_data.get('rainfall')

        if rainfall < 0:
            raise forms.ValidationError(
                "Rainfall cannot be negative."
            )

        return rainfall

    def clean_air_quality(self):

        air_quality = self.cleaned_data.get('air_quality')

        if air_quality < 0:
            raise forms.ValidationError(
                "Air quality cannot be negative."
            )

        return air_quality

    def clean_recorded_date(self):

        recorded_date = self.cleaned_data.get('recorded_date')

        if recorded_date > date.today():
            raise forms.ValidationError(
                "Recorded date cannot be in the future."
            )

        return recorded_date





