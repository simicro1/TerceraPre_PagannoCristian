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
from . import models, forms

def home(request):
    consulta = request.GET.get("consulta", None)
    
    if consulta:
        query = models.Curso.objects.filter(nombre__icontains=consulta)
    else:
        query = models.Curso.objects.all()

    context = {"cursos" : query}
    return render(request, "cursos/index.html", context)

class CursoCreate(CreateView):
    model = models.Curso
    form_class = forms.CursoForm
    success_url = reverse_lazy("cursos:home")
    
class CursoUpdate(UpdateView):
    model = models.Curso
    form_class = forms.CursoForm
    success_url = reverse_lazy("cursos:home")


class CursoDetail(DetailView):
    model = models.Curso


class CursoDelete(LoginRequiredMixin, DeleteView):
    model = models.Curso
    success_url = reverse_lazy("cursos:home")