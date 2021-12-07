from django.urls import path
from . import views


urlpatterns = [
    path("", views.input_date, name="input_date"),
    path("result/<inputed_date>", views.result_in_weeks, name="weeks"),
]
