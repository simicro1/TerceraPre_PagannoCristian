from django.shortcuts import render

from cursos import models

def home(request):
    query = models.Estudiante.objects.all()
    context = {"estudiantes" : query}
    return render(request, "estudiantes/index.html", context)

