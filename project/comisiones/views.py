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
        query = models.Comision.objects.filter(nombre__icontains=consulta)
    else:
        query = models.Comision.objects.all()
    
    context = {"comisiones" : query}
    return render(request, "comisiones/index.html", context)

class ComisionCreate(CreateView):
    model = models.Comision
    form_class = forms.ComisionForm
    success_url = reverse_lazy("comisiones:home")
    
class ComisionUpdate(UpdateView):
    model = models.Comision
    form_class = forms.ComisionForm
    success_url = reverse_lazy("comisiones:home")


class ComisionDetail(DetailView):
    model = models.Comision


class ComisionDelete(LoginRequiredMixin, DeleteView):
    model = models.Comision
    success_url = reverse_lazy("comisiones:home")