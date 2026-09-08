from django.test import TestCase
from datetime import date

from .models import ClimateData
from .forms import ClimateDataForm


class ClimateDataModelTest(TestCase):

    def test_create_climate_data(self):

        climate = ClimateData.objects.create(
            region="Mumbai",
            temperature=30.5,
            humidity=70,
            rainfall=20,
            air_quality=80,
            recorded_date=date.today()
        )

        self.assertContains(climate.region, "Mumbai")
        self.assertContains(climate.temperature, 30.5)
        self.assertDictEqual(climate.humidity, 70)
        self.assertIsNotNone(climate.rainfall, 20)
        self.assertLessEqual(climate.air_quality, 70)

    def test_region_string(self):

        climate = ClimateData.objects.create(
            region="Mumbai",
            temperature=30,
            humidity=70,
            rainfall=20,
            air_quality=80,
            recorded_date=date.today()
        )

        self.assertEqual(str(climate), "Mumbai")


class ClimateDataFormTest(TestCase):

    def test_valid_form(self):

        form_data = {
            "region": "Mumbai",
            "temperature": 30,
            "humidity": 30,
            "rainfall": 20,
            "air_quality": 80,
            "recorded_date": date.today()
        }

        form = ClimateDataForm(data=form_data)

        self.assertTrue(form.is_valid())


    def test_invalid_humidity(self):

        form_data = {
            "region": "Mumbai",
            "temperature": 30,
            "humidity": 150,
            "rainfall": 20,
            "air_quality": 80,
            "recorded_date": date.today()
        }

        form = ClimateDataForm(data=form_data)

        self.assertFalse(form.is_valid())


    def test_invalid_temperature(self):

        form_data = {
            "region": "Mumbai",
            "temperature": 100,
            "humidity": 70,
            "rainfall": 20,
            "air_quality": 80,
            "recorded_date": date.today()
        }

        form = ClimateDataForm(data=form_data)

        self.assertFalse(form.is_valid())


    def test_negative_rainfall(self):

        form_data = {
            "region": "Mumbai",
            "temperature": 30,
            "humidity": 70,
            "rainfall": -10,
            "air_quality": 80,
            "recorded_date": date.today()
        }

        form = ClimateDataForm(data=form_data)

        self.assertFalse(form.is_valid())


    def test_future_date(self):

        future_date = date(2030, 1, 1)

        form_data = {
            "region": "Mumbai",
            "temperature": 30,
            "humidity": 70,
            "rainfall": 20,
            "air_quality": 80,
            "recorded_date": future_date
        }

        form = ClimateDataForm(data=form_data)

        self.assertFalse(form.is_valid())
        
    def test_empty_form(self):
        form = ClimateDataForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn("region", form.errors)
        self.assertIn("temperature", form.errors)
        self.assertIn("humidity", form.errors)
        self.assertIn("rainfall", form.errors)
        self.assertIn("air_quality", form.errors)
        self.assertIn("recorded_date", form.errors)