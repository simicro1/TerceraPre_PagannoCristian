from django.shortcuts import render

from cursos import models

def home(request):
    query = models.Profesor.objects.all()
    context = {"profesores" : query}
    return render(request, "profesores/index.html", context)
