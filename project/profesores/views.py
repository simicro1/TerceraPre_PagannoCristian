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

from cursos import models
from . import forms

def home(request):
    consulta = request.GET.get("consulta", None)
    
    if consulta:
        query = models.Profesor.objects.filter(nombre__icontains=consulta)
    else:
        query = models.Profesor.objects.all()
    context = {"profesores" : query}
    return render(request, "profesores/index.html", context)

class ProfesorCreate(CreateView):
    model = models.Profesor
    form_class = forms.ProfesorForm
    success_url = reverse_lazy("profesores:home")
    
class ProfesorUpdate(UpdateView):
    model = models.Profesor
    form_class = forms.ProfesorForm
    success_url = reverse_lazy("profesores:home")


class ProfesorDetail(DetailView):
    model = models.Profesor


class ProfesorDelete(LoginRequiredMixin, DeleteView):
    model = models.Profesor
    success_url = reverse_lazy("profesores:home")