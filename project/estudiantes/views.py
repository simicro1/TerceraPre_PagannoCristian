from django.shortcuts import render

from cursos import models

def home(request):
    consulta = request.GET.get("consulta", None)
    
    if consulta:
        query = models.Estudiante.objects.filter(nombre__icontains=consulta)
    else:
        query = models.Estudiante.objects.all()
    context = {"estudiantes" : query}
    return render(request, "estudiantes/index.html", context)

