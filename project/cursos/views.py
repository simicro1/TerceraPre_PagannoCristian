from django.shortcuts import render
from . import models

def home(request):
    consulta = request.GET.get("consulta", None)
    
    if consulta:
        query = models.Curso.objects.filter(nombre__icontains=consulta)
    else:
        query = models.Curso.objects.all()

    context = {"cursos" : query}
    return render(request, "cursos/index.html", context)
