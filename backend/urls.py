from django.urls import path
import backend.views as views

urlpatterns = [
    # Auth
    path('check_time', views.count_down),
    path('check_location', views.check_location),
]
