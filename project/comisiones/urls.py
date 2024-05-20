from django.urls import path
from . import views


app_name = "comisiones"

urlpatterns = [
    path("", views.home, name="home"),
    path("create/", views.ComisionCreate.as_view(), name="create"),
]
