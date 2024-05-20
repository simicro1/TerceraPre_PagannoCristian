from django.urls import path
from . import views

app_name = "estudiantes"

urlpatterns = [
    path("", views.home, name="home"),
    path("create/", views.EstudianteCreate.as_view(), name="create"),
    path("detail/<int:pk>", views.EstudianteDetail.as_view(), name="detail"),
    path("update/<int:pk>", views.EstudianteUpdate.as_view(), name="update"),
    path("delete/<int:pk>", views.EstudianteDelete.as_view(), name="delete"),
]