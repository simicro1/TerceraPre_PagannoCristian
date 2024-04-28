from django.urls import path
from . import views

app_name = "estudiantes"

urlpatterns = [
    path("", views.home, name="home"),
]