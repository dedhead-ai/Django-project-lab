from django.contrib import admin

from .models import (
    Question,
    Choice,
    Region,
    WeatherStation,
    ClimateData,
    ClimateAlert,
)



class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2
    ordering = ["order"]



@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):

    list_display = (
        "question_text",
        "active",
        "created_at",
        "choice_count",
    )

    list_filter = (
        "active",
        "created_at",
    )

    search_fields = (
        "question_text",
    )

    ordering = (
        "-created_at",
    )

    list_per_page = 10

    inlines = [
        ChoiceInline,
    ]

    @admin.display(description="Choices")
    def choice_count(self, obj):
        return obj.choices.count()


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):

    list_display = (
        "choice_text",
        "question",
        "votes",
        "order",
    )

    list_filter = (
        "question",
    )

    search_fields = (
        "choice_text",
        "question__question_text",
    )

    ordering = (
        "question",
        "order",
    )

    list_per_page = 20

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "state",
        "country",
    )

    list_filter = (
        "state",
        "country",
    )

    search_fields = (
        "name",
        "state",
        "country",
    )

    ordering = (
        "country",
        "state",
        "name",
    )

    list_per_page = 20


@admin.register(WeatherStation)
class WeatherStationAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "location",
        "region",
        "latitude",
        "longitude",
    )

    list_filter = (
        "region",
    )

    search_fields = (
        "name",
        "location",
        "region__name",
    )

    ordering = (
        "region",
        "name",
    )

    list_per_page = 20


@admin.register(ClimateData)
class ClimateDataAdmin(admin.ModelAdmin):

    list_display = (
        "region",
        "temperature_display",
        "humidity_display",
        "rainfall_display",
        "air_quality_display",
        "recorded_date",
    )

    list_filter = (
        "recorded_date",
        "region",
    )

    search_fields = (
        "region",
    )

    ordering = (
        "-recorded_date",
    )

    date_hierarchy = "recorded_date"

    list_per_page = 20

    @admin.display(description="Temperature")
    def temperature_display(self, obj):
        return f"{obj.temperature} °C"

    @admin.display(description="Humidity")
    def humidity_display(self, obj):
        return f"{obj.humidity}%"

    @admin.display(description="Rainfall")
    def rainfall_display(self, obj):
        return f"{obj.rainfall} mm"

    @admin.display(description="Air Quality")
    def air_quality_display(self, obj):
        return obj.air_quality


@admin.register(ClimateAlert)
class ClimateAlertAdmin(admin.ModelAdmin):

    list_display = (
        "region",
        "alert_type",
        "severity",
        "is_active",
        "created_at",
    )

    list_filter = (
        "alert_type",
        "severity",
        "is_active",
        "created_at",
        "region",
    )

    search_fields = (
        "region__name",
        "message",
    )

    ordering = (
        "-created_at",
    )

    list_per_page = 20

    date_hierarchy = "created_at"

    
    