from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from . import forms
from cursos import models

def home(request):
    consulta = request.GET.get("consulta", None)
    
    if consulta:
        query = models.Estudiante.objects.filter(nombre__icontains=consulta)
    else:
        query = models.Estudiante.objects.all()
    context = {"estudiantes" : query}
    return render(request, "estudiantes/index.html", context)

class EstudianteCreate(CreateView):
    model = models.Estudiante
    form_class = forms.EstudianteForm
    success_url = reverse_lazy("estudiantes:home")
    
class EstudianteUpdate(UpdateView):
    model = models.Estudiante
    form_class = forms.EstudianteForm
    success_url = reverse_lazy("estudiantes:home")


class EstudianteDetail(DetailView):
    model = models.Estudiante


class EstudianteDelete(LoginRequiredMixin, DeleteView):
    model = models.Estudiante
    success_url = reverse_lazy("estudiantes:home")