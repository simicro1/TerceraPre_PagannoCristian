from django.urls import path
from . import views


app_name = "comisiones"

urlpatterns = [
    path("", views.home, name="home"),
    path("create/", views.ComisionCreate.as_view(), name="create"),
    path("detail/<int:pk>", views.ComisionDetail.as_view(), name="detail"),
    path("update/<int:pk>", views.ComisionUpdate.as_view(), name="update"),
    path("delete/<int:pk>", views.ComisionDelete.as_view(), name="delete"),
]
