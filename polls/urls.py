from django.urls import include, path, admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("climateapp.urls")),
    path("polls/", include("polls.urls")),
]