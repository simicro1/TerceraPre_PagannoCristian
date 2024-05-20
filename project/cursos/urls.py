from django.urls import path
from . import views

app_name = "cursos"

urlpatterns = [
    path("", views.home, name="home"),
    path("create/", views.CursoCreate.as_view(), name="create"),
    path("detail/<int:pk>", views.CursoDetail.as_view(), name="detail"),
    path("update/<int:pk>", views.CursoUpdate.as_view(), name="update"),
    path("delete/<int:pk>", views.CursoDelete.as_view(), name="delete"),
]